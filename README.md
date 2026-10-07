# SciTekVision — agente de IA para notícias de ciência e tecnologia

Agente que, toda madrugada, **pesquisa notícias** em sites oficiais e grandes portais, **seleciona por
relevância** pelo menos 1 matéria por editoria, **obtém uma imagem com crédito**, **escreve um artigo
original** em português e **entrega `.docx` até as 10:30** num Pull Request para **revisão e aprovação
humana** antes da publicação no site.

Editorias: Medicina · Biologia · Robótica · Software · Hardware · Astrofísica · Engenharia/Computação
Quântica · Computadores Pessoais · Inteligência Artificial · (correlatas, se houver material) Energia e
Novos Materiais · Cibersegurança.

**Custo: R$ 0 além do que você já tem.** Nada de sites ou APIs pagas: só RSS públicos, extração local,
Wikimedia Commons, GitHub Actions (grátis) e IA via sua assinatura Claude (Claude Code) ou o nível
gratuito do Google AI Studio (Gemini).

---

## Como funciona

```
 22:00  01:00  04:00 (BRT)         06:13                         até 10:00        até 10:30
 ──●──────●──────●───────────────────●──────────────────────────────────●─────────────────●──
  coleta RSS (acumula pool)     coleta final → ranking → extração → redação IA → .docx → Pull Request
```

| Etapa | Módulo | O que faz | Custo |
|---|---|---|---|
| 1. Coleta | `coletor.py` | Lê ~60 feeds RSS/Atom (NASA, ESA, ESO, NIH, OMS, Fiocruz, FAPESP, MIT, Nature, IEEE Spectrum, Ars Technica…) e classifica portais gerais por palavras-chave | grátis |
| 2. Relevância | `ranking.py` | Pontua: autoridade da fonte + recência + aderência à editoria + **repercussão** (mesma pauta em várias fontes) + imagem − penalidades (promoções, patrocinados) | grátis |
| 3. Extração | `extrator.py` | Lê a matéria (trafilatura), pega a imagem (og:image → feed → Wikimedia Commons) e registra crédito e licença; troca pela reserva se a página falhar | grátis |
| 4. Redação | `redator.py` | IA escreve artigo original em JSON; valida tamanho e **detecta cópia** (trechos idênticos à fonte) | assinatura Claude ou Gemini grátis |
| 5. Entrega | `docx_builder.py` | Um `.docx` por artigo + volume completo da edição, com faixa "RASCUNHO", imagem e crédito, fontes, alertas e checklist do revisor | grátis |
| 6. Revisão | GitHub PR | PR `edicao/AAAA-MM-DD`; o **merge = aprovado para publicação** | grátis |

**Prazos garantidos pelo código:** depois das 10:00 nenhum artigo novo é redigido (as editorias que
faltarem saem como "PENDENTE" com a pauta sugerida) e a montagem/entrega acontece logo em seguida.
O estado é salvo a cada artigo — se algo cair, nada do que já foi escrito se perde.

---

## Instalação (passo a passo)

### 1. Criar o repositório `scitekvision`
Em https://github.com/new crie `scitekvision` (pode ser **privado**: o plano grátis inclui 2.000
minutos/mês de Actions; **público** é ilimitado). Depois envie este projeto:

```bash
git clone https://github.com/theagnusdei/routecalculator.git scitekvision
cd scitekvision
git checkout claude/scitekvision-news-agent-cyg47f
git remote set-url origin https://github.com/<seu-usuario>/scitekvision.git
git push -u origin HEAD:main
```

### 2. Permitir que o robô abra Pull Requests
*Settings → Actions → General → Workflow permissions* → marque **Read and write permissions** e
**Allow GitHub Actions to create and approve pull requests**.

### 3. Escolher o "cérebro" (pode configurar os dois; o segundo é reserva)

**Opção A — Claude (preferencial, usa sua assinatura Pro/Max, sem custo por uso)**
```bash
npm install -g @anthropic-ai/claude-code
claude setup-token          # gera um token de longa duração ligado à sua assinatura
```
Salve o token como secret `CLAUDE_CODE_OAUTH_TOKEN` (*Settings → Secrets and variables → Actions*).

**Opção B — Gemini (Google AI Studio, nível gratuito)**
Crie a chave em https://aistudio.google.com/apikey e salve como secret `GEMINI_API_KEY`.
Veja `prompts/google_ai_studio.md`.

