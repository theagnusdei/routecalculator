# Cloudflare Open Sources Decision Models for AI Agents

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/clef-decision-models/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Renato Losio
- Publicado: 2026-10-08T06:54:00+00:00
- Score: 6.349
- Imagem: imagens/software-cloudflare-open-sources-decision-models.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- https://huggingface.co/blog/LiquidAI/open-d1

## Texto extraído

During its recent "Birthday Week", Cloudflare announced Clef, a set of open-weight AI models designed to choose between predefined options rather than generate text. Cloudflare released 9B- and 27B-parameter models, along with a platform for adapting them to specific decision-making tasks.
Clef is a 27B multimodal model that takes a state and a schema of typed questions as input and returns decisions. It can process text, JSON, images, or video, and returns a probability for each allowed option for every question in a single forward pass, without generating free-form text or requiring output parsing.
Source: Cloudflare blog
A decision model classifies inputs and returns typed outcomes with probabilities, allowing AI agents to use these results to determine how to act, such as routing a support request, escalating it, or deferring the decision to a human. Cloudflare’s API is compatible with the popular Typesafe AI’s Jev System One model.
Source: Cloudflare blog
Michelle Chen, group product manager at Cloudflare, Alex Reneau, principal machine learning engineer at Cloudflare, and Kevin Flansburg, senior engineering manager at Cloudflare, write:
Because they are hosted on Cloudflare’s infrastructure, we’re able to take advantage of our GPUs at the edge, leading to low network latency and faster decisions. This means that you could put Clef into the hot path for agents to make decisions and combine that with one of our LLMs on Workers AI to take action.
The hyperscaler also released Clef-Flash, a smaller 9B multimodal model designed for latency-sensitive decisions. It has a median latency of 38.8 ms in Cloudflare’s benchmarks, compared with 209.3 ms for the 27B Clef model. Chen, Reneau, and Flansburg explain how Clef differs from other decision models:
First, it has a vision encoder so it’s able to take in images and classify visual content. This is different from Jev, which only does text classification today. Secondly, our model has a 64k context window (compared to Jev’s 32k), which allows users to squeeze more input state for the model to classify against.
On a popular Hacker News thread, the community discusses decision models, latency, open weights, and whether this is really a new model category. Jacek Złydach writes:
It's not a ‘new paradigm’, it's a low-hanging fruit that's been lying around for years; Typesafe were the first to bother to stop and pick it up, and market the shit out of it.
The benchmark results raised further questions, with user SebastianSosa warning:
Public benchmarks are easy to cheat, if I am Typesafe, I would also release a public benchmark to distract otherwise competent people from overfitting to a benchmark instead of making something actually useful.
Cloudflare plans to fine-tune Clef for specific use cases, such as support triage and bot classification, using its historical labelled data to improve accuracy and speed. On Reddit, user bugra_sa writes:
I'd care more about whether Clef knows when to punt than its raw accuracy score. Test it on cases where a false positive is much more expensive than a miss, then change the data enough to see when its confidence falls apart. If it stays confident through that, the benchmark number doesn't mean much.
Cloudflare also announced a fine-tuning service that lets customers adapt Clef to their own workloads using their data, initially with support from Cloudflare engineers, with a self-service platform planned for a later release. No firm date has been announced.
The company has made the Clef models available through Workers AI and as downloadable weights on Hugging Face, inviting developers to experiment with them and provide feedback.
