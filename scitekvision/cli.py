"""Linha de comando: python -m scitekvision <comando> [opções]."""
from __future__ import annotations

import argparse
import logging
import sys
from datetime import date

from . import coletor, pipeline
from .config import carregar


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="scitekvision", description="Agente editorial SciTekVision")
    ap.add_argument("comando", choices=["coletar", "selecionar", "extrair", "preparar", "redigir", "montar",
                                        "edicao", "verificar-feeds", "info"])
    ap.add_argument("--edicao", help="data da edição (AAAA-MM-DD); padrão: próxima edição pelo prazo")
    ap.add_argument("--backend", help="força um backend de redação (claude-cli, gemini, anthropic, mock)")
    ap.add_argument("--sem-coleta", action="store_true", help="no comando 'edicao', usa só o pool já coletado")
    ap.add_argument("--ignorar-prazo", action="store_true", help="redige mesmo depois do prazo (testes)")
    ap.add_argument("-v", "--verbose", action="store_true")
    a = ap.parse_args(argv)

    logging.basicConfig(level=logging.DEBUG if a.verbose else logging.INFO,
                        format="%(asctime)s %(levelname)s %(name)s: %(message)s")
    cfg = carregar()
    if a.backend:
        cfg.geral["redacao"]["backends"] = [b.strip() for b in a.backend.split(",")]
    edicao = date.fromisoformat(a.edicao) if a.edicao else cfg.edicao_atual()

    if a.comando == "info":
        print(f"Edição: {edicao} | prazo de redação: {cfg.prazo('redacao', edicao):%d/%m %H:%M} | "
              f"entrega: {cfg.prazo('entrega', edicao):%d/%m %H:%M} | pasta: {cfg.pasta_edicao(edicao)}")
    elif a.comando == "coletar":
        coletor.executar(cfg, edicao)
    elif a.comando == "selecionar":
        pipeline.selecionar(cfg, edicao)
    elif a.comando == "extrair":
        pipeline.extrair(cfg, edicao)
    elif a.comando == "preparar":  # coleta final + seleção + extração (modo Claude Code)
        coletor.executar(cfg, edicao)
        pipeline.selecionar(cfg, edicao)
        pautas = pipeline.extrair(cfg, edicao)
        for p in pautas:
            print(f"{p.categoria:25} {p.status:10} {p.candidato.titulo[:80]}")
    elif a.comando == "redigir":
        pipeline.redigir(cfg, edicao, ignorar_prazo=a.ignorar_prazo)
    elif a.comando == "montar":
        for arq in pipeline.montar(cfg, edicao):
            print(arq)
    elif a.comando == "edicao":
        for arq in pipeline.edicao_completa(cfg, edicao, coletar=not a.sem_coleta, ignorar_prazo=a.ignorar_prazo):
            print(arq)
    elif a.comando == "verificar-feeds":
        falhas = 0
        for fonte, url, n in coletor.verificar_feeds(cfg):
            falhas += n == "FALHOU"
            print(f"{str(n):>7}  {fonte:28} {url}")
        print(f"\n{falhas} feed(s) com falha.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
