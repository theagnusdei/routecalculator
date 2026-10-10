# We tested gaming performance in 17-year-old Windows 7 on a modern gaming PC against Windows 11

- Editoria: Computadores Pessoais (`computadores_pessoais`)
- Fonte: Tom's Hardware — https://www.tomshardware.com/software/windows/we-tested-gaming-performance-in-17-year-old-windows-7-against-windows-11-on-a-modern-gaming-pc-older-operating-system-delivers-advantages-in-some-scenarios
- Autor: Dan Mateescu
- Publicado: 2026-10-10T13:40:00+00:00
- Score: 5.51
- Imagem: imagens/computadores_pessoais-we-tested-gaming-performance-in-17-year.jpg | crédito: Tom's Hardware | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

After the rough reception of Windows Vista, Windows 7 launched in 2009 to largely positive reviews. Even 17 years later, it remains one of the most beloved versions of Windows ever released. But how does this nearly two-decade-old operating system hold up on modern hardware? We managed to install Windows 7 on a modern PC and put it to the test across eight DirectX 11 games and two DirectX 9 titles to see how its gaming performance compares to Windows 11 today. Surprisingly, Windows 7 still carves out many notable wins over its successor.
At launch, Windows 7 was very similar to Windows Vista in many respects. Vista had introduced significant changes under the hood compared to Windows XP, including technologies such as SuperFetch, ReadyBoost, ReadyDrive, new asynchronous APIs, and other I/O improvements. It also introduced native processor power management and various memory-management enhancements. On the visual side, Vista was the first version of Windows to feature Windows Aero, with its distinctive glass-like window borders.
Windows 7 retained many of these underlying technologies while addressing several of Vista’s biggest criticisms. One notable improvement was greater control over User Account Control (UAC), allowing users to adjust how frequently they received UAC prompts. In Vista, these prompts could appear far too often, becoming a major source of frustration for many users.
Windows 7 also benefited from something that had nothing to do with the operating system itself: more powerful hardware. When Vista launched, many mid-range and budget PCs struggled to deliver smooth performance, particularly when using more demanding visual features such as Windows Aero. By 2009, however, PC hardware had advanced considerably, and the performance required to run these features smoothly was no longer a significant concern for most users.
The Challenge of Running Windows 7 on a Modern PC
Getting Windows 7 running on modern hardware is not as straightforward as installing a current version of Windows. At 17 years old, the operating system predates many of the technologies used by modern PCs, meaning driver support is extremely limited. For example, Windows 7 does not include native NVMe or USB 3.0 support, so the necessary drivers have to be slipstreamed into the installation ISO. Microsoft did eventually release patches that added NVMe support, but without injecting the appropriate drivers into the ISO, the Windows 7 installer will not recognize an NVMe drive.
Our system is based on AMD’s AM5 platform (with the full system specifications detailed later in the article), which presents another limitation: there are no official Windows 7 chipset drivers for the platform.
Fortunately, we are using an RDNA 2 GPU, which does have Windows 7 driver support, allowing us to use a relatively modern graphics card for our testing.
Get Tom's Hardware's best news and in-depth reviews, straight to your inbox.
The motherboard is also an important consideration. Modern motherboards that have dropped CSM (Compatibility Support Module) and legacy boot support can make installing Windows 7 considerably more difficult, and in some cases may prevent the operating system from booting altogether. Fortunately, our motherboard still supports CSM, so this was not an issue for our setup.
Test System
Windows 7 system specs
- AMD Radeon RX 6950 XT
- Ryzen 7 9800X3D
- 64GB (2x32GB) G.SKILL Flare X5 DDR5 @6000 MHz CL30
- Seagate Lightsaber FireCuda (530) NVMe SSD
- ASUS ROG STRIX B850-F Gaming WiFi
- Corsair Nautilus 360 RS AIO Cooler
- HAGS not supported by driver
- Windows 7 Ultimate 64-bit Service Pack 1 (Build 7601)
- AMD Adrenalin 22.6.1 for Windows 7 (2022)
Windows 11 system specs
- AMD Radeon RX 6950 XT
- Ryzen 7 9800X3D
- 64GB (2x32GB) G.SKILL Flare X5 DDR5 @6000 MHz CL30
- Seagate Lightsaber FireCuda (530) NVMe SSD
- ASUS ROG STRIX B850-F Gaming WiFi
- Corsair Nautilus 360 RS AIO Cooler
- HAGS not supported by driver
- Windows 11 25H2 (Build 26200.9278)
- AMD Adrenalin 22.6.1 for Windows 11 (2022)
For Windows 7, we disabled Secure Boot, enabled CSM, and set Boot Device Control to Legacy OPROM Only. Enabling CSM means that we no longer have access to Resizable BAR (it's not supported anyway). For Windows 11, we disabled VBS (Virtualization-Based Security) and HVCI (Hypervisor-Protected Code Integrity).
It is important to note that while we used Adrenalin 22.6.1 for both Windows 11 and Windows 7 testing, the two packages contain different internal driver versions. Although both packages were released in June 2022, the Windows 11 driver is based on a more advanced codebase than the Windows 7 driver.
In both cases, we performed a clean install of each operating system and filled the SSD to about 50-60%.
Performance Testing
We tested ten games in total: eight using DirectX 11 and two using DirectX 9. The DirectX 11 titles are the primary focus, as both systems support them natively. By comparison, our Windows 11 system will run DirectX 9 games through the D3D9On12 mapping layer, while our Windows 7 system will run them natively. There are ways to get around the use of D3D9On12 on Windows 11, but we want to evaluate the out-of-the-box experience that most gamers would encounter. As a result, we expect Windows 7 to have an advantage in the DirectX 9 titles.
It will become apparent in the results below that the advantages of each operating system will vary depending on whether we are CPU-limited or GPU-limited.
Metro 2033 Redux (DX11)
Metro 2033 Redux was released in 2014 and features a new lighting engine, higher visual fidelity, and new locations for certain levels. The game is predominantly GPU-bound, but there are moments when GPU utilization drops sharply as you traverse the game world. At these points, the CPU becomes the limiting factor, resulting in a corresponding drop in performance.
Although Windows 11 delivers a higher average frame rate, Windows 7 handles the CPU-related performance drops much better, resulting in significantly stronger 1% lows. Installing the AMD chipset drivers and enabling Resizable BAR improves 1% lows on Windows 11 slightly, but it still falls well behind Windows 7.
Windows 11’s more advanced graphics driver appears to provide an advantage in GPU-limited scenarios, while Windows 7’s lower CPU overhead offers more consistent frame pacing, though with lower peak performance.
Batman: Arkham Origins (DX11)
Batman: Arkham Origins runs on a modified version of Unreal Engine 3 and uses several DX11 enhancements such as Tessellation, Ambient Occlusion HBAO+, Percentage Closer Soft Shadows (PCSS), and Depth of Field (DoF).
When CPU-limited at 1080p, Windows 7 once again puts in a strong showing, outperforming Windows 11 in both average frame rate and 1% lows. Surprisingly, Windows 7 also comes out ahead at 4K in Origins, though with a far smaller advantage. As we will see throughout the remainder of our testing, however, this is a rare occurrence. Even so, Windows 7 maintains a slight performance advantage over Windows 11 at 4K in this title.
Batman: Arkham Knight (DX11)
Batman: Arkham Knight was both a critical and commercial success, despite a notoriously troubled PC launch plagued by severe bugs and major performance issues. Visually, however, the game still holds up remarkably well, and modern hardware is more than capable of brute-forcing this demanding PC port.
Windows 7 again delivers higher performance at 1080p when we are CPU-limited. Windows 11 jumps ahead when we become GPU-limited at 1440p and 4K.
Batman: Arkham City (DX11)
Batman: Arkham City was the second entry in the series, following Arkham Asylum, and the first to support DirectX 11. This introduced features such as tessellation, which adds greater geometric detail to characters and environments.
In Arkham City, our system is GPU-bound at every resolution tested, giving Windows 11 the advantage across the board.
The Witcher 3: Wild Hunt (DX11)
The Witcher 3 faced some controversy at launch over reductions in image quality compared to its initial reveal. CD Projekt Red quickly released a patch addressing these concerns and improving the game’s visuals. From a performance perspective, however, the game was extremely demanding at launch.
While the game is very GPU bound in general, at 1080p we did encounter a slight CPU bottleneck, which gave Windows 7 an advantage in 1% lows. At 1440p and 4K, Windows 11 takes a slight lead.
Control (DX11)
Control is the newest title we tested for this comparison, having launched in 2019. While the game introduced several ray tracing features, these were exclusive to the DirectX 12 API. Since Windows 7 does not support DirectX 12, we tested Control using DirectX 11 on both operating systems. Even without ray tracing, Control remains the most graphically advanced title in our Windows 11 vs Windows 7 comparison.
Windows 11 wins across the board. This is not a surprise, as we are GPU-limited across all resolutions tested.
Hitman: Absolution (DX11)
Hitman: Absolution was released in 2012 and was the first game to use the Glacier 2 engine. The updated engine could handle crowds of up to 1200 characters, which was unprecedented at the time. The game also featured several DirectX 11 enhancements, including global illumination and tessellation.
This is another game that pushes the GPU hard, regardless of resolution. Our test system was GPU-limited even at 1080p.
Hitman 2 (DX11)
Hitman 2 was released in 2018, making it the second-newest game in our operating system comparison. It features detailed environments, dense crowds, and full reflections across many surfaces, making it an impressive-looking title overall.
Hitman 2 is another example where our test system is GPU-limited at every resolution, giving Windows 11 a clean sweep across the board.
Batman: Arkham Asylum (DX9)
We now move to our first DirectX 9 game. As previously mentioned, Windows 7 should have an advantage here because our Windows 11 system must use the D3D9On12 mapping layer for DirectX 11 games. But just how much of an advantage?
Significant advantages for Windows 7 in average frame rate and 1% lows, especially at 1080p and 1440p. The advantage is reduced at 4K, but the performance is still smoother overall in Windows 7. Another translation layer, such as DXVK, may close the gap.
Borderlands 2 (DX9)
Borderlands 2 is our second DirectX 9 game and the final overall game tested.
Once again, another massive win for Windows 7 at the lower resolutions. The performance at 4K is virtually identical.
Bottom Line
Windows 11 is optimized for GPU-hungry games
The results are interesting, but perhaps not entirely surprising. The DirectX 9 results are largely in line with our expectations, given that Windows 11 must run these games through the D3D9On12 mapping layer, yielding substantial advantages for Windows 7.
The DirectX 11 results are more nuanced, but a clear trend emerges: Windows 7 has the advantage when we are CPU-limited, while Windows 11 performs better when we are GPU-limited. This makes sense given that Windows 11 uses graphics drivers built on a more advanced codebase, while Windows 7 is a leaner operating system with fewer background processes and, consequently, lower CPU overhead.
Microsoft has recently detailed its K2 plan, which aims to improve the performance and reliability of Windows 11. We hope these continued efforts to improve Windows 11 pay off.
The lower CPU performance we observed in Windows 11 cannot be attributed to its most notable security features, such as VBS (Virtualization-Based Security) and HVCI (Hypervisor-Protected Code Integrity), as we disabled both during testing. Notably, Windows 7 does not support VBS or HVCI at the software level, while Windows 11 supports hardware virtualization extensions (such as Intel VT-x or AMD-V) and Second Level Address Translation (SLAT). Additionally, fixed-function hardware can reduce the impact of virtualization to varying degrees, based on the CPU architecture's capabilities. However, additional telemetry and other background services still pop up and use precious CPU cycles.
Using the latest chipset drivers and enabling features such as Resizable BAR does not help Windows 11 close the gap in CPU-limited scenarios by any significant margin. Ultimately, we would like to see Windows 11 become leaner and more efficient, as our results suggest there is still some performance left on the table, particularly on the CPU side.
Dan Mateescu is a PC enthusiast with many years of experience benchmarking PC hardware. In 2021, he started his own YouTube channel called 'Compusemble' where he benchmarks hardware in video games and the latest tech demos.
- 
Since people cannot always afford 64GB of memory at the insane prices,
This test would have been more interesting constrained to 16GB or otherwise somehow constrained to a slightly unusual 24GB since Win7 hogs less memory. Or at least, dual-test with both memory options and the same slate of games.(Test1: 64GB/Test2: 16GB) Reply
- 
ezst036 said:Since people cannot always afford 64GB of memory at the insane prices,
This test would have been more interesting constrained to 16GB or otherwise somehow constrained to a slightly unusual 24GB since Win7 hogs less memory.The idea was to remove any hardware issues, and concentrate on the OS differences.
Reducing it to 16GB could easily show difference in game performance due to the RAM, not the OS. Reply
- 
USAFRet said:The idea was to remove any hardware issues, and concentrate on the OS differences.
Reducing it to 16GB could easily show difference in game performance due to the RAM, not the OS.
Reducing available memory would allow to see differences in memory management by the OS and the amount of memory used for internal OS purposes. Both very important, as differences in computational game performance are likely largely due to GPU drivers. Reply
- 
qxp said:Reducing available memory would allow to see differences in memory management by the OS and the amount of memory used for internal OS purposes. Both very important, as differences in computational game performance are likely largely due to GPU drivers.Both methods have their advantages and disadvantages. Reply
