# Will ‘boring’ robots win in the real world? Why robotic form should follow workflow

- Editoria: Robótica (`robotica`)
- Fonte: The Robot Report — https://www.therobotreport.com/will-boring-robots-win-in-the-real-world-why-robotic-form-should-follow-workflow/
- Autor: Brianna Wessling
- Publicado: 2026-10-11T12:36:24+00:00
- Score: 4.573
- Imagem: imagens/robotica-will-boring-robots-win-in-the-real-world.jpg | crédito: The Robot Report | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Robots have captured our imagination. We have seen humanoids balancing on one leg, doing backflips, folding laundry, and moving smoothly over difficult terrain. This is all behavior that only a few years ago seemed like something out of science fiction. These viral examples matter because they show that embodied AI has reached a new technical stage.
At the same time, the window on what qualifies as a “humanoid robot” seems to be shifting. Robot companies are adding wheels, more sensors, new manipulators, hats, and screens, while they take away eyes and heads from their humanoid robot designs.
As an engineering ecosystem working directly alongside humanoid developers to solve core hardware bottlenecks, we see a recurring theme. The industry frequently gets caught up in “robot-forward” thinking. We build an extraordinary physical platform first, then scour industrial sites for a task for it to perform.
If we want to move physical AI from social media feeds to a sustained commercial level, we must reverse our current approach. The industry needs a design method that works backwards from the workflow. Begin with a task that has economic value. Consider whether a robot can carry out that task better than a human can.
Then, go backwards to find out exactly what hardware, sensing capabilities, and form factor are actually needed to carry out the task.
The sensor stack is born in the task, not the datasheet
If you start by designing a platform, you will likely end up with a compromised hardware stack. The specific workflow determines the machine’s engineering requirements.
Let’s take as an example a bipedal humanoid robot that is asked to carry out two different industrial work processes. One involves inserting a pin on an automotive assembly line and the other involves packing a pallet in a logistics center.
A pin connector insertion task generally involves a 20 µm clearance and 5 N mating force. So, there needs to be contact-force resolution below 0.1 N and a control bandwidth fast enough to detect jamming before a sensitive pin bends.
Yet, when using the same arm for bulk pallet packing, you need almost none of that high-frequency micro-force resolution. Instead, you need heavy payload capacity, structural rigidity, and the ability to endure 1 million cycles without baseline mechanical drift.
If you are building a general-purpose platform, a single “middle-of-the-road” force sensor may result in a system that could make precise pin insertion difficult. The system could also lack the durability needed for continuous heavy lifting.
The workflow also determines your error budget. This is the only factor that turns force sensing from a cost item into something that provides a demonstrable return on investment.
Attempts to improve force sensing often fail. For example, our tests have shown that using a specific calculation maintaining contact force at ±0.2 N, can reduce connector scrap in amounts from 1.2% to 0.5%. This can translate into annual estimated savings of approximately $450,000 per assembly line. This kind of economic argument is only possible if you begin with the task in question.
That is exactly the reason why the selection of critical components, for example those based on strain sensing, must take place at the architectural design stage rather than being treated as an afterthought when preparing the bill of materials (BOM).
Adjusting the robot rather than adjusting the facility
The tendency to focus on the task first raises the main question about form factor. Is a specialised form factor the better choice? When is a humanoid design strictly necessary?
Operating environments can be divided into two types: greenfield and brownfield. The real issue is not what the robot should look like, but whether it is cheaper to modify the robot or to modify the facility.
With greenfield sites, you can use specialized robots. With brownfield sites, like an existing refinery or chemical plant, the robot has to adapt to spaces created for humans.
In greenfield builds, like Equinor’s Northern Lights facility, the operator can design the layout from the beginning and construct the facility around the task. So, specialized, non-humanoid forms almost always prove better in terms of unit economics, speed, and energy efficiency. Legged and wheeled robots are more reliable for the types of tasks they carry out.
However, in most cases, industrial activities take place in brownfield sites, where the only practical option is to adapt the existing platform. These sites have narrow aisles, stairs, floor grating, and doorways designed with the human body in mind. In this situation, a human-suitable form factor, whether that involves legs, two arms, or a humanoid shape, becomes a major advantage. It lets the equipment operate in environments designed for people without spending millions of dollars retrofitting the facilities.
The true test for a humanoid design is whether, if you were starting again, you would still go with a humanoid. When human compatibility is needed, the basic physical requirements stay the same: foot contact, joint torque, and wrist force.
The robots may come in different shapes, but they have the same sensory physics. Strain-based sensing endures even when the form factor changes, offering fundamental ground-truth measurement regardless of how your physical platform develops.
Deployment depth beats demo breadth
Flashy viral videos show what is technically possible. The true test, however, is not the demonstration itself but the second purchase order. Only through repeat orders can business utility be proven.
Although demonstrations using units calibrated under climate-controlled conditions prove a robot can function once, full fleet deployment demands that the robot survive at least 10,000 cycles per shift amid constant thermal variation and with near-zero tolerance for drift.
Most physical AI projects fail because the engineering effort turns instead to broad, general promises before addressing specific operational facts. In real-world situations, deployments fail due to drift, sensor fatigue, and recalibration challenges, not flaws in reasoning.
Editor’s note: Humanoids and physical AI are among the session track topics at RoboBusiness 2026, which will be on Oct. 20 and 21 in Santa Clara, Calif. Register now to attend.
The physical AI balance sheet
Integrating AI into physical hardware requires a disciplined balance between power consumption, thermal dissipation, mechanical wear, and safety limitations. With software, you scale by making copies; with hardware, you have to buy it, build it, and wait.
Teams that take a software approach often fail to account for this physical balance sheet. Beyond basic thermal or electrical limits, non-linear actuator gear reductions introduce complex behaviour that is notoriously difficult to predict and simulate.
True backdrivability solves part of this problem by allowing the robot actuator or joint to fully reflect any physical impact from the environment back to the core control architecture.
Whatever the hardware bottleneck may be, whether it’s thermal throttling in the joint actuators or the amount of power drawn under peak load, each constraint comes down to the same need: knowing exactly what force is present under actual loading conditions, at real temperatures, over a period of years. This is the information that strain-based sensing provides, which is why it should be included in the architecture and not just listed in the bill of materials.
The real metrics of commercial viability
To assess the commercial viability of physical AI systems, we should go beyond slick-looking marketing videos. Instead, we should focus on the metrics that finance teams actually care about.
The most important and essential metric is mean time between interventions (MTBI). This can be considered the most genuine measure used in the industry, but is the one that is least often published. If a human operator has to intervene every 20 minutes to unjam a gripper or reset a drifted sensor, then high autonomy figures have little significance.
We need to assign the same importance to the actual cost per unit of work, whether calculated on a per-pick, per meter travelled, or per inspection completed basis. This figure ultimately determines whether a robot fleet will replace or augment existing labour.
Operational value also depends on redeployment time. Deployment time shows whether a “general-purpose” platform can swiftly adjust to a new task or whether reconfiguration requires weeks of custom engineering. Lastly, the number of safety incidents per operating hour will determine if the robot ever goes outside of its cage to operate freely among human workers.
A viral video shows a robot capable of carrying out a given task once. However, a sustainable business needs the robot to carry out that same task at least 10,000 times in a row, without any intervention, drift, or failure.
The main conclusion is straightforward: Start with the workflow, build reliable sensing into the core architecture, and focus on operational metrics so both specialised machines and humanoid platforms can fulfil their potential in the physical world.
Ron Zukerman is an innovation director at Vishay Precision Group Inc. (VPG). The company is a leader in precision measurement and sensing technologies.
VPG said its sensors, weighing solutions and measurement systems optimize and enhance customers’ product performance across a broad array of markets to make the world safer, smarter, and more productive. To learn more, visit the company at www.vpgsensors.com and follow it on LinkedIn.
