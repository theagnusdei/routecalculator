# Reading superconducting qubits while suppressing unwanted state transitions

- Editoria: Engenharia e Computação Quântica (`quantica`)
- Fonte: Phys.org — https://phys.org/news/2026-11-superconducting-qubits-suppressing-unwanted-state.html
- Autor: David Appell
- Publicado: 2026-11-16T16:20:42+00:00
- Score: 6.205
- Imagem: imagens/quantica-reading-superconducting-qubits-while-sup.jpg | crédito: Phys.org | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Reading superconducting qubits while suppressing unwanted state transitions
David Appell
Author
Recently an artificial intelligence proved an 18-year-old conjecture in computer science, called the Aaronson–Ambainis conjecture. The proof settles a long-standing conjecture (educated guess) that eliminates one proposed route to enormous quantum computer speedups, ruling out one particular variant of "quantum supremacy," the term for the hypothesis that a programmable quantum computer can solve a problem that no classical computer can solve in any "feasible" amount of time.
But as theoretical computer science expert Scott Aaronson of the University of Texas at Austin wrote, "It doesn't undermine any form of quantum supremacy that we did conjecture to exist!" Which is to say, despite what you may have heard, the promises of quantum computing are still very much alive. Quantum computing is still very difficult, though. In particular, reading qubits is challenging because reading them often changes their state.
Toward that end, a research team from Colorado in the U.S. with a team member from Canada has built a device that can read a qubit without changing its state, with more than 99% fidelity. Their work is published in the journal Physical Review Letters.
Reading qubits without changing their state
Akash V. Dixit of the U.S. National Institute of Standards and Technology in Boulder, Colorado, and colleagues explore "the interaction between millimeter-wave photons and conventional transmon qubits, specifically for qubit readout."
A "qubit" is the quantum mechanical version of a binary bit; its power comes because it is able to exist in more than one state simultaneously. A binary bit can only be in one state, 0 or 1. During calculations, the qubit uses all its simultaneous states, but when the state of the qubit is measured, it will be in one of two quantum mechanical states: |0> or |1>.
The state of a superconducting qubit is measured by a device called a readout resonator. The problem is, such a device often struggles to maintain the qubit's original state when consistently reading the qubit. Dixit and colleagues found a way around this problem, using a microwave resonator that operates in the millimeter range of wavelengths at a frequency of 35 gigahertz (GHz). Their new device accurately reads states using a much higher resonator frequency than conventional designs.
Readout resonators are microwave cavities, enclosed structures usually made of metal, that trap microwaves inside. At certain frequencies, depending on the shape of the cavity, microwaves will form standing waves inside (also called stationary waves), allowing waves to reinforce one another and efficiently storing electromagnetic energy.
In particular, the resonant frequency of a readout resonator changes depending on whether the qubit is in its ground state or its excited state. Thus, readout resonators are used to measure the state of transmon qubits, the most widely used type of superconducting qubit. (The design of a transmon is basically a Josephson junction paired with a large shunting capacitor, designed to be unusually insensitive to electrical charge noise.)
Conventional transmons operate at 3 to 6 GHz, using readout resonators at 6 to 10 GHz. Here the researchers instead coupled a 3.083 GHz transmon to a 34.670 GHz aluminum cavity, meaning a readout-to-qubit frequency ratio greater than 10.
Thus a frequency measurement from the cavity measures the qubit's state. The new device's measurement fidelity is 99.2% using 109 readout photons, and the readout takes just 780 nanoseconds. This strategy raises the readout frequency rather than lowering the qubit frequency, preserving properties useful for conventional qubit operation.
The group writes that increasing the readout frequency to the millimeter range and keeping the transmon frequency in the microwave range "allows us to maintain the required transmon anharmonicity needed for fast gates and operate with minimal residual thermal population."
Suppressing unwanted state transitions
The group used a technique called Floquet simulations that helps explain why the large frequency separation works. The simulations are based on Floquet theory, a branch of ordinary differential equations providing a way to analyze systems being affected by regular, periodic pulses, particularly when the system's response is not constant but results in an enhanced response, akin to pushing a child on a swing. The simulations show that at millimeter-scale frequencies, the cavity drive mostly avoids transitions between states in the transmon's Josephson potential well.
"Because the drive-induced state transitions are suppressed," they write, "we are able to perform a high-fidelity qubit readout using more than 100 photons." Moreover, they say coupling millimeter electromagnetic waves and transmon qubits in this way "paves the way for further advancements in circuit QED (quantum electrodynamics) experiments."
Applications of this new coupling they foresee include aid in dark matter searches and experiments where ultrastrong light interacts with matter in QED circuits. They also write that the coupling "may be a central technology for hybrid quantum systems that leverage the capabilities of platforms, such as circuit optomechanics, Rydberg atoms, and other superconducting qubits."
Written for you by our author David Appell, edited by Sadie Harley, and fact-checked and reviewed by Robert Egan—this article is the result of careful human work. We rely on readers like you to keep independent science journalism alive. If this reporting matters to you, please consider a donation (especially monthly). You'll get an ad-free account as a thank-you.
Publication details
Akash V. Dixit et al., Millimeter Wave Readout of a Superconducting Qubit, Physical Review Letters (2026). DOI: 10.1103/c84y-ggqs. On arXiv: arxiv.org/abs/2603.13837
© 2026 Science X Network
