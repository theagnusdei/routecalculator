# Autonomous crane system handles port containers with centimeter-level precision

- Editoria: Robótica (`robotica`)
- Fonte: Tech Xplore — https://techxplore.com/news/2026-11-autonomous-crane-port-centimeter-precision.html
- Autor: Ingrid Fadelli
- Publicado: 2026-11-26T14:20:02+00:00
- Score: 5.077
- Imagem: imagens/robotica-autonomous-crane-system-handles-port-con.jpg | crédito: Tech Xplore | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Autonomous crane system handles port containers with centimeter-level precision
Robotic systems have already been deployed in many factories, industrial sites and warehouses worldwide to automate processes and improve their efficiency. A taxing task that requires the precise control of large machinery is lifting and moving shipping containers in ports.
Automating this task has so far proved difficult, as cranes must move heavy, suspended loads accurately while avoiding collisions with nearby obstacles. The loads can sway, and successfully placing them requires centimeter-level adjustments.
Researchers at the Hong Kong University of Science and Technology (Guangzhou), Southeast University and Shanghai Master Matrix Information Technology recently introduced Autane, a system for the autonomous operation of port cranes. The new system, introduced in a paper published in Science Robotics, was found to reliably operate rubber-tired gantry (RTG) cranes, large, wheeled structures that straddle rows of shipping containers.
Autane: A system that autonomously operates port cranes
Rather than designing new cranes that can be automated more easily, the researchers set out to develop an autonomous system to reliably operate existing RTG cranes, which are widely used in port yards worldwide. These cranes lift and stack containers and transfer them to and from transport vehicles.
"Fully automated cranes are revolutionizing modern port operations by addressing labor shortages, improving precision and enhancing safety," wrote Jun Yang, Zheng Tian and their colleagues in their paper. "Toward this goal, we present the Autane (autonomous crane) system specifically developed for RTG cranes handling standardized containers in port yards, enabling autonomous safety-critical container grabbing, transport and placement with high accuracy, adaptability and efficiency."
Autane, the new system, relies on different sensors to track motion and perceive its surroundings, gathering information that can be used to plan a crane's movements. These include cameras, laser-based distance sensors called LiDAR, satellite-positioning tools and motion sensors.
The information collected by these sensors is integrated and analyzed to locate containers and obstacles around the robotic crane. A technique called SLAM (simultaneous localization and mapping) then estimates the crane's position while building a map of the surrounding environment.
The researchers connected their system's perception capabilities with planning and control algorithms, which plan and adjust a crane's movements in changing conditions. In addition, they incorporated a sensor calibration component, as well as fault detection and recovery techniques.
"Autane overcomes the challenges of safe motion of large-scale cranes with centimeter-level precision requirements, providing long-distance high-precision perception," wrote the researchers. "It uses multisensor fusion, real-time obstacle detection and simultaneous localization and mapping to perceive the environment, identify container features and dynamically adjust trajectories."
Toward further deployment in working ports
To assess their system, the team deployed Autane at various ports in Shanghai, Ningbo, Suzhou and Hong Kong, where it was installed on more than 60 cranes to perform container-handling tasks.
"By tightly coupling perception, planning, control, and operation and maintenance, Autane achieves safe and precise alignment, seamless interaction with transport vehicles and robust execution of long-distance handling tasks," wrote the authors. "Deployed in multiple ports, Autane shows full-day operation and has autonomously handled more than 2 million 20-foot equivalent units."
According to the university's announcement, Autane achieved a task success rate of 91.23% across over 60,000 operations, averaging approximately 25.93 container moves per hour. In addition, the system could resolve approximately 90% of transient faults without requiring human intervention.
"This work highlights the potential of fully autonomous RTG cranes to enable sustained, resilient and low-intervention port automation," wrote the authors.
In the future, Autane could be refined further and tested in a broader range of ports in China and potentially other countries. Eventually, it could help to automate hazardous crane operations, reducing the exposure of human workers to situations that could lead to work accidents or injuries.
Written for you by our author Ingrid Fadelli, edited by Lisa Lock, and fact-checked and reviewed by Robert Egan—this article is the result of careful human work. We rely on readers like you to keep independent science journalism alive. If this reporting matters to you, please consider a donation (especially monthly). You'll get an ad-free account as a thank-you.
Publication details
Jun Yang et al., Autane: An autonomous crane for sustained port operations, Science Robotics (2026). DOI: 10.1126/scirobotics.ady5784
© 2026 Science X Network
