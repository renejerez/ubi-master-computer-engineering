• Background and Motivation.

De acordo com o Instituto dos Mercados Públicos, do Imobiliário e da Construção, I.P. (IMPIC,
I.P.), o portal dos contratos públicos, denominado Portal BASE, destina-se a divulgar
informação pública sobre os contratos públicos sujeitos ao regime do Código dos Contratos
Públicos, de acordo com o previsto no artigo 2.º do DL n.º 111-B/2017, de 31 de agosto, que
alterou e republicou o Código dos Contratos Públicos (CCP), aprovado pelo DL n.º 18/2008,
de 29 de janeiro. O portal tem por função essencial centralizar a informação sobre os contratos
públicos celebrados em Portugal, configurando um espaço virtual onde são publicitados os
elementos referentes à formação e execução dos contratos públicos, permitindo assim o seu
acompanhamento e monitorização.


• Project Objectives and Research Questions

O nosso objetivo é promover a monitorização pública das ações do governo, ajudando a
melhorar e a manter a honestidade dos contratos e das políticas públicas.
Gostávamos de ser uma fonte para impulsionar a transparência do governo e a integridade com
informações fiáveis.

Afonso Silva em seu repositório do github https://github.com/ajcerejeira/base.gov.pt
desenvolveu um método de extração completa do Base de Contratos, no entanto, não
prosseguiu com nenhuma análise ou estudo consoante aos dados descarregados.

Já Antonio Cruz, 2017, em seu sitio web http://value-from-data.com/blog/2017/04/teoriagrafos/ criou um modelo de grafos que conecta as entidades com conexão entre elas e há um
grafo para cada tipo de contrato, no entanto, os dados estão desatualizados desde 2017.
• Project Architecture

Para este projeto serão inicialmente serão utilizadas as bibliotecas BeautifulSoup, pandas,
urlencode, selenium, webdriver_manager.chrome, time, logging, Llama Index
Na base de dados fazemos uso da Cloud okeanos por ser gratuito e fazemos uso diário,
https://accounts.okeanos-global.grnet.gr/
O modelo de dados deve inicialmente ser conforme abaixo:

Na mesma plataforma Cloud Okeanos vamos ter uma VM para correr os processos automaticos
de scraping que será feito com Airflow.
Os dados estarão disponíveis para consulta por qualquer software terceiro via API.


• Data.

A fonte de dados será do sítio web https://www.base.gov.pt/base4.
Também utilizaremos a lista de códigos de CPV https://www.govis.pt/codigos/cpv


• Ethical Considerations.

Em caso de encontrar irregularidades as empresas e as entidades envolvidas estarão expostas
como possível tentativa de fraude ou contratos irregulares e isso pode gerar má reputação ou
perda de contrato público.


• Data Processing.

Os dados serão coletados por scraping e serão organizados conforme modelo de dados e
devem ter cruzamento de informações entre as três extrações que serão realizadas.
Deverá ser necessário alterar os tipos de dados que serão coletados e manter um standard para
a extração diária.

Devemos ter um manual da API para o uso de terceiros.
O código será majoritariamente em Python para a extração, sítio web via Streamlit e modelo
preditivo ou RAG com python.


• Exploratory Data Analysis.

Faremos a analise de dados nulos, relação de colunas entre si, distribuição por coluna,
outliers.
Faremos tambem o uso de AutoML para verificar qual é a importancia de cada coluna, um
tipo de feature selection.

• Data Visualization.

Vamos olhar as quinze entidades que em total tem os maiores valores de contrato.
Também veremos para os tipos de contratos quais tem o maior valor contratado.
Veremos quais entidades tem a maior quantidade de contratos ofertados e contratados.
Faremos um mapa com a morada de cada entidade e valores contratados por zona.
Em caso de tempo hábil faremos a visualização de grafos conforme o Antonio Cruz o fez