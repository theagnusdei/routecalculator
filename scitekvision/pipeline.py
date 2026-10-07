"""Orquestra as etapas e persiste o estado da edição em edicoes/AAAA-MM-DD/."""
from __future__ import annotations

import json
import logging
from datetime import date
from pathlib import Path

from . import coletor, docx_builder, extrator, ranking, redator
from .config import Config
from .modelos import Candidato, Pauta

log = logging.getLogger(__name__)


def _salvar_json(arq: Path, dados) -> None:
    arq.parent.mkdir(parents=True, exist_ok=True)
    arq.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def _ler_json(arq: Path):
    return json.loads(arq.read_text(encoding="utf-8"))


# ------------------------------------------------------------------ etapas
def selecionar(cfg: Config, edicao: date) -> dict[str, list[Candidato]]:
    pool = coletor.carregar_pool(cfg, edicao)
    if not pool:
        raise SystemExit(f"Nenhum candidato coletado para {edicao}. Rode `coletar` antes.")
    selecao = ranking.selecionar(pool, cfg)
    _salvar_json(cfg.pasta_edicao(edicao) / "selecao.json",
                 {k: [c.to_dict() for c in v] for k, v in selecao.items()})
    for cat, cands in selecao.items():
        log.info("[%s] %d candidatos; topo: %s", cat, len(cands), cands[0].titulo if cands else "—")
    return selecao


def extrair(cfg: Config, edicao: date) -> list[Pauta]:
    pasta = cfg.pasta_edicao(edicao)
    selecao = {k: [Candidato.from_dict(d) for d in v] for k, v in _ler_json(pasta / "selecao.json").items()}
    n = cfg.geral["selecao"]["artigos_por_categoria"]
    pautas: list[Pauta] = []
    for cat, cands in selecao.items():
        restantes = list(cands)
        for _ in range(n):
            if not restantes:
                break
            pauta = extrator.preparar_pauta(cat, restantes, pasta, cfg)
            if pauta is None:
                break
            # descarta os candidatos já tentados (preparar_pauta percorre a lista em ordem)
            restantes = restantes[restantes.index(pauta.candidato) + 1:]
            if pauta.status == "falhou" and cfg.categorias[cat].get("opcional"):
                continue  # editorias correlatas só entram se houver material
            pautas.append(pauta)
    salvar_pautas(cfg, edicao, pautas)
    exportar_fontes(cfg, edicao, pautas)
    return pautas


def exportar_fontes(cfg: Config, edicao: date, pautas: list[Pauta]) -> None:
    """Grava o material de cada pauta em Markdown (usado pelo modo Claude Code e pelo revisor)."""
    pasta = cfg.pasta_edicao(edicao) / "fontes"
    for p in pautas:
        if p.status != "extraida":
            continue
        c = p.candidato
        cob = "\n".join(f"- {u}" for u in c.cobertura[:5]) or "- nenhuma"
        md = (f"# {c.titulo}\n\n- Editoria: {cfg.categorias[p.categoria]['nome']} (`{p.categoria}`)\n"
              f"- Fonte: {c.fonte} — {c.url}\n- Autor: {p.autor_fonte or 'não informado'}\n"
              f"- Publicado: {c.publicado or 'não informado'}\n- Score: {c.score}\n"
              f"- Imagem: {p.imagem_arquivo or 'nenhuma'} | crédito: {p.imagem_credito} | licença: {p.imagem_licenca}\n\n"
              f"## Outras coberturas\n{cob}\n\n## Texto extraído\n\n{p.texto_fonte}\n")
        (pasta / f"{p.categoria}.md").parent.mkdir(parents=True, exist_ok=True)
        (pasta / f"{p.categoria}.md").write_text(md, encoding="utf-8")


def salvar_pautas(cfg: Config, edicao: date, pautas: list[Pauta]) -> None:
    _salvar_json(cfg.pasta_edicao(edicao) / "pautas.json", [p.to_dict() for p in pautas])


