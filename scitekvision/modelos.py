"""Estruturas de dados trocadas entre as etapas do pipeline (serializadas em JSON)."""
from __future__ import annotations

from dataclasses import asdict, dataclass, field


@dataclass
class Candidato:
    id: str
    titulo: str
    url: str
    resumo: str
    fonte: str
    peso_fonte: float
    categorias: list[str]
    publicado: str | None          # ISO 8601 (UTC)
    coletado_em: str
    imagem_feed: str | None = None
    score: float = 0.0
    cobertura: list[str] = field(default_factory=list)  # URLs de outras fontes com a mesma pauta

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "Candidato":
        campos = cls.__dataclass_fields__
        return cls(**{k: v for k, v in d.items() if k in campos})


@dataclass
class Pauta:
    """Matéria selecionada para uma editoria, já com o texto extraído e a imagem."""
    categoria: str
    candidato: Candidato
    texto_fonte: str = ""
    autor_fonte: str | None = None
    site_fonte: str | None = None
    imagem_url: str | None = None
    imagem_arquivo: str | None = None   # caminho relativo à pasta da edição
    imagem_credito: str | None = None
    imagem_licenca: str | None = None
    imagem_pagina: str | None = None    # página de origem da imagem
    status: str = "pendente"            # pendente | extraida | redigida | falhou | fora_do_prazo
    erro: str | None = None
    artigo: dict | None = None
    backend: str | None = None
    alertas_automaticos: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        d = asdict(self)
        d["candidato"] = self.candidato.to_dict()
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Pauta":
        d = dict(d)
        d["candidato"] = Candidato.from_dict(d["candidato"])
        campos = cls.__dataclass_fields__
        return cls(**{k: v for k, v in d.items() if k in campos})
