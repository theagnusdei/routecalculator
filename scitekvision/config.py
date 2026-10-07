"""Carregamento de configuração e utilidades de caminho/tempo."""
from __future__ import annotations

import hashlib
import re
import unicodedata
from dataclasses import dataclass
from datetime import date, datetime, time, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

import yaml

RAIZ = Path(__file__).resolve().parent.parent


@dataclass
class Config:
    geral: dict
    categorias: dict
    portais_gerais: list
    termos_penalizados: list
    raiz: Path

    @property
    def tz(self) -> ZoneInfo:
        return ZoneInfo(self.geral.get("fuso_horario", "America/Sao_Paulo"))

    def agora(self) -> datetime:
        return datetime.now(self.tz)

    def horario(self, chave: str) -> time:
        h, m = self.geral["prazos"][chave].split(":")
        return time(int(h), int(m))

    def prazo(self, chave: str, edicao: date) -> datetime:
        return datetime.combine(edicao, self.horario(chave), tzinfo=self.tz)

    def edicao_atual(self, agora: datetime | None = None) -> date:
        """A edição do dia D reúne o que foi coletado até o prazo de redação de D.
        Coletas depois do prazo já alimentam a edição do dia seguinte."""
        agora = agora or self.agora()
        if agora.timetz().replace(tzinfo=None) >= self.horario("redacao"):
            return agora.date() + timedelta(days=1)
        return agora.date()

    def pasta_edicao(self, edicao: date) -> Path:
        return self.raiz / self.geral["saida"]["pasta_edicoes"] / edicao.isoformat()

    def arquivo_candidatos(self, edicao: date) -> Path:
        return self.raiz / self.geral["saida"]["pasta_candidatos"] / f"{edicao.isoformat()}.json"

    def ler_prompt(self, nome: str) -> str:
        return (self.raiz / "prompts" / nome).read_text(encoding="utf-8")


def carregar(raiz: Path | None = None) -> Config:
    raiz = raiz or RAIZ
    geral = yaml.safe_load((raiz / "config" / "config.yaml").read_text(encoding="utf-8"))
    cats = yaml.safe_load((raiz / "config" / "categorias.yaml").read_text(encoding="utf-8"))
    return Config(
        geral=geral,
        categorias=cats["categorias"],
        portais_gerais=cats.get("portais_gerais", []),
        termos_penalizados=cats.get("termos_penalizados", []),
        raiz=raiz,
    )


def slug(texto: str, limite: int = 60) -> str:
    texto = unicodedata.normalize("NFKD", texto).encode("ascii", "ignore").decode()
    texto = re.sub(r"[^a-zA-Z0-9]+", "-", texto).strip("-").lower()
    return texto[:limite].rstrip("-") or "artigo"


def id_url(url: str) -> str:
    return hashlib.sha1(url.strip().encode()).hexdigest()[:12]
