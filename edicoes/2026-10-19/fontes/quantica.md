# Quantum magic state cleanup cuts errors 40-fold in first successful hardware test

- Editoria: Engenharia e Computação Quântica (`quantica`)
- Fonte: Phys.org — https://phys.org/news/2026-10-quantum-magic-state-cleanup-errors.html
- Autor: Paul Arnold
- Publicado: 2026-10-17T18:00:02+00:00
- Score: 5.205
- Imagem: imagens/quantica-quantum-magic-state-cleanup-cuts-errors.jpg | crédito: Phys.org | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Quantum magic state cleanup cuts errors 40-fold in first successful hardware test
Paul Arnold
Author
Qubits, the quantum equivalent of digital bits, are fragile and prone to errors. That makes building reliable quantum computers extremely difficult. One fix has been to use traditional magic state distillation, which filters out flaws, but it is extremely resource-intensive.
Another potential solution is magic state cultivation, which cleans up a noisy magic state (a specially prepared quantum state that is needed for advanced calculations) directly inside a protected qubit. But this approach has never been tested successfully on real hardware.
However, in a first for quantum computing, Google Quantum AI researchers have demonstrated magic state cultivation on Willow, a superconducting processor, and it has cut errors dramatically.
Cleaning up noisy quantum states
The team first needed some errors to fix.
So, in their experiment, they encoded a noisy magic state across several physical qubits, spreading the quantum information over a small grid of qubits to protect it against errors.
Then, they tried to weed out the errors in the noisy state using helper qubits to scan the information for mistakes without destroying the delicate data itself.
If the checks caught any flaws, the system threw that attempt away and started over. If an attempt passed every test, the refined magic state was kept for further processing.
A dramatic drop in errors
The results, which are published in the journal Science, were striking. "Cultivation reduces the error by a factor of 40," the scientists wrote. And that yielded refined magic states with a fidelity of at least approximately 99.99% (a measure of how closely the prepared quantum state matches the intended state).
Checking such tiny levels of error required a new approach, so the scientists developed a checking method called kickback tomography. It is capable of detecting remaining errors using far fewer measurements than traditional techniques.
And the filtering was strict. Only about 8% of the initial attempts passed every check used to measure the state's fidelity.
The research team also transferred these cultivated magic states into a larger protective arrangement compatible with a surface code, a system designed to protect quantum information from errors. This suggests that the cleaned-up quantum states can be transferred into larger codes for future storage and use. "Overall, our grafting results show a proof-of-principle demonstration of a magic state escaping into an advantageous code."
The research addresses one of the major obstacles holding back quantum computing, which is the massive amount of extra equipment needed to create the special states for universal calculations. Cultivation helps by refining noisy states directly inside a protected qubit, potentially reducing the resources needed to produce them.
Next steps for this technology include scaling it up for larger quantum computers.
Written for you by our author Paul Arnold, edited by Lisa Lock, and fact-checked and reviewed by Robert Egan—this article is the result of careful human work. We rely on readers like you to keep independent science journalism alive. If this reporting matters to you, please consider a donation (especially monthly). You'll get an ad-free account as a thank-you.
Publication details
E. Rosenfeld et al., Magic state cultivation on a superconducting quantum processor, Science (2026). DOI: 10.1126/science.aee7961
© 2026 Science X Network
