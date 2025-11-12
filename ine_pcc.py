import marimo

__generated_with = "0.17.7"
app = marimo.App(width="medium")


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
    df.to_latex("tabela.tex")
    return


@app.cell
def _(df):
    colunas = df[["Preço", "Lucro", "IBOVESPA"]]
    return (colunas,)


@app.cell
def _(colunas, df):
    for coluna in colunas:
        media = df[coluna].mean()
        mediana = df[coluna].median()
        moda = df[coluna].mode()
        print(f"{coluna}: média {media:.4f}, mediana {mediana:.4f} \ne moda {moda}")
        print("####")
    return


@app.cell
def _(colunas, df):
    for i in colunas:
        variancia = df[i].var()
        desvio_padra = df[i].std()
        minimo = df[i].min()
        maximo = df[i].max()
        print(f"{i}: mínimo {minimo}, máximo {maximo} variância {variancia:.4f} e desvio padrão {desvio_padra:.4f}\n####")
    return


@app.cell
def _(df, go, make_subplots):
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(
        go.Scatter(x=df['Trimestre'], y=df["IBOVESPA"], name='IBOVESPA'),
        secondary_y=False, # Define como Eixo Y Primário (à esquerda)
    )

    fig.add_trace(
        go.Scatter(x=df['Trimestre'], y=df["Lucro"], name="Lucro"),
        secondary_y=True, # Define como Eixo Y Secundário (à direita)
    )

    fig.update_layout(
        title_text='IBOVESPA (Pontos) vs. Lucro (Bilhões)',
        xaxis_title='Trimestres'
    )

    fig.update_yaxes(title_text="<b>em Pontos</b>", secondary_y=False)
    fig.update_yaxes(title_text="<b>em Bilhões de Reais</b>", secondary_y=True)

    fig.show()
    return


@app.cell
def _(df):
    df.columns
    return


@app.cell
def _(df, px):
    boxplot = px.box(
        df[["Período Governo", "IBOVESPA"]],
        y = df["IBOVESPA"],
        title= "Distribuição dos Preços nos Períodos de Governo"
    )

    boxplot.show()
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
    histo_anual.show()
    return


if __name__ == "__main__":
    app.run()
