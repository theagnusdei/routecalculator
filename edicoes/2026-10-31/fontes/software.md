# Remote code execution on Linux systems with multipath TCP

- Editoria: Software (`software`)
- Fonte: LWN.net — https://lwn.net/Articles/1104192/
- Autor: [Posted October
- Publicado: 2026-10-30T15:45:27+00:00
- Score: 5.529
- Imagem: nenhuma | crédito: None | licença: None

## Outras coberturas
- nenhuma

## Texto extraído

Remote code execution on Linux systems with multipath TCP
On October 27, LLM provider Anthropic reported on a remotely exploitable use-after-free bug affecting systems with multipath TCP listeners open. The bug works by triggering a response to a retransmitted SYN packet at the same moment that the TCP connection is established in another thread, causing the first thread to access the connection's options structure after the second thread has freed it. The first thread can then disclose kernel memory or cause a buffer overflow, writing an attacker-controlled payload. The fix was to only free the structure after an RCU grace period. On October 29, the Go security team advised that all programs written in Go use multipath TCP by default, so many systems may be unknowingly vulnerable. And, of course, there is always the possibility of related bugs in other sections of the TCP stack. Users may be wise to update to a patched kernel as soon as one becomes available for their distribution.
