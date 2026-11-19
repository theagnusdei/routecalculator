# Vulnerabilidade crítica afeta milhões de sites, apps e serviços feitos em Java

- Editoria: Cibersegurança (`ciberseguranca`)
- Fonte: Canaltech — https://canaltech.com.br/seguranca/vulnerabilidade-critica-afeta-milhoes-de-sites-apps-e-servicos-feitos-em-java/
- Autor: Marcelo Fischer
- Publicado: 2026-11-19T14:02:00+00:00
- Score: 4.164
- Imagem: imagens/ciberseguranca-vulnerabilidade-critica-afeta-milhoes-de.jpg | crédito: Canaltech | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Vulnerabilidade crítica afeta milhões de sites, apps e serviços feitos em Java
Por Marcelo Fischer |
Uma vulnerabilidade crítica no Java pode permitir que criminosos invadam sites, aplicativos e serviços que utilizam a linguagem de programação. Identificada como CVE-2026-114938 e chamada de Java4Shell, a falha permite a execução remota de códigos maliciosos, em alguns casos sem que o invasor precise de login ou senha.
A brecha foi divulgada na terça-feira (17) pela empresa de segurança Calif e recebeu uma pontuação de 9,2 em uma escala de gravidade que vai até 10. A Oracle, responsável pelo Java, já disponibilizou atualizações para corrigir o problema.
Segundo o Tom's Hardware, a exploração pode permitir o acesso a informações confidenciais, incluindo dados de usuários, e abrir caminho para o comprometimento de sistemas inteiros.
O problema está no OpenJDK, implementação de código aberto do Java utilizada como base para diferentes distribuições da linguagem. Como essa tecnologia está presente em sistemas corporativos, servidores e aplicações na internet, a vulnerabilidade tem um alcance potencial elevado.
Como funciona a vulnerabilidade no Java?
A Java4Shell afeta um componente responsável pela decodificação de informações no formato Base64, utilizado para representar dados em texto. Esse recurso aparece em processos de autenticação, envio de arquivos e comunicação entre serviços.
Os pesquisadores descobriram que uma sequência de apenas 64 letras "A", seguida do sinal de igual (=), pode provocar um erro no processamento dos dados em sistemas vulneráveis.
Isso acontece porque uma otimização utilizada para acelerar o processo permite que informações sejam gravadas fora do espaço de memória reservado. Dependendo das condições, um criminoso pode explorar essa falha para acessar dados ou executar comandos no servidor.
A exploração depende de requisitos específicos de hardware e software. A brecha afeta determinados processadores Intel e AMD compatíveis com a tecnologia AVX-512 VBMI, incluindo modelos das famílias Intel Ice Lake e AMD Zen 4.
Sistemas baseados na arquitetura ARM64 não são afetados por essa vulnerabilidade.
Quais serviços estão em risco?
Durante os testes, a Calif conseguiu explorar a falha em diferentes ferramentas utilizadas por empresas e desenvolvedores.
Entre os serviços em que os pesquisadores demonstraram ataques sem autenticação estão Jira, Confluence, Jenkins, Keycloak, JFrog Artifactory e PingFederate.
Também foram realizados testes bem-sucedidos no Apache Kafka, Elasticsearch, Apache Solr, Gerrit e Spinnaker, mas, nesses casos, a execução remota de código exigiu autenticação.
Isso não significa que todas as instalações dessas ferramentas estejam vulneráveis. O risco depende da versão do Java, do processador utilizado e da possibilidade de um invasor enviar dados ao componente afetado.
Segundo o alerta do CERT-EU, estão entre as versões vulneráveis o Java 17, a partir da versão 17.0.6, e versões das linhas 21, 25 e 27 anteriores às respectivas correções. Uma edição específica do Java 8 voltada a desempenho também é afetada.
Como se proteger da Java4Shell?
A Oracle publicou correções em 17 de novembro para as principais versões afetadas. Entre as atualizações disponibilizadas estão:
- Java 17.0.21.1;
- Java 21.0.13.1;
- Java 25.0.5.1;
- Java 27.0.1.1.
Empresas e administradores de sistemas devem verificar quais versões do Java estão em uso, inclusive aquelas incluídas diretamente em aplicativos e servidores.
O CERT-EU recomenda priorizar serviços acessíveis pela internet. Quando a atualização imediata não é possível, uma alternativa temporária é desativar a otimização vulnerável com o parâmetro "-XX:-UseBASE64Intrinsics" na máquina virtual Java.
Até 18 de novembro, empresas de segurança como a Check Point não haviam identificado ataques confirmados explorando a vulnerabilidade em ambientes reais. Entretanto, a Calif já demonstrou a possibilidade de invasão em laboratório e publicou detalhes técnicos sobre o problema.
