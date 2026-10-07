"""Etapa 3 — leitura da matéria original e obtenção de imagem com crédito.

Texto: trafilatura (gratuito, local).  Imagem: og:image da página > imagem do feed >
Wikimedia Commons (licença livre, via API pública) como reserva.
"""
from __future__ import annotations

import io
import logging
from pathlib import Path
from urllib.parse import urlparse

import requests
import trafilatura
from PIL import Image

from .coletor import limpar_html
from .config import Config, slug
from .modelos import Candidato, Pauta
from .ranking import tokens

log = logging.getLogger(__name__)

# Dicas de licença por domínio — SEMPRE conferidas pelo revisor humano.
LICENCAS = {
    "nasa.gov": "Domínio público (NASA Media Usage Guidelines) — manter crédito NASA",
    "esa.int": "ESA — normalmente CC BY-SA 3.0 IGO; conferir na página da imagem",
    "eso.org": "ESO — CC BY 4.0; manter crédito ESO",
    "nih.gov": "Governo dos EUA — em geral domínio público; conferir",
    "noaa.gov": "Governo dos EUA — em geral domínio público; conferir",
    "wikimedia.org": "Wikimedia Commons — ver licença indicada",
    "fapesp.br": "Agência FAPESP — reprodução permitida com crédito (conferir condições)",
    "usp.br": "Jornal da USP — reprodução permitida com crédito (conferir condições)",
}
LICENCA_PADRAO = ("© do veículo/autor original — uso SOMENTE com autorização ou como referência; "
                  "considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)")


def dica_licenca(url: str) -> str:
    host = urlparse(url).netloc.lower()
    for dominio, texto in LICENCAS.items():
        if host == dominio or host.endswith("." + dominio):
            return texto
    return LICENCA_PADRAO


def baixar_html(url: str, cfg: Config) -> str | None:
    c = cfg.geral["coleta"]
    try:
        r = requests.get(url, timeout=c["timeout_segundos"], headers={"User-Agent": c["user_agent"]})
        r.raise_for_status()
        return r.text
    except requests.RequestException as e:
        log.warning("Falha ao abrir %s: %s", url, e)
        return None


def extrair_texto(html: str, url: str) -> tuple[str, dict]:
    texto = trafilatura.extract(html, url=url, include_comments=False, include_tables=False,
                                favor_precision=True) or ""
    meta = trafilatura.extract_metadata(html, default_url=url)
    info = {}
    if meta is not None:
        info = {"autor": meta.author, "site": meta.sitename, "imagem": meta.image, "titulo": meta.title}
    return texto.strip(), info


def salvar_imagem(url_img: str, destino: Path, cfg: Config) -> bool:
    c = cfg.geral["coleta"]
    try:
        r = requests.get(url_img, timeout=c["timeout_segundos"], headers={"User-Agent": c["user_agent"]})
        r.raise_for_status()
        img = Image.open(io.BytesIO(r.content))
        img.load()
    except Exception as e:  # requests, PIL.UnidentifiedImageError, etc.
        log.warning("Imagem inválida %s: %s", url_img, e)
        return False
    if img.width < 300:
        log.info("Imagem pequena demais (%spx): %s", img.width, url_img)
        return False
    largura = cfg.geral["imagens"]["largura_max_px"]
    if img.width > largura:
        img = img.resize((largura, round(img.height * largura / img.width)))
    destino.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(destino, "JPEG", quality=85)
    return True


