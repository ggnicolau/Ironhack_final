<div align="center">
<img src="https://coursereport-production.imgix.net/uploads/school/logo/84/original/logo-ironhack-blue.png?w=200&h=200&dpr=1&q=75">
</div>

<div align="left">

[![Typing SVG](https://readme-typing-svg.herokuapp.com/?lines=Seja+bem-vindo!)](https://git.io/typing-svg)
</div>
<!--GITHUB_ACTIVITY:{"rows": 5}-->

---

<div align="center">

[![visitors](https://visitor-badge.glitch.me/badge?page_id=ggnicolau.visitor-badge)](https://badges.pufler.dev)
[![Created Badge](https://badges.pufler.dev/created/ggnicolau/Ironhack_final)](https://badges.pufler.dev)
[![Updated Badge](https://badges.pufler.dev/updated/ggnicolau/Ironhack_final)](https://badges.pufler.dev)
[![Commits Badge](https://badges.pufler.dev/commits/monthly/ggnicolau)](https://badges.pufler.dev)
[![Repos Badge](https://badges.pufler.dev/repos/ggnicolau)](https://badges.pufler.dev)
[![Years Badge](https://badges.pufler.dev/years/ggnicolau)](https://badges.pufler.dev)
[![ggnicolau StackOverflow](https://stackoverflow-badge.vercel.app/?userID=15673147)](https://stackoverflow.com/users/15673147/ggnicolau)

![+5511976431347](https://img.shields.io/badge/WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white)
![ggnicolau](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)
![ggnicolau@usp.br](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
![https://www.linkedin.com/in/ggnicolau/](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)
![Python 3.9](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PHP](https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white)
![pgAdmin](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Atom](https://img.shields.io/badge/Atom-66595C?style=for-the-badge&logo=Atom&logoColor=white)
![Windows 10 Pro](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![Anurag's GitHub stats](https://github-readme-stats.vercel.app/api?username=ggnicolau&show_icons=true&theme=darcula)
</div>
<!--GITHUB_ACTIVITY:{"rows": 5}-->

---

<div align="left">
<div class=''text-justify''>

# Modelo de Tópicos e a Prefeitura de SP (NLP)
Esse projeto é parte do trabalho final do Bootcamp em Data Analytics da Ironhack, turma de 2021. Também é extensão de trabalhos desenvolvidos durante o mestrado e doutorado em ciência política pela Universidade de São Paulo.

## Tecnologias
* Python version  3.9
* PHP
* postgreSQL
* Prezi

## Ferramentas
* Atom
* pgAdmin
* Jupyter IPython
* Git

## Serviços usados
* Github

## Python Libraries
* os
* glob
* tika
* pandas
* regex
* Audio
* sqlalchemy
* tqdm
* warnings
* csv
* stanza
* gensim
* texthero
* nltk
* SpaCy
* numpy
* pprint
* logging
* time
* random
* operator
* pyLDAvis
* Matplotlib
* Sklearn

## O que é esse projeto?
Buscamos aqui apresentar nosso MVP (Minimal Viable Product) de análise semântica automatizada de grande conjunto de documentos. Aqui analisamos por volta de 200 mil notícias institucionais das secretarias da Prefeitura do Município de São Paulo, entre 2003 e 2020. Demos especial atenção para comparar as duas últimas gestões (Haddad e Dória-Covas). Nossa ferramenta poderia ser aplicada a outros objetos. Por exemplo, poderíamos extrair todas as notícias e conteúdos textuais dos principais sites de empresas de determinado setor para fazer análise de discurso e de suas identidades, para entender como apresentam sua imagem no mercado. Poderíamos comparar as empresas entre si etc. Na verdade, há inúmeras possibilidades e utilidades.

## O que é Topic Model?
* não-supervisionado;
* não-estruturado;
* LDA retorna tópicos. O que é isso?
  * A principal característica dos modelos de tópicos é sua capacidade de realizar uma redução dimensional do espaço definido pelo modelo bag-of-words de forma a capturar estruturas semânticas presentes no espaço. Além disso temos que o novo espaço, dito espaço de tópicos, é um modelo probabilístico para a ocorrência de palavras nos documentos; ou seja, busca-se a covariância entre as palavras em um documento e a relação entre os documentos (Corpus). Vamos além da contagem de palavras.
  * Temos menos bias do que o 'tageamento' de um sujeito e, portanto, melhor classificação que um humano; é ótimo, por exemplo, para informational retrieveal, ou seja, encontrar um conteúdo textual específico em um grande conjunto de dados;
* Um topico se apresenta assim:
  * TÓPICOS DE CULTURA

  > (17, '0.228*"anos" + 0.120*"show" + 0.097*"projeto" + 0.080*"apresentacoes" + 0.076*"musicas" + 0.074*"banda" + 0.025*"acervo" + 0.022*"largo" + 0.018*"pontos" + 0.018*"novo"')

  > (4, '0.164*"sobre" + 0.112*""o" + 0.092*"biblioteca" + 0.075*"diretor" + 0.062*"exposicao" + 0.054*"obras" + 0.051*"reune" + 0.042*"andrade" + 0.042*"mario" + 0.037*"primeiro"')

  > (10, '0.181*"ate" + 0.126*"danca" + 0.092*"inscricoes" + 0.069*"artistas" + 0.068*"musical" + 0.066*"programa" + 0.052*"janeiro" + 0.049*"recebe" + 0.035*"atividades" + 0.023*"grupos"')

* Quais as vantagens de ser sem estrutura e sem supervisão?
  * Não precisamos de 'target' e não tem interferência do sujeito na interpretação do objeto, ou seja, não há interferência humana na definição dos sentidos (semântica) dentro de nosso Corpus.

## Worfklow
Todos os códigos podem ser encontrados na pasta ```py files``` ordenados
* Primeiro extraímos o conteúdo dos sites das secretarias através de PHP;
* Automatizado através de uma função, incorporamos tudo em um pandas DataFrame, cada linha com duas colunas: data e texto;
* Sincronizamos com um banco de dados postgreSQL;
* Automatizado através de uma função, limpamos o texto da tabela (tiramos url, maiusculas, acentos, números, datas, letras únicas, simbolos, stopwords etc);
* Fizemos lematização sem definir função para ter controle de erros (processo lento de deep learning - nem tudo apresentado aqui incorporou a lematização);
* Criamos uma função para automatizar o modelo LDA para cada recorte de análise;
* Não incorporamos hiperparâmetros: nossa intenção é mostrar para o cliente como o algoritmo funciona com os mesmos parâmetros em diferentes conjuntos de dados;
* Visualizações (automatizamos o processo em funções para retornar uma visualização para cada secretaria por gestão);

## Visualizações
* WordClouds:

<div align="center">

![ex](https://github.com/ggnicolau/Ironhack_final/blob/main/Presentation/Images/assistencia_social_doria_covas21.png)

</div>

* pyLDAvis:
  * Não foi possível incorporar o gráfico dinâmico em HTML no GitHub. Faça download do arquivo seguranca_urbana.html e abra em seu navegador para ver um exemplo do gráfico dinâmico pyLDAvis: <https://github.com/ggnicolau/Ironhack_final/tree/main/Presentation>
<br/><br/>
  <div align="center">

  ![ex](https://github.com/ggnicolau/Ironhack_final/blob/main/All%20Visualizations/pyLDAvis_example.png)

  </div>

* Cruzamento de assuntos criados por nós com tópicos no corpus por gestão;
  * Cruzamos o tópico de segurança com o tópico de saúde para ver qual o principal documento do Corpus o algoritmo nos retornava:
  > 'GCM encaminha homem que tentou suicídio a atendimento social    5/01/2010  Texto: Gláucia Arboleya A Guarda Civil Metropolitana encaminhou, na última quarta-feira (13/1) por volta das 14h30, um homem que tentou se suicidar no Viaduto do Chá para o Atendimento Médico Ambulatorial (AMA), na Sé. O homem é natural da cidade de Paulo Afonso, Bahia, e estava em situação de risco há 30 dias. A Inspetoria do Gabinete do Prefeito visualizou a vítima do lado externo da grade do viaduto e foi até o local. Após conversa com o homem, ele aceitou a sair da posição de risco do viaduto e acompanhar os guardas civis metropolitanos para a AMA. Ele estava acompanhado por um rapaz de 18 anos, também em situação vulnerável há 30 dias, natural de Val Paraíso – interior de São Paulo. Ambos foram encaminhados para atendimento médico e, posteriormente, ao atendimento social para acolhimento em albergue da região até que seja viabilizado o retorno para as suas cidades de origem. No ano passado a GCM também atendeu um homem que tentou se suicidar da passarela do DETRAN, no Ibirapuera. O encaminhamento de pessoa em situação de risco é um dos programas prioritários da GCM.'

* Retorno de documentos mais importantes por tópico no corpus e de cruzamento entre tópicos;
  * Criamos um grupo de palavras sobre determinado assunto e cruzamos com os tópicos no Corpus para entender como era a distribuição dos assuntos entre cada gestão:

Haddad:

<div align="center">

![ex1:Haddad](https://github.com/ggnicolau/Ironhack_final/blob/main/Presentation/Images/Captura%20de%20Tela%20(192).png)

![ex1:Haddad](https://github.com/ggnicolau/Ironhack_final/blob/main/Presentation/Images/haddad.png)

</div>

Dória:

<div align="center">

![ex2:Dória](https://github.com/ggnicolau/Ironhack_final/blob/main/Presentation/Images/Captura%20de%20Tela%20(194).png)

![ex2:Dória](https://github.com/ggnicolau/Ironhack_final/blob/main/Presentation/Images/D%C3%B3ria.png)

</div>

## Algumas conclusões
Analisando algumas secretarias e comparando as gestões percebemos que em seus discursos (mais gráficos podem ser encontrados na pasta Presentation desse projeto):

1) Na assistência social, Dória-Covas parecem dar mais atenção ao trabalho e mercado, como capacitação das pessoas em situação de vulnerabilidade. Haddad busca dar mais atenção aos direitos humanos e às minorias (mulheres, indígenas etc);
2) Na segurança pública, Dória-Covas parecem dar mais atenção à Zeladoria e limpeza da cidade, dentro do programa Cidade Linda. Já Haddad parece dar mais atenção aos direitos humanos, como o desarmamento, mediação de conflitos, violência sexual e meio ambiente. Ambos também tem agenda repressora às drogas e aos ambulantes.
3) A saúde parece não ter variação entre as gestões, tendo continuidade e se apresentando mais como um programa de Estado que um programa de Governo. Sempre se fala de prevenção, saúde da mulher, maternidade, cuidado com o idoso, dengue, vacinação, hiv e Carnaval. Na gestão Dória também encontramos um tópico sobre o Corujão para acabar com as filas nas UBSs.

## Futuro
Recomendamos aos clientes incorporarem as seguintes ferramentas além das disponíveis no nosso MVP:
- Automatizar (mais) nossas pipelines, transformando as funções em classes;
- Incorporar e automatizar os hiperparâmetros;
- Automatizar o reto de documentos mais importantes por tópico;
- Comparação entre tópicos no corpus, através de Structured Topic Model (biblioteca de R) em um heatmap;
- NER;
- Sentiment Analysis;

## Agradecimentos

* Especialmente à Rai e Adriano, que são pessoas incríveis, muito inteligentes e muito pacientes;
* Aos meus colegas: Eduardo, Aline, Matheus, Márcio e Luís;
* E a todos da Ironhack que tornaram possível esse Bootcamp que é uma experiência única de vida!
* E a todos que já passaram ou que ainda passarão pela Ironhack, que é uma comunidade!

## Links

  - Repositório: https://github.com/ggnicolau/Ironhack_final
  - Códigos em Python do modelo de tópicos e do workflow: (https://github.com/ggnicolau/Ironhack_final/tree/main/py%20files)
  - Códigos em PHP de web scraping das notícias institucionais: (https://github.com/ggnicolau/Ironhack_final/tree/main/PHP%20webscraping)
  - Exemplos visuais do nosso produto: (https://github.com/ggnicolau/Ironhack_final/tree/main/Presentation)
  - Ver apresentação completa, com mais gráficos e análises, baixando o arquivo executável (.exe) do Prezi em: (https://github.com/ggnicolau/Ironhack_final/tree/main/Presentation)
  - Se quiserem acesso a todas as visualizações geradas automaticamente pela nossa pipeline, acessar aqui: (https://github.com/ggnicolau/Ironhack_final/tree/main/All%20Visualizations)
  - Se quiserem todas as nossas tabelas limpas sem lematização, acessar: (https://github.com/ggnicolau/Ironhack_final/tree/main/tables_clean_no_lem)
  - Se quiserem todas as tabelas limpas e lematizadas, acessar: (https://github.com/ggnicolau/Ironhack_final/tree/main/tables_clean_lem)
  - Se quiserem acesso a todas as notícias institucionais coletadas, acesso em: (https://github.com/ggnicolau/Ironhack_final/tree/main/News)

## Versioning

1.0.0.0

## Autor

* **Guilherme Giuliano Nicolau**: @ggnicolau (https://github.com/ggnicolau)

</div>

<!--GITHUB_ACTIVITY:{"rows": 5}-->

---

<div align="center">

<br/><br/>
![Quote](https://github-readme-quotes.herokuapp.com/quote?theme=dark&animation=grow_out_in)

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=ggnicolau&layout=compact)](https://github.com/anuraghazra/github-readme-stats)

![https://medium.com/@ggnicolau](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)


</div>
