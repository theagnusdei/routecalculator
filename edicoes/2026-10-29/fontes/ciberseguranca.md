# Golpe do falso Claude usa site oficial da Anthropic para roubar senhas e criptomoedas

- Editoria: Cibersegurança (`ciberseguranca`)
- Fonte: Canaltech — https://canaltech.com.br/inteligencia-artificial/golpe-do-falso-claude-usa-site-oficial-da-anthropic-para-roubar-senhas-e-criptomoedas/
- Autor: Viviane França
- Publicado: 2026-10-28T13:05:03+00:00
- Score: 4.283
- Imagem: imagens/ciberseguranca-golpe-do-falso-claude-usa-site-oficial-d.jpg | crédito: Canaltech | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Golpe do falso Claude usa site oficial da Anthropic para roubar senhas e criptomoedas
Por Viviane França |
Uma campanha de cibercriminosos usa anúncios pagos do Google para distribuir versões falsas do Claude e roubar senhas e criptomoedas. A fraude direciona usuários a páginas hospedadas no domínio oficial da Anthropic, claude.ai, para enganar as vítimas e instalar programas maliciosos em computadores com macOS e Windows.
A fraude foi identificada por pesquisadores da Gen Digital, empresa responsável pelas marcas Norton e Avast. Os criminosos exploram duas ferramentas do Claude, chamadas Artefatos e chats compartilhados, que permitem publicar conteúdos acessíveis por outras pessoas. Com elas, os invasores criam páginas falsas dentro do próprio site da inteligência artificial, o que dificulta a identificação do golpe pelo endereço da página.
As páginas mostram apenas um aviso discreto de que o conteúdo foi criado por um usuário e não passou por verificação. No macOS, a vítima recebe instruções para executar um comando no Terminal, que instala o Atomic Stealer (AMOS), um malware especializado no roubo de informações.
O programa mostra uma tela falsa de senha semelhante à dos Ajustes do Sistema para capturar credenciais. Ele também coleta dados de navegadores, cookies, informações armazenadas no Keychain e arquivos de backup. Além disso, pode substituir aplicativos, como Ledger Live e Trezor Suite, por cópias adulteradas para roubar frases de recuperação de carteiras de criptomoedas.
No Windows, os criminosos recorrem a uma técnica conhecida como ClickFix. A página orienta o usuário a pressionar Win + R e colar um comando do PowerShell. A instrução baixa um trojan de acesso remoto hospedado no GitHub, que dá aos invasores acesso ao dispositivo. Com o programa instalado, os criminosos conseguem fazer capturas de tela, procurar carteiras de criptomoedas e controlar o computador à distância.
A estratégia faz parte de uma sequência de ataques que exploram a confiança em plataformas de inteligência artificial. Em julho, um anúncio no Bing já havia direcionado usuários a uma página fraudulenta no domínio da Anthropic. Em outubro, uma versão falsa do ChatGPT hospedada em chatgpt.com foi usada para disseminar outro trojan.
Uma das dificuldades para bloquear esse tipo de ataque é que as próprias vítimas executam os comandos indicados nas páginas. Como a instalação começa com uma ação manual do usuário, algumas proteções antivírus podem não impedir a invasão.
Em agosto, a Anthropic desconectou preventivamente as sessões de contas comprometidas por infostealers, como o AMOS. Até a divulgação do relatório da Gen Digital, porém, a empresa não havia se pronunciado sobre a remoção das páginas denunciadas.
Como baixar o Claude com segurança?
A Anthropic disponibiliza os instaladores oficiais do Claude para Mac e Windows em sua página de downloads: claude.com/download. Para evitar golpes:
- Desconfie de comandos no Terminal ou PowerShell: o instalador convencional do Claude para desktop não pede a execução de comandos desse tipo. A exceção é o Claude Code, ferramenta para desenvolvedores que possui documentação própria da Anthropic;
- Digite o endereço oficial no navegador: evite clicar em anúncios de pesquisa no Google ou Bing para baixar o aplicativo. Prefira acessar claude.com/download manualmente ou usar um favorito salvo anteriormente;
- Confira os avisos da página: páginas legítimas de download não são chats compartilhados nem visualizadores de Artefatos com avisos de conteúdo criado por usuários.
O que fazer se o computador for infectado?
Se você executou comandos de uma página suspeita, use outro dispositivo confiável para trocar as senhas das contas mais importantes, começando pelo e-mail e pelos serviços bancários. Também é recomendável encerrar as sessões ativas e habilitar a autenticação em dois fatores (2FA).
No caso de carteiras de criptomoedas, a orientação é transferir os ativos para uma nova carteira, criada com uma nova frase de recuperação. No entanto, se o dispositivo estiver comprometido, gerar a nova carteira nele pode expor novamente os ativos ao roubo, por isso é indicado utilizar outro aparelho.
Se você gostou do conteúdo, talvez também se interesse por conferir “Como se proteger de golpes feitos com IA?”.
