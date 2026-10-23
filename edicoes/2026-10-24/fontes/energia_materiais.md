# Data-driven operation of biogas plants: Generating electricity when wind and solar power are scarce

- Editoria: Energia e Novos Materiais (`energia_materiais`)
- Fonte: Phys.org — https://techxplore.com/news/2026-10-driven-biogas-generating-electricity-solar.html
- Autor: Fraunhofer Institute
- Publicado: 2026-10-23T11:20:02+00:00
- Score: 5.24
- Imagem: imagens/energia_materiais-data-driven-operation-of-biogas-plants-g.jpg | crédito: Tech Xplore | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Data-driven operation of biogas plants: Generating electricity when wind and solar power are scarce
Biogas plants are considered the third pillar of renewable electricity generation in Germany. Unlike solar and wind power, electricity generation from biogas is largely independent of weather conditions and can generally be scheduled.
With an amendment to the Renewable Energy Sources Act (EEG) planned for 2027, the regulatory framework is expected to place greater emphasis on flexible, market-oriented electricity generation: Biogas plants would supply electricity primarily when solar and wind generation is low. To support this shift, the number of operating hours eligible for remuneration is expected to be limited.
For operators of the nearly 10,000 biogas plants currently operating in Germany, the timing when electricity is fed into the grid from combined heat and power (CHP) units will increasingly determine the economic viability of their operations. Expanding gas storage capacity is likely to be economically viable for only some older plants.
Fraunhofer IGB has developed a cost-effective digital approach to electricity-price-based operation: An "Edge Device" is connected to the existing plant control system, consolidates process and operational data, and makes these data available onsite for models and AI applications—without requiring changes to the existing control logic.
Biogas plants generate more data than they use
A biogas plant generates a significant amount of data: Sensors measure temperatures in the digester, the composition of the biogas and the fill level of the gas storage tank.
The plant control system tracks the rotational speeds, runtimes and operating statuses of pumps and agitators. It also logs warnings and malfunctions. Other information is not measured directly but is equally crucial—such as which substrates are fed into the system and in what quantities.
However, the majority of this information is used solely for the immediate operation of the plant. "For long-term analyses, forecasts or comprehensive optimization, the data are often not available in the required format," explains Alexander Laug, a process engineer at Fraunhofer IGB.
Measured values are often stored only for a limited time, data structures vary, and important contextual information—such as operating states or threshold values—is available only separately.
Optimizing the operation of a biogas plant requires the various data sets to be considered together. A temperature reading of "40 degrees," for example, only gains meaning within the context of the plant: In which tank was it measured, and what setpoint applies there? Is the associated pump running, and is the plant in automatic or manual mode? Which substrates were added previously, and how is gas production developing?
A data platform in the control cabinet
The Edge Device brings these data together. "Our Edge Device is an industrial computer that is installed onsite. It adds a data processing and computing layer to the existing programmable logic controller (PLC)," explains Laug.
The Edge Device retrieves process and operational data from the PLC, stores them over extended periods and organizes them in a consistent structure. This creates a common data foundation that links current measurements, historical trends and associated operating states. External information, such as electricity price forecasts and weather forecasts, can also be integrated.
Data processing takes place directly onsite. "Operational data do not necessarily have to be transferred to an external cloud," Laug explains. Instead, operators decide for themselves which data leave the plant and which are processed exclusively locally. In doing so, Fraunhofer IGB relies on a technical architecture that is as open as possible. This allows the platform to be adapted to different plants and tasks and expanded with additional models or applications.
The Edge Device bridges conventional plant automation and data-driven plant operation. While the PLC remains responsible for reliable plant control, the Edge Device adds data storage, analytics and computing capabilities for forecasting, optimization and AI models. Multiple applications can build on the same data foundation. These may include electricity price and gas production forecasts, soft sensors, energy optimization and predictive maintenance.
From data to decisions
The real added value arises when the aggregated data are transformed into concrete operational recommendations. The system takes into account not only the plant's current status but also how it has evolved over time.
"It can determine how gas production and gas composition have changed following the addition of a specific feedstock, how full the gas storage tank is, or how long pumps and other equipment have been running," explains Laug. Not every application needs to intervene directly in the plant control system. Models can initially focus solely on analyzing data and generating recommendations for operational staff.
Generating electricity when it delivers the greatest value
For electricity-price-based operation, the data platform combines the current plant status with electricity price forecasts. "A high expected electricity price alone is not enough to make a decision—sufficient gas must also be available, and the plant must be technically capable of operating as planned," says Laug.
Accordingly, the system considers expected gas production, the gas storage level, available combined heat and power (CHP) capacity, and technical operating constraints. Based on these inputs, the model proposes an operating schedule: When should biogas be stored? When should the CHP unit run? And when is electricity generation likely to yield the highest revenue at forecast market prices?
Feedstock also influences electricity generation
Digital optimization can begin even earlier in the process, because the amount of biogas available at a given time depends largely on the feedstock supplied to the digester. Substrates differ in their organic content, biogas yield potential and cost. They also produce biogas at different rates.
By combining these data with historical operating data, it becomes possible to assess how a particular substrate mix affects subsequent gas production and, in turn, electricity generation.
"An optimization model can calculate how an available substrate mix should be composed without exceeding the digester's permissible load limits," explains Laug.
At the same time, substrate costs and expected gas production can be taken into account. The goal is not to produce as much gas as possible. What matters is when and how much gas is available, what it costs to produce, and how it can subsequently be used as effectively as possible.
Operators can already test a simulation tool on the institute's website that illustrates the effects of substrate mix and electricity prices on a biogas plant operating strategy optimized in line with electricity prices.
Applicable to other process engineering facilities
The principle underlying this data infrastructure can be applied to other process engineering facilities—from wastewater treatment plants to irrigation systems and drinking water supply systems. These facilities generate a large amount of measurement data and operational information, which are currently used primarily for real-time control.
In wastewater treatment plants, for example, typical opportunities for optimization include more demand-driven aeration of the biological treatment stage and the monitoring of energy-intensive equipment.
Existing facilities therefore do not need to be completely rebuilt to make better use of their data. Laug sums it up: "The first step toward a smart facility is to bring existing information together in a reliable, understandable data foundation. Forecasts, soft sensors and model-based operational optimization can then be built on that foundation."
