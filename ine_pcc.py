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
    return pd, px


@app.cell
def _(pd):
    df = pd.read_csv("BBAS3-2004_2024.csv")
    df.sample(8)
    return (df,)


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


app._unparsable_cell(
    r"""
    for i in colunas:
        variancia = df[i].var()
        desvio_padra = df[i].std()
        minimo = df[i].min()
        maximo = df[i].max()
        print(f\"{i}: mínimo {minimo}, máximo {maximo} variância {variancia:.4f} e desvio padrão {desvio_padra:.4f})
    """,
    name="_"
)


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
        'Frequência Absoluta': freq_abs.values.round(2)
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


if __name__ == "__main__":
    app.run()
