# Your SSD might be lying about its storage capacity. Here’s how to check

- Editoria: Computadores Pessoais (`computadores_pessoais`)
- Fonte: PCWorld — https://www.pcworld.com/article/3251958/your-ssd-might-be-lying-about-its-storage-capacity-heres-how-to-check.html
- Autor: Friedrich Stiemer
- Publicado: 2026-10-12T14:30:00+00:00
- Score: 5.236
- Imagem: imagens/computadores_pessoais-your-ssd-might-be-lying-about-its-storag.jpg | crédito: PCWorld | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

If you buy an external SSD or a USB stick today that’s being offered at a bargain price with astronomical storage capacities, you should be rather skeptical. The reason: The market is currently being flooded with sophisticated counterfeit storage devices.
Manipulated controller firmware can trick the operating system into believing the device has more capacity than physically exists. Here’s an example: Imagine you’ve bought a supposed 4TB SSD on a well-known online platform and your Windows Explorer also displays this capacity.
In reality, however, the drive contains only a comparatively tiny 64GB chip. The insidious thing about this manipulation is that the controller has been programmed to appear to acknowledge write operations successfully, even when the physical storage has long since been exhausted.
Samsung
As soon as the actual capacity is exceeded, the drive either starts overwriting the oldest data at the beginning of the storage or simply dumps new data packets into a digital black hole, while the file system continues to report an intact structure.
The rude awakening usually only sets in weeks later, when you try to open your supposedly backed-up holiday photos or documents. Instead of the content, you’ll only get error messages or find corrupted file fragments. We must make this absolutely clear: The operating system is not a reliable indicator of a drive’s integrity.
It merely retrieves the information provided by the controller. And in this case, the controller has been tampered with. To expose these deceptions, you need tools that scrutinize every single bit. You should therefore check every new drive immediately upon receipt using the Validrive tool: Launch the program with administrator rights and select ‘Check USB Drive.’
Foundry
Now insert the storage device and allow the program to recognize it. Click on ‘Validate THIS drive’ to start the check. The tool carries out a quick, targeted check by writing to random sectors across the entire declared range and reading them back immediately.
As Validrive measures and analyzes access times during this process, it is able to determine very quickly whether there is actually a physical cell behind a logical address, or whether the controller is simply suppressing an error message.
