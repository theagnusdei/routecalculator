# Vírus no Brasil usa ferramentas autênticas do Windows e o VLC para invadir conta bancária

- Editoria: Cibersegurança (`ciberseguranca`)
- Fonte: Canaltech — https://canaltech.com.br/seguranca/virus-no-brasil-usa-ferramentas-autenticas-do-windows-e-o-vlc-para-invadir-conta-bancaria/
- Autor: André Lourenti Magalhães
- Publicado: 2026-10-27T13:10:04+00:00
- Score: 4.859
- Imagem: imagens/ciberseguranca-virus-no-brasil-usa-ferramentas-autentic.jpg | crédito: Canaltech | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Vírus no Brasil usa ferramentas autênticas do Windows e o VLC para invadir conta bancária
Por André Lourenti Magalhães • Editado por Jones Oliveira |
A empresa de cibersegurança WatchGuard identificou um malware que usa elementos legítimos do Windows e arquivos executáveis de programas reais para invadir computadores de vítimas. No Brasil, o golpe começa a partir de e-mails falsos sobre cobranças de cartórios.
As tentativas de phishing levam as vítimas a sites fraudulentos e induzem ao download de scripts VBScript maliciosos. Os arquivos também podem usar uma técnica para distribuir um diretório malicioso dentro de um arquivo executável legítimo do Windows.
A pesquisa identificou a técnica em arquivos como ngentask.exe, do Microsoft .NET Framework, e vlc.exe, do famoso reprodutor de mídia VLC. Ambos se passam como executáveis legítimos para instalar um programa no Windows, mas estão corrompidos.
O script se conecta com um trojan chamado Overlord RAT, no qual é possível controlar o computador remotamente após instalar um vírus no sistema.
A análise de código da ameaça registrou algumas verificações de referências a apps de bancos e instituições financeiras brasileiras. Os dados indicam que a execução do malware pode considerar referências que miram esses serviços, mas não há evidências de invasão ou roubo de dados de clientes.
Malwares também miram contas bancárias
O relatório da WatchGuard também identificou campanhas de malware em Portugal. Uma delas envolve o trojan bancário Lampion, usado para invadir contas em serviços financeiros.
Os arquivos fraudulentos também usam elementos legítimos do Windows, como arquivos DLL, em tentativa de burlar o monitoramento do Microsoft Defender.
Para evitar ser vítima nesse tipo de golpe, é muito importante desconfiar de mensagens muito alarmantes, principalmente aquelas com arquivos anexados. Evite fazer o download e mantenha sempre um antivírus atualizado.
