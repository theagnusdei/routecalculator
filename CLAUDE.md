# SciTekVision — instruções para o Claude Code

Este repositório é um agente editorial: coleta notícias de ciência e tecnologia (RSS gratuitos),
seleciona por relevância, extrai texto e imagem, redige artigos originais em pt-BR e entrega `.docx`
para revisão humana via Pull Request.

## Comandos
- `pip install -r requirements.txt` — dependências (todas gratuitas)
- `python -m scitekvision info` — data da edição e prazos
- `python -m scitekvision preparar` — coleta + seleção + extração (gera `edicoes/<data>/fontes/*.md`)
- `python -m scitekvision redigir` — redige com o backend configurado (claude-cli / gemini)
- `python -m scitekvision montar` — gera os `.docx` e o `LEIA-ME-REVISAO.md`
- `python -m scitekvision edicao` — tudo de uma vez
- `python -m scitekvision verificar-feeds` — testa todos os RSS
- `python -m pytest -q` — testes offline

## Regras editoriais
- Formato e regras do artigo: `prompts/redator_sistema.md` (JSON). Artigos escritos à mão pelo Claude
  ficam em `edicoes/<data>/artigos/<editoria>.json` e são incorporados pelo `montar`.
- Nunca invente fatos; nunca copie trechos da fonte; sempre atribua a fonte e o crédito da imagem.
- Só fontes gratuitas (sem paywall, sem APIs pagas).
- Prazo: parar de redigir às 10:00 (America/Sao_Paulo); entregar até 10:30.
- Nunca faça merge do PR da edição — o merge é a aprovação humana.

## Estrutura
- `config/categorias.yaml` — editorias, feeds e pesos das fontes
- `config/config.yaml` — prazos, seleção, backends de IA
- `scitekvision/` — coletor → ranking → extrator → redator → docx_builder (orquestrados em `pipeline.py`)
- `dados/candidatos/<data>.json` — pool acumulado pelas coletas noturnas
- `edicoes/<data>/` — selecao.json, pautas.json, fontes/, artigos/, imagens/, docx/, volume completo