def carregar_pautas(cfg: Config, edicao: date) -> list[Pauta]:
    pasta = cfg.pasta_edicao(edicao)
    pautas = [Pauta.from_dict(d) for d in _ler_json(pasta / "pautas.json")]
    # Artigos gravados em artigos/<editoria>.json (pelo redator automático ou pelo Claude Code)
    for p in pautas:
        arq = pasta / "artigos" / f"{p.categoria}.json"
        if arq.exists() and p.status != "redigida":
            try:
                artigo = redator.extrair_json(arq.read_text(encoding="utf-8"))
                p.alertas_automaticos.extend(redator.validar(artigo, p, cfg))
                p.artigo, p.status, p.erro = artigo, "redigida", None
                p.backend = p.backend or "claude-code"
            except redator.ErroRedacao as e:
                p.alertas_automaticos.append(f"artigos/{p.categoria}.json inválido: {e}")
    return pautas


def redigir(cfg: Config, edicao: date, ignorar_prazo: bool = False) -> list[Pauta]:
    pautas = carregar_pautas(cfg, edicao)
    prazo = cfg.prazo("redacao", edicao)
    for p in pautas:
        if p.status != "extraida":
            continue
        if not ignorar_prazo and cfg.agora() >= prazo:
            p.status, p.erro = "fora_do_prazo", f"prazo de redação ({prazo:%H:%M}) atingido"
            continue
        log.info("[%s] redigindo: %s", p.categoria, p.candidato.titulo)
        redator.redigir(p, cfg)
        if p.artigo:
            _salvar_json(cfg.pasta_edicao(edicao) / "artigos" / f"{p.categoria}.json", p.artigo)
        salvar_pautas(cfg, edicao, pautas)  # salva a cada artigo: nada se perde se o job cair
    return pautas


def montar(cfg: Config, edicao: date) -> list[Path]:
    pautas = carregar_pautas(cfg, edicao)
    salvar_pautas(cfg, edicao, pautas)
    pasta = cfg.pasta_edicao(edicao)
    arquivos = docx_builder.montar(pautas, pasta, cfg, edicao)
    escrever_leia_me(cfg, edicao, pautas, arquivos)
    return arquivos


def escrever_leia_me(cfg: Config, edicao: date, pautas: list[Pauta], arquivos: list[Path]) -> None:
    pasta = cfg.pasta_edicao(edicao)
    linhas = [f"# {cfg.geral['saida']['nome_publicacao']} — edição {edicao:%d/%m/%Y}", "",
              f"Gerado em {cfg.agora():%d/%m/%Y %H:%M} ({cfg.geral['fuso_horario']}). "
              "Todos os artigos são **rascunhos** e precisam de revisão humana.", "",
              "| # | Editoria | Título | Status | Fonte | Alertas |", "|---|---|---|---|---|---|"]
    for i, p in enumerate(pautas, 1):
        titulo = ((p.artigo or {}).get("titulo") or p.candidato.titulo).replace("|", "/")
        alertas = len((p.artigo or {}).get("alertas_revisor", [])) + len(p.alertas_automaticos)
        linhas.append(f"| {i} | {cfg.categorias[p.categoria]['nome']} | {titulo} | {p.status} | "
                      f"[{p.candidato.fonte}]({p.candidato.url}) | {alertas} |")
    linhas += ["", "## Arquivos", *[f"- `{a.relative_to(pasta)}`" for a in arquivos], "",
               "## Como aprovar",
               "1. Baixe os `.docx`, revise usando o checklist ao final de cada artigo.",
               "2. Substitua no repositório os `.docx` revisados (ou comente no Pull Request o que mudar).",
               "3. Aprove e faça *merge* do Pull Request: o merge significa **aprovado para publicação**.",
               "4. Artigos reprovados: apague o `.docx` correspondente antes do merge."]
    (pasta / "LEIA-ME-REVISAO.md").write_text("\n".join(linhas) + "\n", encoding="utf-8")


def edicao_completa(cfg: Config, edicao: date, coletar: bool = True, ignorar_prazo: bool = False) -> list[Path]:
    if coletar:
        coletor.executar(cfg, edicao)
    selecionar(cfg, edicao)
    extrair(cfg, edicao)
    redigir(cfg, edicao, ignorar_prazo=ignorar_prazo)
    return montar(cfg, edicao)
