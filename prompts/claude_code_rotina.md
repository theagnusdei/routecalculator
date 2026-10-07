# Prompt da Rotina do Claude Code (modo recomendado — Anthropic)

> Cole o texto abaixo (entre as linhas `---`) como prompt de uma **Rotina** (Routine) do
> Claude Code na web (claude.ai/code), apontada para o repositório `scitekvision`.
> Agendamento sugerido: `CRON_TZ=America/Sao_Paulo 0 6 * * *` (todo dia às 06:00 de Brasília).
> Ou rode manualmente no terminal: `claude -p "$(sed -n '/^---$/,/^---$/p' prompts/claude_code_rotina.md)"`.

---
Você é o agente editorial da SciTekVision. Produza a edição de hoje com rascunhos de artigos originais
em português sobre ciência e tecnologia, para revisão humana. Siga o CLAUDE.md do repositório.

Horário de referência: America/Sao_Paulo. Prazo de redação: 10:00. Prazo de entrega dos .docx: 10:30.
Verifique a hora com `TZ=America/Sao_Paulo date` antes de cada artigo; às 10:00 pare de redigir e vá
direto para a montagem e entrega.

1. Preparação
   - `pip install -r requirements.txt`
   - `python -m scitekvision info` (anote a data da edição, AAAA-MM-DD)
   - `python -m scitekvision preparar` — coleta final via RSS, ranqueia por relevância e extrai texto e
     imagem da melhor matéria de cada editoria (medicina, biologia, robótica, software, hardware,
     astrofísica, engenharia/computação quântica, computadores pessoais, inteligência artificial e,
     se houver material, energia/materiais e cibersegurança).

2. Curadoria (sua avaliação editorial)
   - Leia `edicoes/<data>/selecao.json` e `edicoes/<data>/fontes/*.md`.
   - Se a matéria escolhida para uma editoria for fraca (promocional, opinião rasa, repetida, sem
     novidade real), escolha um candidato melhor da mesma editoria em `selecao.json`; leia-o com WebFetch.
     Se quiser complementar, use WebSearch apenas em sites oficiais e grandes portais gratuitos
     (NASA, ESA, ESO, NIH, OMS, Fiocruz, FAPESP, MIT News, Nature, Science, IEEE Spectrum, Ars Technica…).
     Nunca use conteúdo atrás de paywall.
   - Garanta pelo menos 1 artigo por editoria obrigatória, sem repetir a mesma notícia entre editorias.

3. Redação — para cada editoria, escreva `edicoes/<data>/artigos/<editoria>.json`
   (a chave da editoria é o nome do arquivo em `fontes/`, ex.: `astrofisica.json`)
   seguindo EXATAMENTE as regras e o formato JSON de `prompts/redator_sistema.md`
   (500–900 palavras, texto original, nada de fatos inventados, alertas para o revisor).
   Se trocou a matéria no passo 2, ajuste também `pautas.json` (url, título, fonte) dessa editoria
   e, se possível, baixe uma imagem com crédito para `edicoes/<data>/imagens/`.

4. Montagem e entrega
   - `python -m scitekvision montar` — gera `edicoes/<data>/docx/*.docx`, o volume
     `SciTekVision-<data>-edicao-completa.docx` e `LEIA-ME-REVISAO.md`.
   - Abra o `LEIA-ME-REVISAO.md` e confira se todas as editorias estão "redigida".
   - Crie o ramo `edicao/<data>`, faça commit de `dados/candidatos` e `edicoes/<data>`, faça push e
     abra um Pull Request para o ramo principal com o título "Edição <data> — rascunhos para revisão"
     e o conteúdo do `LEIA-ME-REVISAO.md` como descrição. Não faça merge: o merge é a aprovação humana.

5. Termine com um resumo curto: artigos entregues, pendências e alertas importantes para o revisor.
---
