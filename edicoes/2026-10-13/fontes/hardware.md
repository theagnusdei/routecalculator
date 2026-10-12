# AMD debuts Helion reference design for agentic AI servers with up to 32,768 Zen 6 ‘Venice’ cores

- Editoria: Hardware (`hardware`)
- Fonte: Tom's Hardware — https://www.tomshardware.com/pc-components/cpus/amd-debuts-helion-reference-design-for-agentic-ai-servers-with-up-to-32-768-zen-6-venice-cores-rack-design-ships-next-year-in-cpu-only-and-all-in-one-configurations
- Autor: Jake Roach
- Publicado: 2026-10-12T13:00:00+00:00
- Score: 5.109
- Imagem: imagens/hardware-amd-debuts-helion-reference-design-for-a.jpg | crédito: Tom's Hardware | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Updated 10/12/26 at 12:01pm ET: AMD originally said the Helion rack would ship in the first half of 2027, but it has revised the release date to November 2026. We've updated the headline and featured image. We also corrected an error where OpenU trays were marked as 21mm wide instead of 21 inches wide.
AMD is bringing a new reference rack-scale design to the data center ecosystem with Helion. It’s a standardized, 21-inch rack reference design that will complement the Helios rack AMD revealed at OCP Global Summit last year. This year, we have Helion, which AMD says can house up to 32,768 Zen 6 cores in a CPU-only deployment using the dense 256-core design available with the EPYC ‘Venice’ 9996.
The rack design is standardized, based on the Open Compute Project’s ORv4 specification, which is slightly wider and taller than a standard IT rack. Helion is designed to support 44 OpenU trays, which are 21 inches wide and 48mm tall, slightly larger than a standard EA1-310 tray. AMD says the reference design supports both air-cooled and direct liquid-cooled deployments.
The design is also compliant with OCP’s DC-MHS (Data Center Modular Hardware System) standard. MHS is designed to bring “interoperability between key elements of data center, edge, and enterprise infrastructure,” according to OCP.
Although AMD has renders of the design you can see in the presentation below, it won’t actually sell racks. This is a reference design that AMD is contributing to OCP, and OEMs and ODMs will actually bring that design to market. AMD didn’t share partners supporting Helion during a pre-briefing with the press. The company says CEO Lisa Su will announce partners during the lead keynote at the OCP Global Summit later today.
AMD also didn’t share deployment partners, though it suggested that Helios customers will also deploy Helion racks.
Unlike Helios, which is built for AI training and inference, Helion is a more flexible rack solution primarily focused on CPUs. In a CPU-only deployment, the design can hold up to 128 EPYC 9996 CPUs, bringing that impressive 32,768 core count per rack. This configuration would likely look something like an agentic AI sandbox system, which is then connected to an inference system.
This model for personal AI agents is in use today, both in Meta’s Muse and OpenAI Dots. Each user has a sandbox with a slice of compute from the host system, with the backbone of an inference server. Some workloads are handled on those CPU-only servers, such as building software, but the heavy-duty AI inference happens elsewhere.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
Presumably, this is the model AMD is aiming at with Helion as hyperscalers build out CPU capacity on the back of agentic AI. However, the design is flexible, supporting up to 16 MI350P GPUs and 102 Tbps of networking, though at the cost of CPU capacity. This hybrid configuration is targeted at enterprises, says AMD, giving them an all-in-one rack for data management, networking, and AI usage.
AMD says the Helion rack will be available starting in the first half of 2027, likely riding the wave of Zen 6 deployments that are expected to start ramping up later this year.
Full AMD OCP 2026 presentation
Follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.
Jake Roach is the Senior CPU Analyst at Tom’s Hardware, writing reviews, news, and features about the latest consumer and workstation processors.
- 
jp7189 said:"OpenU trays, which are 21mm wide and 48mm tall"
21mm ? Now that's dense! In reality, those trays are actually 537mmThanks for catching that! Inches, not mm. I've corrected the article. Reply
- 
jp7189 said:"OpenU trays, which are 21mm wide and 48mm tall"
21mm ? Now that's dense! In reality, those trays are actually 537mmYeah, ~19 inches is the standard rackmount chassis width. 1.75 inches (44.45 mm) is the height of a standard "rack unit". According to Wikipedia, 23 inches is another popular width.
I used to have some interest in running old, decommissioned server hardware at home. However, these machines are far too noisy, power-hungry, and expensive (even used!) for me to ever contemplate it. So, I have no personal interest in what rack form factor they use. A lot of them are now requiring liquid cooling, too. Reply
