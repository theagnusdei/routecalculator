"""Etapa 4 — redação do artigo original com IA.

Backends (tentados na ordem de config.yaml → redacao.backends):
  claude-cli  Claude Code headless (`claude -p`) — usa a assinatura Claude Pro/Max já existente
              (CLAUDE_CODE_OAUTH_TOKEN, gerado com `claude setup-token`). Sem custo adicional.
  gemini      Google AI Studio (nível gratuito, GEMINI_API_KEY).
  anthropic   API da Anthropic (paga por uso, ANTHROPIC_API_KEY). Opcional.
  mock        Texto fictício, para testes offline.
"""
from __future__ import annotations

import json
import logging
import os
import re
import shutil
import subprocess
import time

import requests

from .config import Config
from .modelos import Pauta

log = logging.getLogger(__name__)

CAMPOS_OBRIGATORIOS = ["titulo", "subtitulo", "lead", "corpo", "por_que_importa", "pontos_chave",
                       "palavras_chave", "meta_descricao", "legenda_imagem", "nivel_confianca", "alertas_revisor"]


class ErroRedacao(Exception):
    pass


# ---------------------------------------------------------------- prompts
def prompt_sistema(cfg: Config) -> str:
    r = cfg.geral["redacao"]
    return (cfg.ler_prompt("redator_sistema.md")
            .replace("{palavras_min}", str(r["palavras_min"]))
            .replace("{palavras_max}", str(r["palavras_max"])))


def prompt_usuario(pauta: Pauta, cfg: Config) -> str:
    c = pauta.candidato
    limite = cfg.geral["redacao"]["max_caracteres_fonte"]
    nome_cat = cfg.categorias[pauta.categoria]["nome"]
    cobertura = "\n".join(f"- {u}" for u in c.cobertura[:5]) or "- (nenhuma identificada)"
    imagem = (f"Imagem: obtida de {pauta.imagem_credito} ({pauta.imagem_pagina})"
              if pauta.imagem_arquivo else "Imagem: nenhuma (escreva uma legenda sugerida para o editor escolher uma)")
    return f"""Editoria: {nome_cat}
Fonte original: {c.fonte} — {c.url}
Site: {pauta.site_fonte or c.fonte} | Autor original: {pauta.autor_fonte or "não informado"}
Publicado em: {c.publicado or "data não informada"}
Título original: {c.titulo}
Outras coberturas do mesmo assunto (só para contexto; não cite o que não estiver no texto abaixo):
{cobertura}
{imagem}

<texto_fonte>
{pauta.texto_fonte[:limite]}
</texto_fonte>

Escreva o artigo seguindo rigorosamente as regras e devolva apenas o JSON."""


# ---------------------------------------------------------------- backends
def _claude_cli(sistema: str, usuario: str, modelo: str) -> str:
    exe = shutil.which("claude")
    if not exe:
        raise ErroRedacao("Claude Code CLI não instalado (npm i -g @anthropic-ai/claude-code)")
    if not (os.environ.get("CLAUDE_CODE_OAUTH_TOKEN") or os.environ.get("ANTHROPIC_API_KEY")
            or os.path.exists(os.path.expanduser("~/.claude/.credentials.json"))):
        raise ErroRedacao("sem credencial do Claude Code (defina CLAUDE_CODE_OAUTH_TOKEN)")
    cmd = [exe, "-p", "--output-format", "json", "--model", modelo,
           "--append-system-prompt", sistema, "--disallowedTools", "Bash,Edit,Write,WebFetch,WebSearch"]
    proc = subprocess.run(cmd, input=usuario, capture_output=True, text=True, timeout=600)
    if proc.returncode != 0:
        raise ErroRedacao(f"claude -p falhou ({proc.returncode}): {proc.stderr[-500:]}")
    try:
        saida = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return proc.stdout
    if saida.get("is_error"):
        raise ErroRedacao(f"claude -p retornou erro: {saida.get('result', '')[:500]}")
    return saida.get("result", "")


def _gemini(sistema: str, usuario: str, modelo: str) -> str:
    chave = os.environ.get("GEMINI_API_KEY")
    if not chave:
        raise ErroRedacao("GEMINI_API_KEY não definida (crie grátis em https://aistudio.google.com/apikey)")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent"
    corpo = {
        "systemInstruction": {"parts": [{"text": sistema}]},
        "contents": [{"role": "user", "parts": [{"text": usuario}]}],
        "generationConfig": {"responseMimeType": "application/json", "temperature": 0.6},
    }
    for tentativa in range(4):
        r = requests.post(url, params={"key": chave}, json=corpo, timeout=300)
        if r.status_code in (429, 503):  # limite do nível gratuito: espera e tenta de novo
            time.sleep(30 * (tentativa + 1))
            continue
        if r.status_code != 200:
            raise ErroRedacao(f"Gemini HTTP {r.status_code}: {r.text[:300]}")
        partes = r.json()["candidates"][0]["content"]["parts"]
        return "".join(p.get("text", "") for p in partes)
    raise ErroRedacao("Gemini: limite de requisições excedido")


