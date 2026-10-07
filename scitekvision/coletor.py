"""Etapa 1 — coleta de notícias via RSS/Atom (gratuito, sem chave de API).

Cada execução acrescenta itens novos ao "pool" de candidatos da edição
(dados/candidatos/AAAA-MM-DD.json), permitindo várias coletas durante a noite.
"""
from __future__ import annotations

import html
import json
import logging
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone

import feedparser
import requests

from .config import Config, id_url
from .modelos import Candidato

log = logging.getLogger(__name__)

_TAG = re.compile(r"<[^>]+>")


def limpar_html(texto: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(_TAG.sub(" ", texto or ""))).strip()


def baixar_feed(url: str, cfg: Config) -> feedparser.FeedParserDict | None:
    c = cfg.geral["coleta"]
    try:
        r = requests.get(url, timeout=c["timeout_segundos"], headers={"User-Agent": c["user_agent"]})
        r.raise_for_status()
    except requests.RequestException as e:
        log.warning("Feed indisponível %s: %s", url, e)
        return None
    feed = feedparser.parse(r.content)
    if feed.bozo and not feed.entries:
        log.warning("Feed inválido %s: %s", url, feed.get("bozo_exception"))
        return None
    return feed


def _data_entrada(e) -> datetime | None:
    for chave in ("published_parsed", "updated_parsed", "created_parsed"):
        st = e.get(chave)
        if st:
            return datetime(*st[:6], tzinfo=timezone.utc)
    return None


def _imagem_entrada(e) -> str | None:
    for chave in ("media_content", "media_thumbnail"):
        for m in e.get(chave) or []:
            if m.get("url"):
                return m["url"]
    for link in e.get("links", []):
        if link.get("rel") == "enclosure" and str(link.get("type", "")).startswith("image"):
            return link.get("href")
    m = re.search(r'<img[^>]+src="([^"]+)"', e.get("summary", "") or "")
    return m.group(1) if m else None


def classificar(texto: str, cfg: Config) -> list[str]:
    """Editorias cujas palavras-chave aparecem no texto (para portais gerais)."""
    t = f" {texto.lower()} "
    achadas = []
    for chave, cat in cfg.categorias.items():
        for kw in cat.get("palavras_chave", []):
            k = kw.lower()
            # palavra inteira para siglas curtas (AI, PC, IA...), substring para termos longos
            if (len(k) <= 3 and re.search(rf"\b{re.escape(k)}\b", t)) or (len(k) > 3 and k in t):
                achadas.append(chave)
                break
    return achadas


def entradas_do_feed(feed, fonte: str, peso: float, categorias: list[str] | None,
                     cfg: Config, desde: datetime) -> list[Candidato]:
    agora = datetime.now(timezone.utc).isoformat()
    itens = []
    for e in feed.entries[: cfg.geral["coleta"]["max_itens_por_feed"]]:
        url = e.get("link")
        titulo = limpar_html(e.get("title", ""))
        if not url or not titulo:
            continue
        publicado = _data_entrada(e)
        if publicado and publicado < desde:
            continue
        resumo = limpar_html(e.get("summary", ""))[:1200]
        cats = categorias or classificar(f"{titulo} {resumo}", cfg)
        if not cats:
            continue
        itens.append(Candidato(
            id=id_url(url), titulo=titulo, url=url, resumo=resumo, fonte=fonte, peso_fonte=float(peso),
            categorias=list(cats), publicado=publicado.isoformat() if publicado else None,
            coletado_em=agora, imagem_feed=_imagem_entrada(e),
        ))
    return itens


def tarefas_de_coleta(cfg: Config) -> list[tuple[str, str, float, list[str] | None]]:
    tarefas = []
    for chave, cat in cfg.categorias.items():
        for f in cat.get("feeds", []):
            tarefas.append((f["url"], f["fonte"], f.get("peso", 0.7), [chave]))
    for f in cfg.portais_gerais:
        tarefas.append((f["url"], f["fonte"], f.get("peso", 0.6), None))
    return tarefas


def coletar(cfg: Config) -> list[Candidato]:
    desde = datetime.now(timezone.utc) - timedelta(hours=cfg.geral["coleta"]["janela_horas"])
    feeds_cache: dict[str, object] = {}
    tarefas = tarefas_de_coleta(cfg)
    with ThreadPoolExecutor(max_workers=8) as ex:
        urls = sorted({t[0] for t in tarefas})
        for url, feed in zip(urls, ex.map(lambda u: baixar_feed(u, cfg), urls)):
            feeds_cache[url] = feed
    itens: list[Candidato] = []
    for url, fonte, peso, cats in tarefas:
        feed = feeds_cache.get(url)
        if feed is not None:
            itens.extend(entradas_do_feed(feed, fonte, peso, cats, cfg, desde))
    log.info("Coletados %d itens de %d feeds", len(itens), len(feeds_cache))
    return itens


def mesclar(existentes: list[Candidato], novos: list[Candidato]) -> list[Candidato]:
    """Une pools sem duplicar URLs; um mesmo link pode ganhar editorias novas."""
    por_id = {c.id: c for c in existentes}
    for n in novos:
        if n.id in por_id:
            atual = por_id[n.id]
            atual.categorias = sorted(set(atual.categorias) | set(n.categorias))
            atual.peso_fonte = max(atual.peso_fonte, n.peso_fonte)
            atual.imagem_feed = atual.imagem_feed or n.imagem_feed
        else:
            por_id[n.id] = n
    return list(por_id.values())


def carregar_pool(cfg: Config, edicao: date) -> list[Candidato]:
    arq = cfg.arquivo_candidatos(edicao)
    if not arq.exists():
        return []
    return [Candidato.from_dict(d) for d in json.loads(arq.read_text(encoding="utf-8"))]


def salvar_pool(cfg: Config, edicao: date, pool: list[Candidato]) -> None:
    arq = cfg.arquivo_candidatos(edicao)
    arq.parent.mkdir(parents=True, exist_ok=True)
    pool = sorted(pool, key=lambda c: c.id)
    arq.write_text(json.dumps([c.to_dict() for c in pool], ensure_ascii=False, indent=1), encoding="utf-8")


def executar(cfg: Config, edicao: date) -> list[Candidato]:
    pool = mesclar(carregar_pool(cfg, edicao), coletar(cfg))
    salvar_pool(cfg, edicao, pool)
    log.info("Pool da edição %s: %d candidatos", edicao, len(pool))
    return pool


def verificar_feeds(cfg: Config) -> list[tuple[str, str, int | str]]:
    """Diagnóstico: devolve (fonte, url, nº de itens ou erro) para cada feed configurado."""
    resultado = []
    for url, fonte, _peso, _cats in tarefas_de_coleta(cfg):
        feed = baixar_feed(url, cfg)
        resultado.append((fonte, url, len(feed.entries) if feed is not None else "FALHOU"))
    return resultado
