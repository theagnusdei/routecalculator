# Cuidado: excluir histórico de IA não apaga rastros em celulares Android

- Editoria: Software (`software`)
- Fonte: Canaltech — https://canaltech.com.br/inteligencia-artificial/cuidado-excluir-historico-de-ia-nao-apaga-rastros-em-celulares-android/
- Autor: Viviane França
- Publicado: 2026-10-27T14:35:00+00:00
- Score: 5.009
- Imagem: imagens/software-cuidado-excluir-historico-de-ia-nao-apag.jpg | crédito: Canaltech | licença: © do veículo/autor original — uso SOMENTE com autorização ou como referência; considere substituir por imagem livre (NASA, ESA, Wikimedia, banco próprio)

## Outras coberturas
- nenhuma

## Texto extraído

Cuidado: excluir histórico de IA não apaga rastros em celulares Android
Por Viviane França |
Os pesquisadores do Instituto de Tecnologia da Geórgia (Georgia Tech), nos Estados Unidos, desenvolveram uma ferramenta que consegue recuperar conversas excluídas de assistentes de IA que funcionam localmente em celulares Android. A tecnologia, batizada de ORISA, identifica fragmentos de bate-papos que continuam na memória do aparelho mesmo após a exclusão pelo aplicativo.
Isso acontece porque apagar um bate-papo pela interface do aplicativo não remove imediatamente todos os dados armazenados na memória de trabalho (RAM) do celular. Com isso, a ferramenta também conseguiu reconstruir o contexto das conversas e criar uma nova sessão funcional do chatbot.
A pesquisa foi realizada no Laboratório de Inovação em Forense Cibernética do Georgia Tech e apresentada no 2026 IEEE Symposium on Security and Privacy. Para testar a ferramenta, a equipe liderada pelo doutorando Ken Xu criou um assistente fictício chamado Project Note Keeper no aplicativo de código aberto ChatterUI.
Os pesquisadores forneceram 100 fatos fictícios ao assistente antes de excluir a conversa. Naquele momento, o modelo conseguia acessar ativamente apenas 14 informações devido ao limite de memória. O ORISA, porém, recuperou 26 fatos armazenados no celular e criou uma nova sessão capaz de responder a perguntas sobre o projeto.
O experimento também mostrou que a ferramenta consegue resgatar informações que já haviam saído da janela de contexto da IA. Embora o modelo não conseguisse mais consultar esses fatos durante a conversa original, os dados ainda permaneciam na memória do dispositivo e puderam ser recuperados pelo ORISA.
A equipe validou o desempenho da ferramenta em 60 configurações de teste, com 10 aplicativos Android e três modelos de IA. No entanto, segundo os pesquisadores, a recuperação fica mais difícil à medida que outras atividades do sistema sobrescrevem os dados antigos na memória do dispositivo.
O artigo Recovering and Rehosting Mobile Local LLM Conversations and Contexts via Memory Forensics também tem como autores os doutorandos David Oygenblik, Runze Zhang e Mingxuan Yao, o cientista de pesquisa Muhammad Ibrahim e o professor associado Brendan Saltaformaggio.
Ferramenta ajuda em investigações, mas levanta alertas de privacidade
O ORISA foi desenvolvido para auxiliar em investigações criminais e perícias digitais. A ferramenta consegue recuperar informações compartilhadas com assistentes de IA e as respostas recebidas, o que pode ajudar a esclarecer casos em que orientações de um chatbot tenham causado danos. No entanto, a tecnologia não é um aplicativo comercial ou público para usuários comuns restaurarem conversas apagadas, mas um recurso para análise forense de dispositivos.
A descoberta também levanta questões sobre a privacidade de quem usa assistentes de IA com processamento local, como o Google AI Edge Gallery e o ChatterUI. Essas ferramentas executam modelos no próprio celular, o que reduz a necessidade de enviar informações pessoais para servidores na nuvem. Ainda assim, apagar uma conversa não garante que todos os seus registros desapareçam imediatamente, pois fragmentos do histórico podem permanecer na memória do aparelho.
A recuperação depende de acesso forense à memória e ao armazenamento do dispositivo. Por isso, o estudo não indica que qualquer pessoa consiga restaurar conversas apagadas com facilidade. Os pesquisadores também não investigaram se bate-papos com assistentes de IA baseados na nuvem poderiam ser recuperados por técnicas semelhantes.
Se você gostou do conteúdo, talvez também se interesse por conferir “O que é "IA local"? Entenda como funcionam as ferramentas que rodam no seu PC”.
