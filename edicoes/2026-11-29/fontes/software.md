# Google Enhances its Open-Source MaxText Training Framework for Long-Context Training

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/11/google-long-context-training/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Sergio De Simone
- Publicado: 2026-11-28T16:00:00+00:00
- Score: 5.528
- Imagem: imagens/software-google-enhances-its-open-source-maxtext.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

To address the computational, memory, and communication bottlenecks of long-context training, Google has integrated four context-parallelism strategies into MaxText, its open-source JAX training framework, enabling LLM training with context lengths up to 14 million tokens on Cloud TPUs.
Google engineers highlight the growing trend towards larger context windows, noting that they enable applications such as processing entire code repositories or ingesting hours of video:
In three years, context windows have grown from 128K-200K tokens to 1M-2M, and models trained toward 10M tokens are arriving. Training at those lengths, not just serving them, is where the system limits show up.
Training large language models at such sequence lengths introduces two major bottlenecks: the quadratic growth of attention and the linear growth of activations and key-value (KV) caches. To address these challenges, Google uses context parallelism, which distributes sequences across multiple chips and streams keys and values between them, rather than materializing the entire sequence on every chip.
Google has implemented four context-parallelism strategies in MaxText are: All-Gather, All-to-All (Ulysses), P2P (Ring Attention), and A2A + P2P (USP). They differ in their high-bandwidth memory (HBM) requirements, their ability to overlap communication with computation, and their scalability beyond the number of KV heads.
P2P (Ring Attention) is the primary workhorse for very long-context training, whereas All-Gather is the standard baseline for most other cases where the KV can fit. These are the primary CP strategies to use in practice.
Using these new strategies, Google reported significant results with Llama 3.1 8b and its Cloud TPU infrastructure. These include achieving 70% Model FLOPs Utilization (MFU) for sequence lengths up to 4 million tokens on TPU 5p, supporting context lengths of up to 14 million tokens on both TPU 5p and TPU 7, and maintaining approximately 50% MFU for sequence lengths below 6 million tokens. Additionally, P2P achieved 48.7% MFU on TPU 7, compared with 37.1% on TPU 5p.
Google identified two areas of future development. The first is adding support for more architectures, including those combining sliding-window and global attention layers, as well as linear attention mechanisms such as Gated Delta Net (GDN) and Kimi Delta Attention (KDA). The second is improving performance through further optimization of Tokamax kernels, enhancements to the P2P backward pass, and the development of "recipes by model and context length" for distinct TPU architectures.
Commenting on the announcement, Google director Nathan Beach observed that:
If you are training models on Google TPUs with multi-million-token context, attention memory -- not compute -- is usually the first wall you hit.
MaxText 0.2.4 is available through PyPi, DockerHub, and GitHub.