def _anthropic(sistema: str, usuario: str, modelo: str) -> str:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise ErroRedacao("ANTHROPIC_API_KEY não definida (backend pago, opcional)")
    import anthropic

    client = anthropic.Anthropic()
    resp = client.beta.messages.create(
        model=modelo,
        max_tokens=16000,
        system=sistema,
        output_config={"effort": "medium"},
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
        messages=[{"role": "user", "content": usuario}],
    )
    if resp.stop_reason == "refusal":
        raise ErroRedacao("modelo recusou a solicitação")
    return "".join(b.text for b in resp.content if b.type == "text")


def _mock(sistema: str, usuario: str, modelo: str) -> str:
    titulo = re.search(r"Título original: (.+)", usuario).group(1)
    par = ("Este é um parágrafo de teste gerado pelo backend mock, usado apenas para validar o "
           "pipeline de ponta a ponta sem chamar nenhum modelo de linguagem real. ") * 3
    return json.dumps({
        "titulo": f"[TESTE] {titulo[:70]}", "subtitulo": "Linha fina de teste",
        "lead": "Lead de teste.", "corpo": [{"intertitulo": f"Seção {i}", "paragrafos": [par, par]} for i in (1, 2, 3)],
        "por_que_importa": "Teste.", "pontos_chave": ["a", "b", "c"],
        "glossario": [{"termo": "mock", "definicao": "simulação"}], "palavras_chave": ["teste"],
        "meta_descricao": "teste", "legenda_imagem": "Imagem de teste", "nivel_confianca": "baixo",
        "alertas_revisor": ["Artigo gerado pelo backend mock."],
    }, ensure_ascii=False)


BACKENDS = {"claude-cli": _claude_cli, "gemini": _gemini, "anthropic": _anthropic, "mock": _mock}


# ---------------------------------------------------------------- validação
def extrair_json(texto: str) -> dict:
    texto = texto.strip()
    texto = re.sub(r"^```(?:json)?\s*|\s*```$", "", texto)
    inicio, fim = texto.find("{"), texto.rfind("}")
    if inicio < 0 or fim < 0:
        raise ErroRedacao("resposta sem JSON")
    try:
        return json.loads(texto[inicio: fim + 1])
    except json.JSONDecodeError as e:
        raise ErroRedacao(f"JSON inválido: {e}") from e


def contar_palavras(artigo: dict) -> int:
    texto = " ".join(p for s in artigo.get("corpo", []) for p in s.get("paragrafos", []))
    return len(texto.split())


def sobreposicao(artigo: dict, fonte: str, n: int = 8) -> float:
    """Fração de sequências de n palavras do artigo que aparecem literalmente na fonte."""
    def shingles(t: str) -> set[tuple[str, ...]]:
        p = re.findall(r"\w+", t.lower())
        return {tuple(p[i:i + n]) for i in range(len(p) - n + 1)}
    texto = " ".join([artigo.get("lead", "")] + [p for s in artigo.get("corpo", []) for p in s.get("paragrafos", [])])
    a = shingles(texto)
    return len(a & shingles(fonte)) / len(a) if a else 0.0


def validar(artigo: dict, pauta: Pauta, cfg: Config) -> list[str]:
    faltando = [c for c in CAMPOS_OBRIGATORIOS if not artigo.get(c)]
    if faltando:
        raise ErroRedacao(f"campos ausentes: {', '.join(faltando)}")
    alertas = []
    r = cfg.geral["redacao"]
    palavras = contar_palavras(artigo)
    if not r["palavras_min"] * 0.8 <= palavras <= r["palavras_max"] * 1.2:
        alertas.append(f"Tamanho fora do padrão: {palavras} palavras (alvo {r['palavras_min']}–{r['palavras_max']}).")
    sob = sobreposicao(artigo, pauta.texto_fonte)
    if sob > 0.05:
        alertas.append(f"Possível cópia: {sob:.0%} de trechos idênticos ao texto original — reescrever.")
    return alertas


# ---------------------------------------------------------------- orquestração
def redigir(pauta: Pauta, cfg: Config) -> None:
    r = cfg.geral["redacao"]
    sistema, usuario = prompt_sistema(cfg), prompt_usuario(pauta, cfg)
    erros = []
    for nome in r["backends"]:
        try:
            bruto = BACKENDS[nome](sistema, usuario, r["modelos"].get(nome, ""))
            artigo = extrair_json(bruto)
            pauta.alertas_automaticos.extend(validar(artigo, pauta, cfg))
            pauta.artigo, pauta.backend, pauta.status, pauta.erro = artigo, nome, "redigida", None
            time.sleep(r.get("pausa_entre_chamadas_segundos", {}).get(nome, 0))
            return
        except (ErroRedacao, subprocess.TimeoutExpired, requests.RequestException) as e:
            log.warning("[%s] backend %s falhou: %s", pauta.categoria, nome, e)
            erros.append(f"{nome}: {e}")
        except Exception as e:  # SDK opcional (anthropic) e erros inesperados não devem parar a edição
            log.exception("[%s] erro inesperado no backend %s", pauta.categoria, nome)
            erros.append(f"{nome}: {e!r}")
    pauta.status, pauta.erro = "falhou", " | ".join(erros)