> `ANTHROPIC_API_KEY` (API paga por uso) também é suportada, mas **não é necessária**.

### 4. Pronto
Os workflows `Coleta noturna` e `Edição diária` passam a rodar sozinhos. Para testar já:
*Actions → Edição diária → Run workflow*.

---

## Modo alternativo: Rotina do Claude Code (100% Anthropic, sem GitHub Actions)

Em vez do pipeline em Actions, o próprio Claude Code pode fazer o trabalho com **curadoria editorial
real** (lê as candidatas, troca matérias fracas, pesquisa na web em fontes oficiais e escreve):

1. Em https://claude.ai/code, conecte o repositório `scitekvision`.
2. Crie uma **Rotina** (Routine) com agendamento `CRON_TZ=America/Sao_Paulo 0 6 * * *`.
3. Use como prompt o texto de [`prompts/claude_code_rotina.md`](prompts/claude_code_rotina.md).
4. O ambiente da rotina precisa de **acesso à internet** (política de rede que permita os sites de
   notícias), senão a coleta falha.

O resultado é o mesmo: PR `edicao/AAAA-MM-DD` com os `.docx`. Se usar este modo, desative o workflow
"Edição diária" (mantenha a "Coleta noturna", que enriquece o pool).

---

## Uso local

```bash
pip install -r requirements.txt
python -m scitekvision info              # edição e prazos
python -m scitekvision verificar-feeds   # testa os RSS
python -m scitekvision edicao --backend claude-cli    # ou gemini, mock
python -m pytest -q                      # testes offline
```

Saída em `edicoes/AAAA-MM-DD/`:
```
LEIA-ME-REVISAO.md                      resumo para o revisor
SciTekVision-AAAA-MM-DD-edicao-completa.docx
docx/01-medicina-....docx  …            um arquivo por artigo
imagens/  fontes/  artigos/  selecao.json  pautas.json
```

## Personalização
- **Fontes e pesos:** `config/categorias.yaml` (adicione qualquer RSS gratuito; nova editoria = novo bloco).
- **Prazos, quantidade de artigos, tamanho, modelos de IA:** `config/config.yaml`.
- **Estilo editorial:** `prompts/redator_sistema.md`.

---

## Direitos autorais e ética (importante)
- O texto é **original** (o redator é instruído a não copiar e o sistema mede a sobreposição com a fonte).
- **Imagens de portais são protegidas.** O agente registra crédito, página de origem e uma dica de
  licença; quando a imagem não é livre, o `.docx` traz um alerta para o revisor **obter autorização ou
  trocar** por imagem livre (NASA e governo dos EUA: domínio público; ESO: CC BY 4.0; ESA: em geral
  CC BY-SA 3.0 IGO; Wikimedia Commons: conforme o arquivo).
- Todo artigo sai como **RASCUNHO** e exige aprovação humana (merge do PR).
- O robô respeita os sites: poucas requisições, identificação por User-Agent, apenas conteúdo aberto.

---

## Melhorias técnicas sugeridas (todas gratuitas ou freemium)
1. **Publicação automática após aprovação:** um workflow disparado pelo merge que converte os `.docx`
   aprovados para Markdown/HTML (Pandoc) e publica via API do WordPress, Ghost, ou em site estático
   (GitHub Pages / Cloudflare Pages / Netlify — todos com plano grátis).
2. **Aviso no celular quando a edição sair:** notificações do GitHub, ou Telegram Bot/Discord webhook
   (grátis) no fim do workflow.
3. **Revisão no Google Docs:** enviar os `.docx` para uma pasta do Google Drive (API gratuita) para o
   revisor editar no navegador, com comentários.
4. **Segunda opinião automática:** um passo de "checagem de fatos" em que outro modelo compara o artigo
   com a fonte e lista divergências antes do revisor humano.
5. **Memória editorial:** evitar repetir assuntos dos últimos 7 dias comparando com edições anteriores.
6. **Mais fontes oficiais:** arXiv (preprints, grátis), PubMed/Europe PMC (APIs grátis), NewsAPI ou
   GNews (planos freemium) para ampliar a cobertura.
7. **Imagens próprias:** gerar ilustrações livres de direitos com modelos de imagem de nível gratuito,
   sempre identificadas como "ilustração gerada por IA".
8. **Painel de métricas:** histórico de fontes mais aproveitadas e taxa de aprovação por editoria
   (GitHub Pages + JSON das edições).
