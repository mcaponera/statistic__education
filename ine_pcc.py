import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _():
    import pandas as pd
    import plotly.express as px
    from plotly.subplots import make_subplots
    import plotly.graph_objects as go
    return go, make_subplots, pd, px


@app.cell
def _(pd):
    df = pd.read_csv("BBAS3-2004_2024.csv")
    df.sample(8)
    return (df,)


@app.cell
def _(df):
    df.shape
    return


@app.cell
def _(df):
    df.to_latex("brutos/tabela.tex")
    return


@app.cell
def _():
    colunas = ["Preço", "Lucro", "IBOVESPA"]
    return (colunas,)


@app.cell
def _(colunas, df):
    for coluna in colunas:
        media = df[coluna].mean()
        mediana = df[coluna].median()
        moda = df[coluna].mode()
        print(f"{coluna}: média {media:.4f}, mediana {mediana:.4f} e moda\n{moda}")
        print("####")
    return


@app.cell
def _(colunas, df):
    for i in colunas:
        variancia = df[i].var()
        desvio_padra = df[i].std()
        minimo = df[i].min()
        maximo = df[i].max()
        print(f"{i}: mínimo {minimo}, máximo {maximo} variância {variancia:.4f} e desvio padrão {desvio_padra:.4f}")
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df, px):
    df['Ano'] = df['Trimestre'].str.split('-').str[1]

    # agrupa por ano e calcula a média
    lucro_anual = df.groupby('Ano')['Lucro'].mean()

    histo_anual = px.histogram(
        x=lucro_anual.index,
        y=lucro_anual.values,
        title="Lucro Líquido Médio Anual (Bilhões R$)",
        labels={'x': 'Ano', 'y': 'Lucro Médio (Bilhões R$)'}
    )

    histo_anual.update_layout(
        yaxis_title='Lucro Médio (Bilhões R$)', # Define o título exato sem o prefixo de agregação
        xaxis_title='Ano',
        hovermode='x unified'
    )

    histo_anual.update_xaxes(
        tickangle=45,
        dtick=1 # Garante que todos os anos sejam mostrados
    )

    histo_anual.update_yaxes(
        tickprefix='R$ ',
        ticksuffix=' Bi',
        showgrid=True,
    )

    histo_anual.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Análise exploratória
    """)
    return


@app.cell
def _(df, pd, px):
    freq_abs = df["Período Governo"].value_counts()
    freq_rel = df["Período Governo"].value_counts(normalize=True) * 100

    tab_freq = pd.DataFrame({
        'Governo' : freq_abs.index,
        'Frequência Relativa': freq_rel.values,
        'Frequência Absoluta': freq_abs.values
    })

    fig_barras = px.bar(
        tab_freq,
        x='Governo',
        y='Frequência Absoluta',
        text='Frequência Absoluta',
        title='Distribuição de Frequência - Período de Governo',
        color='Governo'
    )
    tab_freq.to_latex('brutos/freq_gov.tex')
    fig_barras.show()
    return (tab_freq,)


@app.cell
def _(tab_freq):
    tab_freq
    return


@app.cell
def _(df, px):
    variaveis = ['Preço', 'Lucro', 'IBOVESPA']
    quartis_df = df[variaveis].quantile([0.25, 0.5, 0.75])

    fig_lucro_box = px.box(
        df, 
        y='Lucro',
        title='Distribuição do Lucro Líquido - Boxplot',
        #notched=True,
        hover_data=['Trimestre'],
        points='all'
    )
    fig_lucro_box.update_layout(yaxis_title='Lucro (Bilhões R$)')
    fig_lucro_box.show()
    return


@app.cell
def _(df, go, make_subplots):

    # 2. Criação da Figura com Eixo Y Secundário
    # Usamos make_subplots para criar a estrutura de dois eixos Y
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    # Adicionar a linha do Lucro (Eixo Y Primário)
    fig.add_trace(
        go.Scatter(
            x=df['Trimestre'],
            y=df['Lucro'],
            mode='lines+markers',
            name='Lucro (BBAS3.SA)',
            marker=dict(size=4)
        ),
        secondary_y=True, # Este é o eixo Y primário (left)
    )

    # Adicionar a linha do IBOVESPA (Eixo Y Secundário)
    fig.add_trace(
        go.Scatter(
            x=df['Trimestre'],
            y=df['IBOVESPA'],
            mode='lines+markers',
            name='IBOVESPA',
            marker=dict(size=4)
        ),
        secondary_y=False, # Este é o eixo Y secundário (right)
    )

    # 3. Configurações de Layout Simplificadas
    fig.update_layout(
        title={
            'text': 'Lucro BBAS3 x IBOVESPA (2004-2024)',
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': {'size': 18}
        },
        hovermode='x unified', # Melhora a interatividade
        template='plotly_white',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )

    # Configurar Eixo X
    fig.update_xaxes(
        title_text="Trimestre",
        tickformat="%b %Y",
        showgrid=True,
        gridcolor='#eaeaea'
    )

    # Configurar Eixo Y Primário (Lucro)
    fig.update_yaxes(
        title_text="Lucro (BBAS3.SA)",
        secondary_y=True,
        showgrid=True,
        gridcolor='#eaeaea',
        tickprefix='R$ ',
        ticksuffix=' Bi',
        showspikes=True,
        spikethickness=1,
    )

    # Configurar Eixo Y Secundário (IBOVESPA)
    fig.update_yaxes(
        title_text="IBOVESPA (Pontos)",
        secondary_y=False,
        showgrid=False, # Geralmente desliga-se a grade do secundário para clareza
        tickformat='.0f', # Formato para pontos (ex: 100,000)
        showspikes=True,
        spikethickness=1,
    )


    # Exibir o gráfico
    fig.show()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # correlação
    """)
    return


@app.cell
def _(df):
    # Matriz de correlação de Pearson
    correlacoes = df[['Preço', 'Lucro', 'IBOVESPA']].corr(method='pearson')

    print("MATRIZ DE CORRELAÇÃO DE PEARSON")
    print("="*40)
    print(correlacoes.round(3))
    return (correlacoes,)


@app.cell
def _(df):
    df[['IBOVESPA', 'Preço', 'Lucro']].corr()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Modelo de Regressão
    """)
    return


@app.cell
def _(df, px):
    correlacaoI = px.scatter(
        df, 
        x='IBOVESPA', 
        y='Lucro',
        title='Relação entre IBOVESPA e Lucro Líquido',
        trendline='ols',
        trendline_color_override="red",
        labels={'IBOVESPA': 'IBOVESPA (pontos)', 'Lucro': 'Lucro Líquido (Bilhões R$)'}
    )
    correlacaoI.show()
    return


@app.cell
def _(correlacoes, px):
    fig_corr = px.imshow(
        correlacoes,
        text_auto=True,
        aspect="auto",
        color_continuous_scale='Burg',
        title='Matriz de Correlação entre Variáveis Quantitativas'
    )
    fig_corr.update_layout(width=500, height=500)
    fig_corr.show()
    return


@app.cell
def _(df):

    import statsmodels.api as sm

    X_sm = sm.add_constant(df[['IBOVESPA', 'Preço']])

    modelo_sm = sm.OLS(df['Lucro'], X_sm).fit()

    print(modelo_sm.summary())
    return


if __name__ == "__main__":
    app.run()
