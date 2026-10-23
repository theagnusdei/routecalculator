# Falhas críticas no PHP já eram exploradas por hackers antes de correção

- Editoria: Cibersegurança (`ciberseguranca`)
- Fonte: Canaltech — https://canaltech.com.br/seguranca/falhas-criticas-no-php-ja-eram-exploradas-por-hackers-antes-de-correcao/
- Autor: Marcelo Fischer
- Publicado: 2026-10-22T20:02:00+00:00
- Score: 3.798
- Imagem: imagens/ciberseguranca-falhas-criticas-no-php-ja-eram-explorada.jpg | crédito: Canaltech | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Falhas críticas no PHP já eram exploradas por hackers antes de correção
Por Marcelo Fischer |
As duas falhas críticas de segurança do PHP, que colocaram milhões de sites em alerta nesta semana, já eram alvo de tentativas de exploração por hackers desde 17 de outubro, quatro dias antes da divulgação das correções. A descoberta foi feita pela Amazon Web Services (AWS), que identificou atividades suspeitas em seus sistemas de monitoramento.
Segundo informações divulgadas pela Wired nesta quinta-feira (22), os ataques começaram antes mesmo do vazamento de informações sobre as vulnerabilidades, ocorrido na terça-feira (20).
A descoberta representa um novo desdobramento do alerta global de segurança provocado pelas falhas no PHP. As duas brechas, identificadas como CVE-2026-109618 e CVE-2026-109619, receberam classificação de gravidade de 9,2 em uma escala de 0 a 10.
Apesar das tentativas registradas, ainda não há confirmação de invasões bem-sucedidas. À Wired, a PHP Foundation, organização que apoia o desenvolvimento da linguagem, afirmou não ter conhecimento de casos em que invasores conseguiram executar códigos maliciosos remotamente utilizando as vulnerabilidades.
Como os hackers exploraram as falhas antes da correção?
A Amazon identificou os primeiros ataques ao analisar registros de sua rede MadPot, formada por servidores-isca, conhecidos como honeypots (potes de mel, em inglês).
Esses sistemas são utilizados para atrair tentativas de invasão e permitir que pesquisadores acompanhem as técnicas empregadas por criminosos.
O primeiro registro, de 17 de outubro, partiu de um endereço IP associado a um serviço comercial de anonimização, como uma rede de proxies ou VPN.
Segundo CJ Moses, diretor de segurança da AWS, a utilização desse tipo de infraestrutura para tentar explorar uma vulnerabilidade ainda mantida em sigilo indica uma possível atividade criminosa.
Entretanto, os pesquisadores não conseguiram determinar como o responsável pelo ataque obteve informações sobre a falha antes da divulgação pública.
A situação se intensificou em 21 de outubro. A Amazon identificou novas tentativas a partir das 2h UTC, equivalentes às 23h de terça-feira (20) no horário de Brasília, aproximadamente 12 horas antes da liberação das correções.
Nas seis horas seguintes, outros ataques partiram de diferentes serviços de anonimização e utilizaram códigos maliciosos distintos.
Para os pesquisadores, as diferenças sugerem a atuação de múltiplos grupos ou indivíduos, embora ainda não seja possível identificar os responsáveis.
Milhões de tentativas de invasão após divulgação das falhas
O número de ataques cresceu rapidamente depois que as vulnerabilidades se tornaram públicas.
Segundo Matthew Prince, CEO da Cloudflare, a empresa registrou milhares de tentativas de exploração nas dez horas anteriores à divulgação oficial.
O volume chegou a dezenas de milhares de tentativas nos primeiros 45 minutos após o anúncio e ultrapassou a marca de centenas de milhares em duas horas.
Ainda na quarta-feira (21), a quantidade acumulada de tentativas identificadas pela Cloudflare já havia chegado à casa dos milhões, conforme informações divulgadas pela Reuters.
A empresa também observou invasores modificando os códigos utilizados nos ataques para tentar contornar seus mecanismos de proteção.
Apesar do volume, é importante diferenciar tentativas de exploração de invasões efetivamente realizadas. Os números não significam que milhões de sites tenham sido comprometidos.
A Cloudflare afirma ter implementado proteções antes da divulgação oficial das vulnerabilidades, inclusive para clientes que utilizam seu serviço gratuito.
Essas medidas, porém, são temporárias e não substituem a atualização do PHP.
O que muda para quem já corrigiu as falhas?
A descoberta de ataques anteriores à divulgação pública exige que administradores de sites verifiquem se seus sistemas foram comprometidos antes da instalação das atualizações.
Segundo a Amazon, a recomendação é analisar registros de atividades suspeitas desde pelo menos 17 de outubro, e não apenas a partir de quarta-feira (21), quando as correções foram liberadas.
Entre os sinais que devem ser investigados estão requisições suspeitas enviadas aos servidores, execução inesperada de processos e alterações desconhecidas em arquivos.
A aplicação das correções impede a exploração das vulnerabilidades conhecidas, mas não desfaz eventuais alterações realizadas por invasores anteriormente.
A AWS também alerta que o avanço da inteligência artificial pode reduzir o intervalo entre a divulgação de uma falha e o desenvolvimento de ferramentas capazes de explorá-la.
Segundo a empresa, ferramentas de IA permitem analisar correções e identificar maneiras de contorná-las em questão de horas ou minutos. Entretanto, não há evidências de que os ataques identificados neste caso tenham utilizado inteligência artificial.
A descoberta reforça a preocupação com a segurança do PHP, linguagem utilizada por quase 70% dos sites cuja tecnologia de servidor é conhecida.
Até o momento, as empresas responsáveis pelo monitoramento não divulgaram um número confirmado de sites efetivamente invadidos por meio das duas vulnerabilidades.
