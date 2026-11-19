# DDR6 RAM shrinks by 44% while delivering 4 times more bandwidth than DDR5 — JEDEC previews 12.8 GT/s modules with up to 1 terabyte of capacity per slot

- Editoria: Hardware (`hardware`)
- Fonte: Tom's Hardware — https://www.tomshardware.com/pc-components/ram/ddr6-ram-shrinks-by-44-percent-while-delivering-4x-ddr5s-baseline-bandwidth-jedec-previews-12-8-gt-s-modules-with-up-to-1-terabyte-of-capacity-per-slot
- Autor: Zhiye Liu
- Publicado: 2026-11-19T10:00:00+00:00
- Score: 5.439
- Imagem: imagens/hardware-ddr6-ram-shrinks-by-44-while-delivering.jpg | crédito: Tom's Hardware | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- https://www.techspot.com/news/114629-ddr6-memory-could-44-shorter-than-ddr5-while.html

## Texto extraído

Today's best RAM will look huge compared to upcoming DDR6 memory. JEDEC has just released a preview of the DDR6 specification, confirming that next-generation memory modules will be 44% shorter than DDR5. That is only the physical aspect, though. From a performance perspective, DDR6 will debut at 12.8 GT/s, more than double DDR5's baseline transfer rate, while also quadrupling the memory bandwidth per memory module thanks to a new design.
JEDEC's DDR6 preview highlights improvements in various areas, including performance, capacity, reliability, and power efficiency. These advancements align with the upgrades DDR5 brought to the table when it launched.
One of the most notable differences is that DDR6 memory modules will measure just 74mm in length, 44% shorter than DDR5’s 133mm memory modules. This makes DDR6 only 6% longer than DDR5 SO-DIMM modules, which you commonly find in laptops and mini-PCs.
JEDEC has maintained the pin count for many years, sticking to 288 pins for DDR4 and DDR5. However, DDR6 may finally break that mould. Given the substantial reduction in length with DDR6 and the data bus width upgrade, it is reasonable to assume that DDR6 will have a completely different pinout and density. Sadly, JEDEC has not revealed the pin count for DDR6.
Early rumors suggested that DDR6 may be limited to CAMM form factors to feed the AI boom. However, JEDEC's announcement at least does not rule out other form factors. It appears JEDEC is still determining which form factors DDR6 will use. Potential options include RDIMM, UDIMM, and CAMM formats, just like DDR5.
DDR6 Specifications
Notably, JEDEC has increased the data bus width in DDR6 to 96 bits, a 50% boost over DDR5's 64 bits. The channel architecture for DDR6 will also change substantially. While DDR4 and DDR5 leveraged a single 64-bit channel and two 32-bit sub-channels, DDR6 takes a different approach. JEDEC will implement a design with four 24-bit sub-channels.
Using the baseline for comparison, DDR6 offers up to 153.6 GB/s of total module bandwidth, compared to DDR5's 38.4 GB/s. That is a 4X uplift in bandwidth. If we compare DDR5-9200 RDIMMs, which max out at 73.6 GB/s per module, with DDR6-12800 RDIMMs, the uplift is a little more than double.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
At least on the server side, DDR6 RDIMMs will start at DDR6-12800, whereas DDR5 RDIMMs topped out at DDR5-9200. JEDEC anticipates DDR6 reaching DDR6-14400 and beyond. This is for the server and enterprise market, though. It remains to be seen which DDR6 speed will launch in the consumer market. DDR5 commenced at DDR5-4800.
DDR6 may be shorter than DDR5, but it makes up for it by having 2X the bank count. This will help push higher data rates and capacities. DDR6 will support 128Gb (16GB) dies, which represents a massive leap. We are looking at 4X the density of early DDR5 memory modules. Instead of placing chips side by side on the PCB, DDR6 enables die stacking, allowing manufacturers to place multiple dies on top of each other via Through-Silicon Vias (TSVs).
Consumer DDR5 memory modules currently sit at 64GB per module, while server RDIMMs have reached 512GB. DDR6 could raise module capacity to 128GB or 256GB and potentially scale RDIMMs to 1TB or more per slot.
DDR6 has no official launch date. Many believe 2029 is a realistic target for commercialization. However, in the current state of things, it would be a miracle if DDR6 had no setbacks.
Download the Tom's Hardware app for up-to-the-minute updates on iOS and Android. Also follow Tom's Hardware on Google News, or add us as a preferred source, to get our latest news, analysis, & reviews in your feeds.
Zhiye Liu is a news editor, memory reviewer, and SSD tester at Tom’s Hardware. Although he loves everything that’s hardware, he has a soft spot for CPUs, GPUs, and RAM.
- 
If it doesn't change between now and the specification actually being published this should mean the death of SODIMMs. The last couple of generations have both been a bit under 70mm long so with this being 73mm I cannot see why it would be carried forward. The size also explains the push for better die stacking because of how much less module area is available limiting the number of packages (I don't expect to see any die stacking on client products).
On the UDIMM side of things I'm wondering if there will be any latency penalties having packages not all being next to each other. DDR5 SODIMMs of 16GB+ have two packages side by side and then two above, but all DDR5 UDIMMs have them side by side. On the topic of consumer products there's the potential that channels could be side by side length wise and not take up much more room than a single UDIMM does today.
I believe this is the first confirmation that DDR6 channels are going to be effectively 96-bit though it was expected given that LPDDR6 is. DDR6 is going to be the biggest fundamental change to socketed memory since the advent of dual channel. The base configuration, on paper, has a dual channel bandwidth of ~307GB/s which effectively doubles the best available today. This ought to mean a lot for integrated graphics and the amount of bandwidth per core as CPU core counts are increasing.
Typically we would see client products first (less validation required), but in the current market I just don't see that happening. DDR6 was also supposed to have the specification rolling out this year, but that obviously isn't happening either. I suspect next year is when it will be finalized and then it could be in enterprise as early as 2028 depending on demand and how well MRDIMMs are scaling. I'd like to see it pop up in client ASAP, but I wouldn't really bet on any earlier than end of 2029 to some time in 2030. LPDDR6 will likely hit client much earlier than DDR6 does so it will be interesting to see what sort of productization it sees.
I didn't see a link in the article here's the JEDEC preview announcement: https://www.jedec.org/news/pressreleases/jedec%C2%AE-previews-next-generation-ddr6-dram-higher-performance-greater-capacity Reply
- 
"DDR6 has no official launch date. Many believe 2029 is a realistic target for commercialization. However, in the current state of things, it would be a miracle if DDR6 had no setbacks."
There is a lot of money available to make this happen. First one out the door will make a ton of money. This is how the AI bubble pops. Reply
- 
Razzi16 said:May sound impressive, but nobody in the world will be able to afford to buy it for another 10 years!With Zen 7 likely coming to AM5, most people aren't going to be buying DDR6-capable CPUs for around 5 years.
thestryker said:The base configuration, on paper, has a dual channel bandwidth of ~307GB/s which effectively doubles the best available today. This ought to mean a lot for integrated graphics and the amount of bandwidth per core as CPU core counts are increasing.Basically double if you compare 12800 MT/s DDR6 to something crazy like this: https://www.corsair.com/us/en/explorer/diy-builder/memory/corsair-sets-new-ddr5-world-record-at-12832-mts/
If you compare to typical DDR5-6000 memory Ryzen owners are using now, it's a tripling and change. Or quadrupling from entry-level DDR5-4800, which has seen more use in the memory dark ages. Although it's possible more people will be using 8000-10000 MT/s by the end of the generation.
That's better than Gorgon Halo bandwidth in what should be the cheap trash configuration (dual-channel), so very good for our precious iGPUs. Maybe the integrated NPUs as well if those are sticking around.
If OEMs want to cheap out, they might give you single-channel, as they do now, or produce DDR6 "HUDIMM" memory, giving PCs as low as 48-bit and ~77 GB/s. Reply
- 
jabliese said:"DDR6 has no official launch date. Many believe 2029 is a realistic target for commercialization. However, in the current state of things, it would be a miracle if DDR6 had no setbacks."
There is a lot of money available to make this happen. First one out the door will make a ton of money. This is how the AI bubble pops.Yep -- DDR6 will surely become commercially available as RDIMMs for servers first and then UDIMM and CAMM later for consumers. With the massive cash reserves that the big mem makers have and pricing incentives to bring faster and higher-capacity memory to market, I don't see this being delayed. Yeah, I'm sure early availability will be limited and expensive. Reply
