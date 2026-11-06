# Valve escaped Windows. Now Steam is breaking free from the PC itself

- Editoria: Computadores Pessoais (`computadores_pessoais`)
- Fonte: PCWorld — https://www.pcworld.com/article/3266419/valve-escaped-windows-now-steam-is-breaking-free-from-the-pc-itself.html
- Autor: Brad Chacos
- Publicado: 2026-11-06T14:00:00+00:00
- Score: 5.903
- Imagem: imagens/computadores_pessoais-valve-escaped-windows-now-steam-is-break.jpg | crédito: PCWorld | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Valve spent the last decade making Windows optional for PC gaming. Now it wants to do the same thing to x86 — the Intel- and AMD-based CPU architecture at the heart of every gaming PC. If it succeeds, the resulting shake-up could change what “PC game” even means.
The Steam Deck proved Valve’s Proton compatibility layer could run an enormous library of Windows games on Linux without developers needing to port them to Linux first. That breakthrough helped make the Steam Deck a success. It also made Linux gaming legitimately viable, and laid the groundwork for SteamOS to spread to other PCs.
But the Steam Frame reveals that Valve’s ambitions go much deeper. The standalone VR headset runs SteamOS on a Qualcomm Snapdragon 8 Gen 3 processor based on the Arm architecture, rather than the x86 processors from AMD and Intel that have powered PC gaming for decades.
And Valve expects your existing x86 Windows games to run on it anyway. That’s why the Arm chip inside Steam Frame matters so much more than VR. Valve is starting to dismantle the fundamental assumptions about which hardware and software a gaming PC needs to run your games.
The writing is on the wall. We’re looking at the endgame for everything Valve has been building with SteamOS, Proton, Steam Deck, and now Steam Frame: Buy anywhere, play anywhere. Your Steam library won’t care what operating system you’re using, what processor architecture sits inside your device, or, eventually, even what type of device you’re holding. As long as you’ve got enough compute and graphics horsepower to run the game, Steam will figure out the rest.
And that would be a true game-changer. Buckle up.
Hi! I’m Brad, PCWorld’s executive editor. Want to get more hard-hitting journalism like this wherever you are? Sign up for PCWorld’s Full Nerd and Boost Mode newsletters for PC enthusiasts, and be sure to subscribe to PCWorld on YouTube and all the usual social channels. Welcome to the PCWorld family!
First Valve made Windows optional
The Steam Deck’s software magic is easy to take for granted now, but it’s worth revisiting how crazy its basic premise once sounded.
Most PC games are Windows games. Valve didn’t solve that problem by convincing thousands of developers to create and maintain native Linux versions. It built Proton to let the Windows versions run on Linux instead.
There’s a lot happening under Proton’s hood. It’s built around Wine, while components like DXVK translate DirectX graphics calls into Vulkan. The important bit is that all this happens underneath the game. Developers can keep shipping Windows games. Gamers can keep buying Windows games. Valve resolves the incompatibility.
That strategy didn’t start with Steam Deck. Valve’s push toward Linux began in earnest during the Windows 8 era, when Microsoft’s Windows Store and its increasingly locked-down approach to computing convinced Gabe Newell that Valve needed an escape hatch. The original SteamOS and Steam Machines last decade were that hedge. They failed as products, but Valve never abandoned the underlying work.
Proton eventually attacked the fatal chicken-and-egg problem that helped doom Steam Machines: Gamers wouldn’t switch to Linux because their Windows games weren’t there, while developers wouldn’t support Linux because the gamers weren’t there.
So Valve stopped asking developers to port their games.
Instead of demanding that the PC gaming ecosystem bend around SteamOS, Valve bent SteamOS around the PC gaming ecosystem. Steam Deck was the culmination of that decade-long push toward independence.
Willis Lai/Foundry
Omdia analyst James McWhirter traces Valve’s strategy back to exactly the same place. “The very first 2013 release of SteamOS and Steam Machines were a hedge against Windows 8 sidelining the old Win32 framework by which so many games depended on,” McWhirter told me via email.
Much has changed since then, he said, but “the spirit of SteamOS, giving Valve more control of its own destiny, has remained a key constant.” And now Steam Frame takes the same idea one layer deeper.
Now Valve is making x86 optional
Steam Frame doesn’t just have an operating-system compatibility problem. Its Snapdragon processor speaks a fundamentally different language than the x86 code compiled for traditional gaming PCs.
That’s where FEX comes in.
Valve
FEX translates x86 code into Arm64 instructions that the Snapdragon processor can understand. Stack it together with Proton and something kind of bonkers becomes possible: You can take an x86 game compiled for Windows and run it on an Arm processor running Linux.
But Valve isn’t simply emulating an entire x86 Windows PC and hoping for the best. “When provided with a proper ARM execution environment, such as when integrated with Proton ARM, FEX only translates the CPU code of the application,” Valve software engineer Pierre-Loup Griffais told me via email.
That’s a crucial distinction. Proton itself, the operating system, and graphics drivers can execute natively on Arm. Griffais says Proton crosses over at the Win32 API boundary, meaning “no Proton, OS or graphics driver code requires translation.” FEX primarily has to deal with the game’s own CPU code.
“The FEX translation overhead is only on the game’s own CPU code and is typically pretty modest,” Griffais said. “For a typical GPU-bound game, our aim is that the output performance would be similar to running the game on a similarly powerful GPU without CPU translation.”
Foundry
That’s the technical detail that makes the bigger idea possible. Valve hasn’t made processor architecture irrelevant. It’s trying to turn architecture from a compatibility veto into a performance tradeoff.
That’s essentially the same trick Proton pulled on Windows. Valve doesn’t need the underlying technology to disappear. It just needs it to stop being something that can dictate where your Steam library runs.
Griffais says that if an Arm chip offers enough of a performance-per-watt advantage at a given power envelope, it could become a viable SteamOS gaming chip “even with FEX translation overhead in the picture.” There are still catches, which we’ll get to later. But those catches are increasingly questions about how well a game runs rather than whether x86 Windows software can run at all.
Valve has been here before
Getting software to technically run isn’t enough. Translation has to feel invisible, too.
“FEX code caching is vital for frame time consistency,” Griffais said, and Valve plans to integrate it with Steam Pre-Caching so translated code can eventually be ready before you launch a game. It’s the sort of deeply boring engineering work that separates getting Doom to boot on a weird processor from making translated games actually feel native.
And Valve has been doing that work for a long time.
For FEX, Griffais said, the challenge was getting it ready to run modern games with minimal performance loss. “It’s a fairly binary threshold to hit, but it took nearly a decade to get there,” he said.
Meanwhile, Arm chips were becoming faster and adding CPU and GPU features better suited to PC gaming. Valve’s early FEX work helped inform that process through conversations with chip vendors about what Valve wanted from the hardware.
“Timing-wise, FEX readiness and availability of ARM chips powerful enough to play the latest PC games ended up hitting at around the same time,” Griffais said.
We’ve seen this movie before. Proton took years of mostly invisible compatibility work before Valve could build a Steam Deck around it. FEX followed a remarkably similar path before surfacing inside Steam Frame. Valve keeps doing the hard compatibility work first, then building new hardware around the freedom it creates.
Don’t port your game. Steam will figure it out
All this compatibility work raises an obvious question: What does Valve actually want game developers to do about this new world of Windows, Linux, x86, Arm, and Android?
Not much, actually. Valve’s guidance to developers is revealing.
Steam Frame can run native Arm Linux software. Valve also created Lepton, a containerized compatibility layer for Android games. But for most PC developers, Valve isn’t asking for another bespoke version of their game. 
Valve
Valve says most developers can support Steam Frame by simply running their existing Windows x86 version through Proton and FEX. Proton handles Windows. FEX handles x86. SteamOS handles the rest.
Steam Frame can therefore accommodate Windows x86 games through Proton and FEX, Linux x86 games through FEX, Android Arm software through Lepton, and native Arm software directly. That’s the bigger point: SteamOS is increasingly becoming an abstraction layer between the games in your Steam library and whatever hardware happens to sit underneath it.
Valve isn’t betting that Arm replaces x86 or Linux replaces Windows. It’s building Steam so it doesn’t have to care what replaces what. You can just play your games.
Proton didn’t require Windows to lose. It made Windows less important to Valve. FEX doesn’t require x86 to lose. It just makes x86 less important to Valve.
Arm could change what a Steam PC looks like
Arm is the big wildcard, and that’s where hardware possibilities get interesting. The interesting part isn’t merely swapping one CPU architecture for another. It’s what becomes possible if Arm’s performance-per-watt strengths survive the translation layer.
Hannah Cowton-Barnes / Foundry
McWhirter points to Nintendo’s Switch 2. The system’s Nvidia Arm SoC consumes around 6 watts in handheld mode, with total system power around 10 watts, while AI technologies like DLSS help it deliver graphical fidelity far beyond what those power figures might suggest.
PC handhelds generally live much higher on the power curve, often around 15 to 35 watts. That means bigger batteries, more cooling, more weight, and thicker devices.
Arm doesn’t automatically fix that, and Steam Frame certainly doesn’t prove it will. But if FEX makes translation cheap enough while Arm silicon provides a meaningful efficiency advantage, the design space for SteamOS hardware gets a lot more interesting.
“The result is we’ll see more form factors unlocked for SteamOS devices,” McWhirter said.
Handhelds are obvious SteamOS targets, but so are laptops, mini PCs, living-room boxes, and maybe even devices we haven’t even considered yet. Qualcomm’s involvement matters beyond its processor, too: McWhirter notes that the company is contributing to the open-source Mesa graphics stack, attacking another major barrier to Arm PC gaming.
Mark Hachman / Foundry
Valve still needs other silicon vendors and PC manufacturers to buy in. McWhirter thinks Nvidia could be a particularly important tipping point, and the recent debut of RTX Spark laptops shows its interest in this space. And Arm systems won’t get a free pass simply for being efficient; they still need to compete against increasingly potent x86 hardware on performance, price, and margins.
But that’s the whole point. If Valve’s compatibility work succeeds, Arm versus x86 becomes a hardware competition rather than a library-compatibility decision.
That’s great news for gamers. Once processor architecture stops dictating which games you can play, chipmakers have to compete on performance, battery life, thermals, form factor, and price. Arm won’t automatically deliver better gaming PCs, but giving manufacturers more viable hardware choices should put some welcome pressure on AMD and Intel, too.
Steam Deck helps from the other direction
FEX can’t magically make an underpowered GPU run a game that needs dramatically more horsepower. Fortunately for Valve, PC games are already becoming accustomed to scaling down.
Steam Deck contributes to that. Omdia’s 2026 Game Developer Collective survey found 34 percent of developers said handheld gaming PCs have had a major or minor influence on their games’ design. Developers routinely optimize around the Deck, and some games ship with dedicated Deck presets.
My first instinct was to see a Valve-specific flywheel here: More lower-powered Steam devices give developers more reason to make games scale down; more scalable games make more lower-powered Steam hardware viable.
McWhirter thinks that’s overstating Valve’s role, and I think he’s right.
Chris Hoffman / Foundry
Nintendo already spent years convincing publishers to target the modest original Switch. Switch 2 provides another incentive. Digital distribution has also made everything from indies to decade-old games commercially relevant alongside new AAA blockbusters.
But that actually reinforces the broader opportunity for Valve. It doesn’t need every new triple-A game to run beautifully on every conceivable SteamOS device. It simply needs enough of your existing Steam backlog to work.
Steam already contains thousands of excellent games that don’t demand cutting-edge silicon. As that library becomes more portable across operating systems and processor architectures, manufacturers can potentially build Steam devices around different performance targets rather than one ever-escalating definition of a “gaming PC.”
The harder problem may become telling players which games fit which devices—a problem Valve has already started tackling with Deck Verified and Steam Frame’s verification program.
The walls haven’t disappeared
Anti-cheat remains an annoying bastard despite recent improvements.
The software that publishers use to detect and block cheating is deeply intertwined with the operating system, and McWhirter calls it the biggest barrier to SteamOS expanding beyond traditional Windows gaming PCs. Valve has made strides with BattlEye and Easy Anti-Cheat, but publisher-specific systems such as EA’s Javelin and Activision’s Ricochet remain unsupported.
Valve can engineer around Windows APIs and x86 instructions. It can’t unilaterally make somebody else’s anti-cheat stack support an environment they don’t want to support.
Activision
Griffais flags the same issue for Arm. GPUs remain another constraint, as do memory, battery life, price, and plain old horsepower. Software abstraction doesn’t cancel out physics.
Nor does every form factor make sense for every PC game. McWhirter points to triple-A gaming’s struggles on smartphones: controller requirements, limited storage, and games designed for sustained attention don’t disappear merely because the software technically runs. “Play anywhere” doesn’t mean Cyberpunk will run on a toaster.
Buy anywhere, play anywhere
Put all these pieces together and Valve’s trajectory becomes hard to miss.
Steam has always been obsessed with removing friction. Gabe Newell famously argued that piracy was “almost always a service problem and not a pricing problem.” More than two decades later, Valve is applying that same instinct to the boundaries around your game library.
Steam started life as a Windows-based store selling Windows-based games for x86 PCs. Microsoft’s locked-down Windows Store ambitions during the Windows 8 era showed Valve the danger of building that business on assumptions controlled by somebody else. SteamOS gave it an escape hatch. Proton weakened the Windows requirement. Steam Deck proved the approach could underpin an entirely new class of gaming PC. FEX now attacks the x86 requirement. Lepton pulls Android software into the fold.
Every step removes another assumption about what a Steam gaming device needs to be.
Valve doesn’t need SteamOS to replace Windows or Arm to replace x86. Its prize is more fundamental: a Steam library that survives whatever happens underneath it. And that should ultimately be good for us, The Gamers. The best version of this future isn’t one where Arm defeats x86 or SteamOS defeats Windows. It’s one where those choices stop deciding which games you get to play.
That’s why the Arm chip inside Steam Frame matters so much more than VR. Valve isn’t just building another headset. It’s spending years—sometimes a decade at a time—systematically removing dependencies out of Steam itself.
Buy anywhere. Play anywhere. Just bring enough hardware.
Hi! It’s Brad again, once more asking whether you want to get hard-hitting journalism like this wherever you are? Sign up for PCWorld’s Full Nerd and Boost Mode newsletters for PC enthusiasts, and be sure to subscribe to PCWorld on YouTube and all the usual social channels.
