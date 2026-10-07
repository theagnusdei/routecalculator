"""Etapa 2 — pontuação de relevância e seleção das pautas por editoria.

score = autoridade da fonte + recência + aderência à editoria + repercussão
        (quantas fontes diferentes cobrem o mesmo assunto) + bônus de imagem
        - penalidades (promoções, podcasts, patrocinados...)
"""
from __future__ import annotations

import math
import re
from datetime import datetime, timezone

from .config import Config
from .modelos import Candidato

_PALAVRA = re.compile(r"[a-zà-ú0-9]{4,}", re.IGNORECASE)
_STOP = {"that", "with", "from", "this", "have", "will", "into", "their", "about", "after", "says", "said",
         "para", "como", "mais", "pela", "pelo", "sobre", "entre", "novo", "nova", "what", "your", "they"}


def tokens(texto: str) -> set[str]:
    return {p.lower() for p in _PALAVRA.findall(texto)} - _STOP


def jaccard(a: set[str], b: set[str]) -> float:
    return len(a & b) / len(a | b) if a and b else 0.0


def _horas_desde(iso: str | None, agora: datetime) -> float:
    if not iso:
        return 24.0  # sem data: trata como "ontem"
    return max(0.0, (agora - datetime.fromisoformat(iso)).total_seconds() / 3600)


def _hits(texto: str, palavras: list[str]) -> int:
    t = f" {texto.lower()} "
    n = 0
    for kw in palavras:
        k = kw.lower()
        if (len(k) <= 3 and re.search(rf"\b{re.escape(k)}\b", t)) or (len(k) > 3 and k in t):
            n += 1
    return n


def calcular_cobertura(pool: list[Candidato], limiar: float = 0.3) -> None:
    """Marca, para cada candidato, as matérias de OUTRAS fontes com título semelhante."""
    toks = [tokens(c.titulo) for c in pool]
    for i, c in enumerate(pool):
        c.cobertura = [
            o.url for j, o in enumerate(pool)
            if j != i and o.fonte != c.fonte and jaccard(toks[i], toks[j]) >= limiar
        ]


def pontuar(c: Candidato, categoria: str, cfg: Config, agora: datetime) -> float:
    sel = cfg.geral["selecao"]
    texto = f"{c.titulo} {c.resumo}"
    autoridade = 3.0 * c.peso_fonte
    recencia = 2.0 * math.pow(0.5, _horas_desde(c.publicado, agora) / sel["meia_vida_recencia_horas"])
    aderencia = 0.5 * min(_hits(texto, cfg.categorias[categoria].get("palavras_chave", [])), 4)
    repercussao = min(len({u for u in c.cobertura}), 3) * 1.0
    imagem = 0.3 if c.imagem_feed else 0.0
    penalidade = 3.0 if _hits(texto, cfg.termos_penalizados) else 0.0
    return round(autoridade + recencia + aderencia + repercussao + imagem - penalidade, 3)


def selecionar(pool: list[Candidato], cfg: Config, agora: datetime | None = None) -> dict[str, list[Candidato]]:
    """Devolve {editoria: [principal(is) + reservas]} sem repetir URL entre editorias."""
    agora = agora or datetime.now(timezone.utc)
    calcular_cobertura(pool)
    sel = cfg.geral["selecao"]
    quantos = sel["artigos_por_categoria"] + sel["reservas_por_categoria"]
    usados: set[str] = set()
    resultado: dict[str, list[Candidato]] = {}
    # editorias com menos candidatos escolhem primeiro, para não ficarem sem pauta
    ordem = sorted(cfg.categorias, key=lambda k: sum(k in c.categorias for c in pool))
    for cat in ordem:
        candidatos = []
        for c in pool:
            if cat in c.categorias and c.id not in usados:
                pontuado = Candidato.from_dict(c.to_dict())
                pontuado.score = pontuar(c, cat, cfg, agora)
                candidatos.append(pontuado)
        candidatos.sort(key=lambda c: c.score, reverse=True)
        escolhidos = candidatos[:quantos]
        usados.update(c.id for c in escolhidos[: sel["artigos_por_categoria"]])
        resultado[cat] = escolhidos
    return {k: resultado[k] for k in cfg.categorias if k in resultado}
