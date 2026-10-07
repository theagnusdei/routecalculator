# Uso no Google AI Studio (alternativa gratuita)

Há duas formas de usar o Gemini sem custo:

## A) Automática (recomendado como reserva): chave grátis + GitHub Actions
1. Crie uma chave em https://aistudio.google.com/apikey (nível gratuito, sem cartão).
2. No repositório: *Settings → Secrets and variables → Actions → New repository secret* →
   `GEMINI_API_KEY`.
3. Pronto: o workflow "Edição diária" usa o Gemini sempre que o Claude não estiver disponível
   (ordem definida em `config/config.yaml → redacao.backends`). Para usar só o Gemini, rode o
   workflow manualmente com `backend = gemini`, ou deixe `backends: [gemini]`.

## B) Manual no AI Studio (sem programação)
1. Abra https://aistudio.google.com → *Create prompt*.
2. Em **System instructions**, cole o conteúdo de `prompts/redator_sistema.md`
   (troque `{palavras_min}` por 500 e `{palavras_max}` por 900).
3. Ative **Grounding with Google Search** (gratuito, com limites) e **Structured output → JSON**.
4. Na mensagem do usuário, cole o modelo abaixo, preenchido com uma matéria de `edicoes/<data>/fontes/*.md`
   (ou peça para o próprio Gemini pesquisar, usando o segundo modelo).
5. Salve a resposta como `edicoes/<data>/artigos/<editoria>.json` e rode `python -m scitekvision montar`.

### Modelo 1 — a partir de uma fonte já coletada
```
Editoria: <Astrofísica>
Fonte original: <ESA> — <https://...>
Publicado em: <data>
Título original: <...>

<texto_fonte>
<cole aqui o texto extraído>
</texto_fonte>

Escreva o artigo seguindo rigorosamente as regras e devolva apenas o JSON.
```

### Modelo 2 — pesquisa feita pelo próprio Gemini (com Google Search)
```
Pesquise as notícias mais relevantes das últimas 24 horas na editoria <Robótica>, apenas em sites
oficiais (universidades, agências espaciais, institutos de pesquisa, empresas) e grandes portais de
acesso gratuito. Escolha a mais relevante (novidade real, impacto, repercussão em mais de um veículo),
informe a URL da fonte e de uma imagem com crédito, e então escreva o artigo seguindo as regras,
devolvendo apenas o JSON.
```
