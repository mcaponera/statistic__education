# Análise Estatística do Desempenho da Ação do Banco do Brasil (BRAS3) no período de 2004 a 2024

### Introdução
O mercado de capitais é um termômetro sensível às condições sociais e econômicas de um país. As cotações, lucros e índices do mercado, como o IBOVESPA, refletem tanto o desempenho corporativo, como também a confiança dos investidores.
Este trabalho tem como foco a análise estatística descritiva da ação do Banco do Brasil, a mais antiga instituição financeira do país, ao longo de um período significativo de 20 anos (2004 a 2024), abrangendo os governos Lula, Dilma, Temer e Bolsonaro, e o retorno ao governo Lula ao final da série histórica.
A motivação para este estudo reside na possibilidade de investigar, por meio de ferramentas estatísticas, como variáveis-chave — Preço da ação, Lucro por ação e o índice IBOVESPA — se comportaram e se relacionaram em diferentes contextos políticos e econômicos. Questões como "O lucro da empresa apresentou tendência de crescimento constante?" ou "Existe uma correlação visível entre o preço da ação e o desempenho do IBOVESPA?" ou ainda "É possível identificar padrões distintos de comportamento dessas variáveis entre os diferentes governos?" guiam esta investigação.
Para isso, serão utilizados conceitos fundamentais da estatística descritiva, como medidas de tendência central e dispersão, análise de frequência, construção de gráficos e estudo de correlação. O objetivo principal é realizar uma exploração deste conjunto de dados, apresentando os resultados de forma clara e discutindo possíveis interpretações para os padrões observados.

### Metodologia

#### Fonte dos Dados
Os dados históricos de preços das ações do Banco do Brasil (BBAS3.SA) e do índice IBOVESPA (BVSP), foram obtidos através da biblioteca [yfinance](https://pypi.org/project/yfinance/) do Python, que fornece acesso aos dados do Yahoo Finance. O período selecionado foi de janeiro de 2004 a dezembro de 2004, abrangendo 20 anos de dados trimestrais. Foi escolhida esta fonte, por ser amplamente utilizada pela comunidade financeira e por sua confiabilidade, frequência de atualização dos dados e manutenção do código da biblioteca.

Os dados de lucro líquido trimestral do Banco do Brasil foram coletados manualmente a partir dos relatórios financeiros trimestrais publicados pela instituição. Estes documentos estão disponíveis no site de relações com investidores do Banco do Brasil e representam informações auditadas e oficialmente divulgadas ao mercado.
- Classificação dos governos: baseada em mandatos presidenciais oficiais

#### Ferramentas e Softwares Utilizados
Para a coleta, processamento e análise dos dados, foram utilizadas as seguintes ferramentas: Python 3.12 com as bibliotecas pandas, para manipulação, yfinance, usado para a coleta dos dados financeiros, streamlit, para visualização interativa e plotly, para os gráficos.

#### Variáveis Utilizadas
Foram utilizadas quatro variáveis para analisar o desempenho da ação BBAS entre 2004 e 2024. A seleção dessas variáveis buscou capturar tanto aspectos específicos do ativo quanto o ambiente social no qual está inserido.
A variável **Preço da ação** apresenta o valor de mercado no fechamento de cada trimestre, servindo de indicador direto da percepção no mercado. Paralelamente, o **Lucro Líquido Trimestral** reflete o desempenho operacional e a saúde financeira da instituição.
Para contextualizar o desempenho do ativo em relação ao mercado, incluiu-se o **IBOVESPA**, principal índice de referência do mercado acionário. Esta variável permite observar se os movimentos do ativo estão ou não alinhados com tendências gerais do mercado ou apresentam comportamento distinto.
Por fim, a variável **Período de Governo** introduz uma dimensão qualitativa importante, categorizando cada trimestre conforme o governo federal vigente. Permitindo examinar se contextos políticos podem influenciar o desempenho do setor financeiro, em especial o Banco do Brasil, instituição financeira de de economia mista, com controle estatal.
Essas variáveis, duas quantitativas que explicitam preços, uma quantitativa que expressa um score e uma qualitativa, proporciona uma base de investigação interessante para explorar fatores que podem influir no desempenho da mais antiga instituição financeira do país.


‌
