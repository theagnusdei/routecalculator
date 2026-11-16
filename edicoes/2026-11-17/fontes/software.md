# Microsoft explica “apagão” que derrubou o Outlook (não foi hacker)

- Editoria: Software (`software`)
- Fonte: Tecnoblog — https://tecnoblog.net/noticias/microsoft-explica-apagao-que-derrubou-o-outlook-nao-foi-hacker/
- Autor: Emerson Alecrim
- Publicado: 2026-11-16T18:20:57+00:00
- Score: 6.108
- Imagem: imagens/software-microsoft-explica-apagao-que-derrubou-o.jpg | crédito: Mobilon Mídia LTDA | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- https://canaltech.com.br/software/apagao-da-microsoft-empresa-explica-os-3-erros-que-derrubaram-80-dos-servidores/

## Texto extraído

Resumo IA
- A Microsoft informou que o “apagão” que afetou o Outlook e outros serviços da empresa na semana passada foi causado por uma falha em uma atualização de software (e não por um ataque hacker).
- A falha ocorreu em uma atualização aplicada em julho em servidores de “gateway de rede” ligados ao Microsoft 365, que controla o acesso aos serviços da empresa.
- A Microsoft reconheceu que os testes pós-atualização não foram executados corretamente, o que permitiu que a falha passasse despercebida até que uma sequência de acontecimentos criasse o cenário perfeito para que ela se manifestasse.
O “apagão” que a Microsoft sofreu na última semana, que manteve o Outlook e vários serviços da companhia inacessíveis ou instáveis por horas, deixou algumas dúvidas no ar, entre elas, “a companhia teria sido alvo de hackers?”. Bom, de acordo com a própria empresa, o problema foi causado por falha em uma atualização de software.
Chega a ser irônico, pois atualizações de software visam corrigir falhas, não causá-las. Mas foi o que aconteceu aqui. Em um relatório preliminar sobre o caso, a companhia explica que o problema começou em uma atualização aplicada em julho deste ano em servidores de “gateway de rede” ligados ao Microsoft 365.
Esses servidores controlam o acesso aos serviços da empresa (embora não respondam pela autenticação de usuários), recebendo solicitações dos usuários e as encaminhando para os sistemas que devem lidar com elas. Se essa dinâmica falha, os tais serviços deixam de ser acessados.
A tal atualização de software visava corrigir um problema anterior. Depois que o procedimento foi realizado, nenhuma anormalidade foi percebida. Testes de carga de trabalho chegaram a ser executados, mas nenhum deles apontou falhas ou sinais de impactos operacionais negativos. Mas o problema estava lá.
Como a falha na atualização passou despercebida?
A própria Microsoft reconheceu que os testes pós-atualização não foram executados corretamente. Eles foram baseados em computadores mais antigos, com menos núcleos de processamento. Porém, o problema se manifestava com hardware mais recente e, portanto, com mais núcleos.
Eis que, no último dia 12, uma sequência de acontecimentos criou o cenário perfeito para que a falha, até então desconhecida, ganhasse forma.
Cerca de 15 horas antes da interrupção, o Microsoft Teams passou por um procedimento de failover, que transferiu seu tráfego para o gateway principal, também utilizado pelo Exchange Online.
Esse tipo de transferência de carga não é incomum ou inesperado. O problema é que, na ocasião, 14% da capacidade dos servidores de gateway estava indisponível devido a outro problema. Embora a infraestrutura da empresa ainda tivesse capacidade para absorver essa transferência isoladamente, a combinação com a demanda do Microsoft Teams fez a falha se manifestar.
Outlook só voltou à normalidade no dia seguinte
A consequência foi esta: o Outlook e outros serviços ficaram indisponíveis por horas. A normalização nos sistemas da Microsoft só ocorreu no dia seguinte (13/11).
Tamanha demora se deve à dificuldade que a companhia teve para identificar a origem do problema e aplicar uma atualização para reverter a correção que estava no centro do caos. A Microsoft chegou a ativar uma capacidade extra nos servidores de gateway, mas nem isso foi suficiente. A solução só se mostrou efetiva com a reversão.
Quem acha que o Outlook foi o serviço mais afetado, achou certo. Isso aconteceu porque o Outlook depende do Exchange Online. Enquanto serviços como Teams, OneDrive e SharePoint conseguiram recorrer a caminhos alternativos, por assim dizer, o Exchange Online não teve essa possibilidade em escala suficiente para manter a sua operação.
Vale destacar que este é um posicionamento preliminar. A Microsoft deve publicar um relatório mais detalhado sobre o “apagão” no próximo dia 20.
