# IBM Connects Two 120-Qubit Processors With 99% State-Transfer Fidelity

- Editoria: Engenharia e Computação Quântica (`quantica`)
- Fonte: The Quantum Insider — https://thequantuminsider.com/2026/10/27/ibm-connects-two-120-qubit-processors-with-99-state-transfer-fidelity/
- Autor: Matt Swayne
- Publicado: 2026-10-27T08:01:04+00:00
- Score: 6.006
- Imagem: imagens/quantica-ibm-connects-two-120-qubit-processors-wi.jpg | crédito: The Quantum Insider | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Insider Brief
- IBM researchers linked two 120-qubit quantum processors with four superconducting cables, demonstrating connections that could support larger modular quantum computers.
- The links achieved average quantum state-transfer fidelity of 99% and enabled operations and entanglement between qubits on separate processors.
- Complete operations between processors averaged 94.75% fidelity, with further improvements needed in qubit stability, magnetic shielding and manufacturing before scaling the approach.
IBM researchers connected two quantum processors through four superconducting cables, demonstrating a way to build larger quantum computers from separate chips.
The links transferred quantum states with an average fidelity of 99% and supported operations between computing elements on different processors, according to a study posted on the preprint server arXiv. The team also created entangled states spanning the chips, including two pairs generated at the same time through neighboring connections.
The results address a practical problem in quantum computing: how to make separate processors work together without losing the fragile information that gives the machines their potential. Connecting modules could let developers expand a computer beyond the limits of a single chip.
The experiment also shows that work remains. Complete operations between the processors had an average fidelity of 94.75%, below the performance of the state transfers alone. Only a subset of the computing elements on each processor was wired and measured.
Building a Computer Across Chips
The researchers connected two IBM Nighthawk R1 superconducting processors, each containing 120 qubits. Qubits are the basic units of quantum information, but their useful properties can be disrupted by energy loss, environmental interference and imperfect controls.
A modular computer would divide the work among processors, using quantum connections to coordinate operations across them. Those links must preserve quantum states and support entanglement, a relationship in which separate qubits share a joint quantum state.
The IBM team used four aluminum coaxial cables, each about 80 centimeters long, to bridge the processors. The cables operated as superconducting microwave links inside the system’s ultracold environment.
The distance reflects the physical demands of installing processors, cooling equipment and control wiring, according to the study. These are connections within a quantum computing system, rather than links intended to carry information across a conventional telecommunications network.
Earlier experiments have transferred quantum states and generated entanglement through superconducting cables. Many of those experiments used modules containing only a few qubits and a single connection between processors, the researchers write.
IBM’s contribution centers on operating several connections between large processors with a cable attachment designed for more densely connected systems. The researchers describe the work as — to their knowledge — the first demonstration of a multichannel quantum interconnect between large superconducting quantum processors.
The 120-qubit chip size does not mean the experiment coordinated all 240 qubits, as the team wired and measured only selected qubits near the connections to speed development.
Transferring States and Creating Entanglement
Each connection used dedicated qubits at the cable’s ends to move quantum information between modules. Adjustable coupling devices controlled how those qubits interacted with the cable.
The researchers measured state-transfer performance in both directions using network benchmarking, a method that separates transfer errors from errors associated with preparing and measuring the qubits.
All four links achieved state-transfer fidelities of at least 98.86%. The best reached 99.29%, with an uncertainty of 0.07 percentage points. Fidelity measures how closely an operation or prepared state matches its intended result.
The team then used the connections to perform controlled-Z gates between ordinary computing qubits on separate processors. A controlled-Z gate changes the relationship between two qubits’ quantum states and can help create entanglement.
That complete operation required more steps than transferring a state across a cable. It combined two state transfers, three local two-qubit gates and additional single-qubit controls.
The extra steps introduced additional opportunities for error. Average fidelity for the distant gates was 94.75%, while the best reached 96.42%, with an uncertainty of 0.28 percentage points, according to the paper.
Using those gates, the researchers generated entangled pairs across the processors. They also generated two pairs simultaneously through adjacent links. Both pairs remained entangled, although one showed a measurable decline in fidelity during simultaneous operation.
The experiment extended entanglement to groups of four and six computing qubits distributed across the chips. These larger states show that the connections can support operations beyond the dedicated qubits at the cable ends.
The four-qubit state had a measured fidelity of 77.23%, while the six-qubit state reached 67.67%. After statistical correction for measurement errors, those figures rose to 91.70% and 90.87%, respectively.
While correcting measurement results does not improve the underlying physical operation, both states nevertheless exceeded the threshold needed to establish genuine entanglement across the group without that correction, the researchers reported.
A Connection That Can Survive Cooling
Part of the work focused on assembly rather than quantum operations.
The cables attached perpendicular to the processor surface, a shape intended to accommodate more connections. Earlier IBM designs placed the cable-to-chip connection parallel to the surface, creating difficulties for reliability and denser packing, according to the study.
The new arrangement used indium-to-indium pressure bonds made at room temperature after both processor modules had been mounted in the cryogenic system. A spring-loaded holder installed two cable connections at once, using screws and visual alignment.
All four links remained operational through three cycles of warming and cooling without adjustments to their connections.
That durability is required because a modular machine will need maintenance and reconfiguration over its lifetime, the researchers write. However, the team did not disconnect and reconnect the bonds in this experiment. Their suitability for repeated reconnection may be the focus of further testing.
The researchers also identified a source of cable loss: magnetic fields present while the aluminum cooled into its superconducting state.
In controlled tests, the cable’s ability to retain microwave energy declined substantially as the magnetic field during cooling increased. Changing the field after the cable had become superconducting did not reverse the effect.
The team added magnetic shielding around the cables. Two layers were needed, and the researchers described the shielding braid as a temporary solution. The physical mechanism behind the observed loss remains unresolved, although the paper identifies trapped magnetic fields as a possible explanation.
Reducing the Remaining Errors
The study points to several routes for improving performance, while distinguishing projections from measured results.
An error model attributed about 77% of the measured state-transfer error to the limited persistence of quantum states in the cable and its dedicated qubits. The largest modeled contribution came from the qubits losing a stable phase relationship, a process known as dephasing.
The researchers intentionally omitted some fabrication and processing steps known to improve qubit performance to accelerate development. They therefore argue that the observed qubit limitations are not inherent to the cable-link approach.
With improved qubit coherence, their model placed state-transfer fidelity between 99.68% and 99.77% across the four links. Those figures are modeled limits under specified conditions, not experimental results.
The team also identified a design change that could reduce the cost of distant operations: integrating the connection elements directly into the processor’s computing lattice. That would eliminate some of the intermediate operations required by the present arrangement, according to the paper.
The next challenge is to turn four working links into many reproducible connections while improving fidelity, shielding and manufacturability. The experiment establishes a component for that effort. Demonstrating a larger machine that repeatedly uses those connections for reliable, error-corrected computation remains ahead.
The study was conducted by Neereja M. Sundaresan, Nicholas Cotaj, Yadav Prasad Kandel, Eric Lewandowski, Christian Robert Longton, Yves Martin, Jae-woong Nah, Kathryn Pooley, Martin Sandberg,† Michael Scanlon, Chi Xiong, Emanuil Sashev Yanev, David Abraham, Abhinandan Antony, Vincent Arena, Nicholas Bornman, Khanh Dang, Oliver Dial, Christopher Guarino, Gabriel Haspil, Jared Hertzberg, Kentaro Heya, Swetha Kamlapurkar, Michael Karschner, George Keefe, Eric Liniger, Laura Luo, Thomas G. McConkey,† David Olson, Jason Orcutt, Dmitry Ovchinnikov, Timothy Phung, Sankeerth Rajalingam, Michael Selvanayagam, William Shanks, Dongbing Shao, Abigail Shearrow, Adam Stabile, Jiri Stehlik, Joseph Suttle, Jeng-Bang Yau and Eric Zhang, all researchers at IBM Research’s Thomas J. Watson Research Center in Yorktown Heights, New York.
For a deeper, more technical dive, please review the paper on arXiv. It’s important to note that arXiv is a pre-print server, which allows researchers to receive quick feedback on their work. However, it is not — nor is this article, itself — official peer-review publications. Peer-review is an important step in the scientific process to verify results.
Matt Swayne
Get the latest research, company news, and market intelligence every week.
