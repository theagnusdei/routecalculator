# Robots recognize the shape of an arena by messaging each other

- Editoria: Robótica (`robotica`)
- Fonte: Tech Xplore — https://techxplore.com/news/2026-11-robots-arena-messaging.html
- Autor: Ingrid Fadelli
- Publicado: 2026-11-14T13:40:02+00:00
- Score: 3.478
- Imagem: imagens/robotica-robots-recognize-the-shape-of-an-arena-b.jpg | crédito: Tech Xplore | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Robots recognize the shape of an arena by messaging each other
Ingrid Fadelli
Author
Humans can create loose maps of environments they are exploring in their minds, using their senses and navigation skills. Many robots, on the other hand, rely on set maps of known environments or new maps produced using data collected by their sensors.
Researchers at Sorbonne University's Institute of Intelligent Systems and Robotics (ISIR), the University of Tokyo and other institutions recently introduced a framework that could allow a swarm of tiny robots to recognize the shape of an enclosure they are in without a map. Their approach, outlined in a paper published in Science Robotics, allows robots to identify the enclosure from a set of known shapes by repeatedly exchanging messages with nearby robots.
"The project addressed a fundamental question in swarm robotics: how can a group of simple robots perceive something that none of its members can observe alone?" Leo Cazenille, first author of the paper, told Tech Xplore.
"It is not unlike the parable of the blind men and the elephant: each man touches only one part of the animal, so none can guess its overall shape. Similarly, each robot can only perceive its immediate neighbors and has no GPS, camera or sufficient memory or computing power to build a map. So how could they recognize the shape of the space they are in?"
Local messages as clues to an enclosure's shape
The recent project originated from a close research collaboration between roboticists, biophysicists and mathematicians. The authors drew inspiration from a famous question posed by the mathematician Mark Kac: Can one hear the shape of a drum?
"The notes a drum produces depend on the shape of its membrane, and we wondered whether a swarm could similarly 'listen' to how numerical information (not sounds) was exchanged between its members," said Cazenille. "The objective was for every robot to learn the shape of the space the swarm occupies without knowing its own position, building a map or relying on a central computer."
The researchers' newly developed approach, spectral swarm robotics, allows groups of robots to learn information about the space they occupy simply by sharing information with their neighboring robots. The term "spectral" comes from the mathematical field of spectral analysis. In this context, it is used to describe the mathematical signature (i.e., spectrum) of an arena's shape.
"The idea is to use the swarm's communication network as a collective sensor," explained Cazenille. "Each robot holds a number representing a virtual temperature and exchanges it with nearby robots, updating its value as though heat were spreading through the group.
"The rate at which temperature differences fade depends on the network of connections, reflecting the geometry of the space occupied by the swarm. By monitoring how its own value changes, each robot can estimate a numerical signature of that geometry and compare it with references for known shapes."
The method proposed by Cazenille and his colleagues only relies on the exchange of short messages between robots and simple calculations. It thus eliminates the need for cameras, information about the position of robots on a map or a central computer that processes the data exchanged by robots.
Tests with real robots
The researchers first assessed their approach mathematically and ran simulations with swarms of up to several hundred robots across seven arena shapes. They also performed experiments with swarms of two different robot types, called Kilobots and Pogobots.
In the real-world experiments, both swarm types successfully used messages exchanged between nearby robots to distinguish a disk-shaped arena from a ring-shaped one. The Kilobots identified the correct shape of an arena in 22 of 30 trials.
"A group of just 25 Pogobots, on the other hand, correctly distinguished between a disk-shaped and a ring-shaped arena in all 30 trials," said Cazenille. "We also identified a relationship between swarm size, communication range and arena area that helps to determine optimal conditions for this method."
Recognizing shapes without a map
Cazenille and his colleagues introduced a new strategy that could allow swarms of robots to infer the shape of their surroundings. This approach could be particularly advantageous for improving the navigation of robot swarms with limited capabilities.
"We demonstrate how the pattern of connections between robots can itself become a tool for sensing and computation," said Cazenille. "Although the presented algorithm focused on identifying the shape of the arena, the approach may be general enough to be applied to more complex tasks involving the local estimation of global properties."
Notably, the team's study focused on the ability of robots to recognize an arena's shape. The extent to which recognizing the shape could improve the swarm's navigation could be assessed in future studies.
The researchers now plan to run experiments with various robot swarms navigating a broader range of environments. They would also like to improve their approach, allowing it to extract richer geometric information about an arena by estimating multiple spectral values.
"Another important development would be to enable robots to keep moving while estimating these properties, so that the method can operate as their communication network changes," added Cazenille.
"We also intend to explore tasks beyond shape recognition, such as identifying boundaries or cavities. In the longer term, our aim is to connect collective perception to action, enabling a swarm to adjust its distribution or formation in response to its perceived environment."
Written for you by our author Ingrid Fadelli, edited by Sadie Harley, and fact-checked and reviewed by Robert Egan—this article is the result of careful human work. We rely on readers like you to keep independent science journalism alive. If this reporting matters to you, please consider a donation (especially monthly). You'll get an ad-free account as a thank-you.
Publication details
Leo Cazenille et al., Hearing the shape of an arena with spectral swarm robotics, Science Robotics (2026). DOI: 10.1126/scirobotics.adr9578.
© 2026 Science X Network
