# Two paths, one flux: Trapped ions simulate Aharonov–Bohm interference in a lattice gauge theory

- Editoria: Engenharia e Computação Quântica (`quantica`)
- Fonte: Phys.org — https://phys.org/news/2026-11-paths-flux-ions-simulate-aharonovbohm.html
- Autor: Tejasri Gururaj
- Publicado: 2026-11-07T18:00:02+00:00
- Score: 4.112
- Imagem: imagens/quantica-two-paths-one-flux-trapped-ions-simulate.jpg | crédito: Phys.org | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Two paths, one flux: Trapped ions simulate Aharonov–Bohm interference in a lattice gauge theory
Tejasri Gururaj
Author
In a new Nature Physics study, researchers demonstrated the Aharonov-Bohm effect in a quantum simulation of a lattice gauge theory using a hybrid trapped-ion quantum computer.
Gauge theories describe how matter interacts through fields called gauge fields, which carry the electromagnetic, weak and strong forces. They form the basis of the Standard Model of particle physics. In lattice gauge theories, space is modeled as a grid with matter at the vertices and gauge fields on the links connecting them.
Quantum simulators offer a way to study these theories. However, most quantum simulations of the simplest version—the Z₂ lattice gauge theory—have been limited to one spatial dimension, where effects linked to magnetic flux cannot appear.
To address this issue, researchers from the University of Oxford have now used trapped ions to simulate a Z₂ lattice gauge theory in a quasi-two-dimensional loop. The trapped ions perform a dual role. Their electronic states encode the gauge fields and their vibrations encode the matter.
Phys.org spoke to the first author of the study, Sebastian Saner, about the work.
"We first started brainstorming how to use a hybrid trapped-ion quantum system to simulate lattice gauge theories back in 2022. Later, during the project, we had the idea of using entangled qubits to encode the gauge-field flux. Coming up with this idea was one of the particularly exciting moments for us during the project," said Saner.
Using two trapped ions, the team built a closed loop to see how a flux stored in entangled qubits would affect a moving particle.
Matter, fields and flux
"Gauge theories describe how particles interact with each other through gauge fields. A simple example is two electrons repelling each other through the electromagnetic field," explained Saner. "In this picture, the electrons are described by a matter field, while the electromagnetic field is the gauge field that mediates their interaction."
Some of the most puzzling materials in physics, such as quantum spin liquids and high-temperature superconductors, are also described by gauge theories. Here, the gauge fields emerge from the collective behavior of electrons. Physicists often describe these materials using Z₂ lattice gauge theories, the simplest type, in which the field at each link of a grid can take only two values.
In these theories, the two values represent whether a field line is present or absent. Z₂ lattice gauge theories are also relevant to topological quantum error correction.
Simulating these theories on classical computers is challenging. According to Saner, computational complexity generally grows exponentially with system size, particularly in higher dimensions. The physics also becomes richer with each additional dimension.
For instance, in two spatial dimensions, links can form closed loops, which can be pierced by a magnetic flux. This gives rise to quasiparticles called visons, which have no counterpart in one dimension, where no loops can form.
Earlier experiments have studied Z₂ lattice gauge theories using cold atoms and superconducting qubits, but mostly in one-dimensional setups. Some experiments have simulated two-dimensional geometries, but removed the matter fields to simplify the model. As a result, these approaches could not capture how moving charges and gauge fields influence each other, including how flux affects particle motion.
Ions doing double duty
"Trapped ions naturally have both qubits and vibrational modes. Typically, the ions' vibrations are cooled close to their ground state and used to mediate interactions between qubits, but are not directly used to store quantum information," explained Saner.
The team used both. Two electronic energy levels of a strontium ion served as a qubit, representing the gauge field on a link. The ion's vibrations, behaving like harmonic oscillators, served as the matter sites.
An oscillator can hold any number of units of vibrational energy, or phonons. In this simulation, a single phonon represents a matter particle.
"The advantage is that matter fields can be stored much more efficiently in the vibrational modes," said Saner.
The geometry of the lattice is determined by which qubits and vibrational modes are coupled together, not by the ions' physical positions. Even with the ions in a single line, these connections can create loops and other geometries that the arrangement alone can't. Dimensions created this way are known as synthetic dimensions.
To make the phonon hop, the researchers used a laser to apply two forces, each acting on a different vibrational mode and each pushing in a direction set by the qubit's state.
In simple terms, each time the particle hops between sites, the field line on the link switches between present and absent. This ties the particle's motion to the gauge field, as the theory requires.
The team first used a single ion to simulate one link connecting two matter sites. Adding a second ion introduced a second qubit, and so a second link between the same two sites. The result was a loop, which gave the particle two paths to choose from.
To encode the flux through this loop, the researchers entangled the two link qubits. One entangled state corresponded to zero flux, while the other corresponded to a nonzero flux, representing a vison.
"The hardest part was combining all the different ingredients and translating the theoretical ideas into a feasible experiment," Saner noted. "This involved getting the hybrid interactions to the required level of control, as well as developing the necessary state preparation and readout techniques."
Frozen by flux
With a single ion, the researchers observed the particle tunnel back and forth between the two sites, with the field line switching between present and absent. This is consistent with the Z₂ version of Gauss's law. As the particle moved away from the starting site, a field line stretched out behind it and disappeared when the particle returned to the site.
In these first runs, the researchers set the energy cost of creating a field line to zero. When the team then added the cost, the oscillations became faster but smaller, and the particle no longer moved fully from one site to the other. Because every move required creating a field line, moving became energetically costly. According to the researchers, this tunneling suppression is a precursor to confinement in larger systems, the effect that binds quarks together inside hadrons.
The researchers then moved to the two-ion setup to study the Aharonov–Bohm effect.
"The Aharonov–Bohm effect is a phenomenon where, in its original conception, an electron travels along two different paths around a region containing magnetic flux. Even though the magnetic field is zero along the paths of the electron, the interference pattern shifts depending on the magnetic flux," explained Saner.
In the loop, the two links play the role of the two paths. As the particle crosses a link, it picks up a phase set by that link's gauge field. In the Z₂ case, this phase is either a plus or minus sign. The flux through the loop determines whether the two paths give the particle the same sign or opposite signs.
When the two qubits were entangled in the zero-flux state, both paths gave the particle the same sign, so they added up. The particle tunneled freely between the sites, twice as fast as on a single link. When the two qubits were entangled in the state representing a vison, the two paths gave the particle opposite signs and canceled out. The particle stayed where it started, with its tunneling completely suppressed.
The researchers also confirmed that the flux remained constant throughout, except for a slow decay caused by decoherence. Numerical simulations that included known sources of noise, such as heating of the vibrational modes, agreed with the experimental data.
Next steps
According to the researchers, the results show that the hybrid approach can capture how flux affects the motion of matter, something earlier simulations without matter fields could not.
Saner sees two main directions for future work. The first is simulating larger lattices.
"Currently, we are simulating a single loop, which in lattice terms is still a very small system and can easily be solved using classical computers. However, even a relatively modest increase in lattice size could make the problem very difficult, if not impossible in practice, to solve using classical computers," said Saner.
The second is extending the approach beyond Z₂. "Future work could extend this to Zₙ gauge theories, where the gauge field can take a larger number of values, or even toward the limit N → ∞," Saner explained.
Written for you by our author Tejasri Gururaj, edited by Gaby Clark, and fact-checked and reviewed by Robert Egan—this article is the result of careful human work. We rely on readers like you to keep independent science journalism alive. If this reporting matters to you, please consider a donation (especially monthly). You'll get an ad-free account as a thank-you.
Publication details
Aharonov–Bohm interference in a Z₂ lattice gauge theory on a hybrid qubit–oscillator quantum computer, Nature Physics (2026). DOI: 10.1038/s41567-026-03400-6.
Key concepts
Quantum algorithms & computationQuantum correlations, foundations & formalismQuantum field theoryQuasiparticles & collective excitations
© 2026 Science X Network