def buscar_wikimedia(consulta: str, cfg: Config) -> dict | None:
    """Busca uma imagem de licença livre no Wikimedia Commons (API pública, gratuita)."""
    params = {
        "action": "query", "format": "json", "generator": "search", "gsrnamespace": 6,
        "gsrsearch": f"{consulta} filetype:bitmap", "gsrlimit": 5,
        "prop": "imageinfo", "iiprop": "url|extmetadata", "iiurlwidth": 1600,
    }
    try:
        r = requests.get("https://commons.wikimedia.org/w/api.php", params=params, timeout=20,
                         headers={"User-Agent": cfg.geral["coleta"]["user_agent"]})
        r.raise_for_status()
        paginas = (r.json().get("query") or {}).get("pages", {})
    except (requests.RequestException, ValueError) as e:
        log.warning("Wikimedia indisponível: %s", e)
        return None
    for p in sorted(paginas.values(), key=lambda p: p.get("index", 99)):
        info = (p.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata", {})
        if not info.get("thumburl"):
            continue
        autor = limpar_html(meta.get("Artist", {}).get("value", "")) or "autor desconhecido"
        licenca = meta.get("LicenseShortName", {}).get("value", "ver página")
        return {"url": info["thumburl"], "pagina": info.get("descriptionurl"),
                "credito": f"{autor} / Wikimedia Commons", "licenca": f"Wikimedia Commons — {licenca}"}
    return None


def preparar_pauta(categoria: str, candidatos: list[Candidato], pasta: Path, cfg: Config) -> Pauta | None:
    """Tenta o principal e, se falhar, as reservas, até obter texto suficiente.
    Devolve None se a editoria não tiver candidatos."""
    minimo = cfg.geral["selecao"]["min_caracteres_texto"]
    ultima = None
    for cand in candidatos:
        pauta = Pauta(categoria=categoria, candidato=cand)
        ultima = pauta
        html = baixar_html(cand.url, cfg)
        if not html:
            pauta.status, pauta.erro = "falhou", "página indisponível"
            continue
        texto, info = extrair_texto(html, cand.url)
        if len(texto) < minimo:
            pauta.status, pauta.erro = "falhou", f"texto extraído curto ({len(texto)} caracteres)"
            log.info("[%s] %s: %s — tentando reserva", categoria, cand.url, pauta.erro)
            continue
        limite = cfg.geral["redacao"]["max_caracteres_fonte"]
        if len(texto) > limite:
            pauta.alertas_automaticos.append(
                f"Texto-fonte longo ({len(texto)} caracteres): o redator recebeu só os primeiros {limite}.")
        pauta.texto_fonte = texto
        pauta.autor_fonte = info.get("autor")
        pauta.site_fonte = info.get("site") or cand.fonte
        obter_imagem(pauta, info.get("imagem"), pasta, cfg)
        pauta.status = "extraida"
        return pauta
    return ultima


def obter_imagem(pauta: Pauta, og_image: str | None, pasta: Path, cfg: Config) -> None:
    cand = pauta.candidato
    nome = f"imagens/{categoria_slug(pauta)}.jpg"
    destino = pasta / nome
    for url_img in (og_image, cand.imagem_feed):
        if url_img and salvar_imagem(url_img, destino, cfg):
            pauta.imagem_url, pauta.imagem_arquivo, pauta.imagem_pagina = url_img, nome, cand.url
            pauta.imagem_credito = f"{pauta.site_fonte or cand.fonte}"
            pauta.imagem_licenca = dica_licenca(cand.url)
            if pauta.imagem_licenca == LICENCA_PADRAO:
                pauta.alertas_automaticos.append(
                    "Imagem protegida por direitos autorais do veículo de origem: confirmar autorização "
                    "ou substituir por imagem livre antes de publicar.")
            return
    if cfg.geral["imagens"].get("usar_wikimedia_como_reserva"):
        consulta = " ".join(sorted(tokens(cand.titulo), key=len, reverse=True)[:3])
        achada = buscar_wikimedia(consulta, cfg)
        if achada and salvar_imagem(achada["url"], destino, cfg):
            pauta.imagem_url, pauta.imagem_arquivo = achada["url"], nome
            pauta.imagem_pagina, pauta.imagem_credito = achada["pagina"], achada["credito"]
            pauta.imagem_licenca = achada["licenca"]
            pauta.alertas_automaticos.append(
                "Imagem ilustrativa obtida no Wikimedia Commons (não é da matéria original): conferir pertinência.")
            return
    pauta.alertas_automaticos.append("Nenhuma imagem obtida automaticamente: inserir imagem manualmente.")


def categoria_slug(pauta: Pauta) -> str:
    return f"{pauta.categoria}-{slug(pauta.candidato.titulo, 40)}"
