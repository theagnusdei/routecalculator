# The Async Multiprocessing Has Sound Foundations in Linux, But Further Testing Is Needed

- Editoria: Software (`software`)
- Fonte: InfoQ — https://www.infoq.com/news/2026/10/linux-amp-analysis/?utm_campaign=infoq_content&utm_source=infoq&utm_medium=feed&utm_term=global
- Autor: Olimpiu Pop
- Publicado: 2026-10-07T16:16:00+00:00
- Score: 5.174
- Imagem: imagens/software-the-async-multiprocessing-has-sound-foun.jpg | crédito: InfoQ | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

At Embedded Linux Conference Europe 2026, Wolfram Sang, a Linux kernel developer and maintainer of the Linux I2C subsystem, examined the Linux building blocks for asymmetric multiprocessing (AMP). His assessment: they are sound enough to build on, but thin contributor coverage and fragmented testing need attention.
His talk drew on an attempt to upstream a hardware-spinlock driver, work that led him to examine the health of the wider AMP stack. He focused on the Linux side, pointing attendees to other conference talks for Zephyr, trusted firmware and device-tree details.
In a basic AMP system, Linux application CPUs and a smaller real-time core run within the same system-on-chip. A mailbox signals that information is available; shared SRAM or DDR holds the data. More complex systems must also coordinate ownership of shared resources. Sang described SCMI as a way for Linux to communicate with a dedicated system-control processor about resources such as clocks, rather than managing every resource alone.
That communication is less straightforward than a mailbox diagram suggests. A doorbell typically signals in one direction. Sang showed how two unidirectional mailboxes can form one request-and-response channel, while a fully bidirectional SCMI arrangement can require four. Firmware may impose a different arrangement: in his Keystone example, the existing firmware used two unidirectional mailboxes for bidirectional SCMI communication, leaving no equivalent acknowledgement path for a notification.
Other layers serve different purposes. remoteproc loads firmware and starts or stops a remote core; its firmware binary can describe the resources it needs. Given shared memory and a driver callback that "kicks" the other side, it can enable RPMsg messaging. Virtio defines an open communication standard using shared-memory virtqueues, with notifications when work is available. Sang distinguished RPMsg, which communicates between processors, from the proposed virtio-over-message transport, which would carry virtio traffic over a message channel and is not yet upstream.
Sang’s subsystem survey found remoteproc core commits growing from 175 at Linux 5.0 to roughly 1,550, though growth slowed after an earlier surge. Mailbox commits and drivers grew more recently, but only about four authors had contributed more than five patches. Hardware spinlocks stood out: core commits rose from 19 to 30 over roughly seven years, while the driver count remained largely flat. Sang did not conclude these components were broken; he called for more reviewers and testers.
His spinlock-driver work illustrated the maintenance burden: a seemingly small change expanded into header and lifecycle questions, while a proposed debugging improvement ran into a deprecated API. Testing could also require modified firmware and U-Boot merely to exercise a driver. OpenAMP provides build instructions and test cases, but its examples do not yet run uniformly across supported boards. For Sang, reducing that friction is key to sustaining the more ambitious AMP systems now being built.
