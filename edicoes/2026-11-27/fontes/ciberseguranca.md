# 1Password sofre invasão e alerta clientes sobre vazamento de dados

- Editoria: Cibersegurança (`ciberseguranca`)
- Fonte: Tecnoblog — https://tecnoblog.net/noticias/1password-sofre-invasao-e-alerta-clientes-sobre-vazamento-de-dados/
- Autor: Emerson Alecrim
- Publicado: 2026-11-26T13:49:54+00:00
- Score: 4.233
- Imagem: imagens/ciberseguranca-1password-sofre-invasao-e-alerta-cliente.jpg | crédito: Mobilon Mídia LTDA | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Resumo IA
- A 1Password relatou uma invasão em seus sistemas, mas os cofres de senhas e chaves de recuperação de acesso não foram comprometidos.
- Dados como nome, endereço de e-mail, chaves públicas e tokens de links enviados por e-mail foram expostos, porém.
- A 1Password afirma que um pequeno número de usuários foi afetado e que eles foram notificados; não é necessário alterar senhas ou chaves de acesso.
Se você tem conta na 1Password, atenção: o serviço de gerenciamento de senhas emitiu um comunicado para alertar clientes sobre uma invasão aos seus sistemas. Os hackers não tiveram acesso a cofres de senhas e chaves de recuperação de acesso, mas dados como nome e endereço de e-mail foram expostos.
De acordo com uma investigação iniciada pela própria 1Password em 19 de novembro de 2026, o problema teve origem no comprometimento da conta corporativa de um de seus funcionários no GitHub.
Ao acessar essa conta, os invasores puderam entrar nos repositórios privados da empresa e inserir um código malicioso em serviços internos que, por sua vez, foi capaz de captura dados relacionados a clientes.
Para completar, os hackers conseguiram copiar um código-fonte interno da empresa, bem como acessar o ambiente de CI/CD (Continuous Integration e Continuous Delivery/Deployment), um conjunto de ferramentas e processos que automatiza testes, compilação e distribuição de software.
Ambientes de CI/CD podem conter credenciais de acesso e dados críticos de infraestrutura, por isso, o acesso indevido a ele configura um importante problema de segurança.
Quais dados de usuários da 1Password foram vazados?
Segundo a 1Password, o vazamento expôs os seguintes dados de clientes:
- nome
- endereço de e-mail
- chaves públicas
- datas e horários de criação de conta ou último login
- tokens de links enviados por e-mail relacionados a convites, provisionamento de contas e recuperação de acesso
- parâmetros do protocolo SRP (Secure Remote Password), usado para autenticação
- metadados internos
A 1Password ressaltou que os cofres que armazenam senhas e dados relacionados não foram comprometidos, o mesmo valendo para as chaves que protegem esses cofres e para os aplicativos ou extensões do serviço.
Quanto aos tokens expostos, a companhia explica que eles não são suficientes para as contas dos clientes serem acessadas, pois esse procedimento também exige um código de verificação de seis dígitos enviado por e-mail ou autenticação de login único (SSO, na sigla em inglês).
Já a exposição de chaves públicas não chega a ser um problema grave, pois esse tipo de informação foi projetada para ser compartilhada sem que isso permita decifrar informações protegidas. A exposição de chaves privadas é que seria um problema, mas isso não aconteceu.
O que o usuário da 1Password deve fazer?
A 1Password afirma que apenas um pequeno número de usuários foi afetado pela invasão e que eles foram notificados individualmente sobre o problema. Em todos os casos, não é preciso que os clientes alterem senhas ou chaves de acesso.
Por outro lado, os usuários devem ficar atentos para possíveis ações de phishing que usam os dados expostos para aplicar golpes em nome da 1Password.
Do seu lado, a companhia informou já ter adotado medidas para deter a invasão e evitar outros incidentes do tipo. Entre elas está a desativação da conta no GitHub comprometida, o reforço da segurança do ambiente de CI/CD e a contratação de especialistas em segurança para validação e aplicação de ajustes nos procedimentos adotados.
