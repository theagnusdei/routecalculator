# Your 4TB SSD probably has the wrong cluster size for large files

- Editoria: Computadores Pessoais (`computadores_pessoais`)
- Fonte: PCWorld — https://www.pcworld.com/article/3229547/your-4tb-ssd-probably-has-the-wrong-cluster-size-for-large-files.html
- Autor: Friedrich Stiemer
- Publicado: 2026-10-14T14:30:00+00:00
- Score: 5.697
- Imagem: imagens/computadores_pessoais-your-4tb-ssd-probably-has-the-wrong-clus.jpg | crédito: PCWorld | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

In an age of 4TB SSDs and massive NVMe drives, many users tend to leave the entire storage space as a single, huge system drive. While this is convenient, from an administrative point of view it is a risky move that amounts to flying blind. Instead, we recommend strategically partitioning your largest drives.
This brings tangible benefits for data security, system recovery, and backup efficiency. Think of partitions as digital firewalls within your hardware. If your operating system becomes corrupted by a faulty driver, a failed update, or even malware, a clean reinstallation is often the quickest way back to a stable system.
However, if you’ve stored everything on a single partition, you’ll have to laboriously back up terabytes of data before reinstalling, or risk losing it when formatting the drive.
By separating the operating system onto partition C: and your user data onto partition D:, you can completely wipe and reinstall Windows, while your game collections, video projects, and documents on the second partition remain completely untouched. This not only saves time but also spares you a lot of stress in crisis situations.
Kingston
To implement this optimization, you must first analyze your current configuration. To do this, open the Command Prompt with administrator rights and enter the command fsutil fsinfo ntfsinfo C:, then press the Enter key to confirm. Look for the value ‘Bytes per cluster’ in the results.
By default, Windows uses 4KB, which is ideal for the system partition to minimize fragmentation when dealing with many small system files. However, for data-only partitions where you mainly store large files such as 4K videos or backups, it makes sense to adjust the cluster size to 64KB.
Here’s how to do it: The neatest way to change the cluster size in Windows 11 is via Windows Settings. Press the Windows + I key combination to open Settings. In the left-hand menu, navigate to ‘System’ and then click on ‘Storage’ on the right. Scroll down to the ‘Storage management’ section.
Foundry
Next, expand ‘Advanced storage settings’ and select ‘Disks and volumes.’ A list of all physical drives will appear. Click the arrow next to your hard drive to view the associated partitions (volumes). Select the desired data partition and click the ‘Properties’ button.
Next, click the ‘Format’ button. The crucial dialog box will now open. Here, under ‘Label,’ enter a name for your drive. Ensure that ‘NTFS’ is selected under ‘File system.’ In the ‘Allocation unit size’ drop-down menu, select ‘64KB’ explicitly instead of ‘Standard (4KB).’
Tick the box next to ‘Perform quick format’ and confirm the process by clicking ‘Format.’ Please note: This process will irrevocably delete all data on this partition. You should therefore only carry it out on newly created or empty data partitions.
Foundry
This adjustment to 64KB is so effective because it reduces fragmentation in large files and minimizes the amount of metadata that needs to be managed in the Master File Table (MFT). Please bear in mind a technical limitation: With the standard cluster size of 4KB, an NTFS partition is limited to a maximum of 16TB.
If you upgrade to even larger drives in future, you must use larger clusters to be able to utilize the full capacity. On modern SSDs, you should also ensure that the partitions are aligned with the internal NAND memory.
Nowadays, Windows handles this correctly and automatically when creating partitions via Disk Management or the Settings app, in order to avoid unnecessary write cycles (write amplification).
