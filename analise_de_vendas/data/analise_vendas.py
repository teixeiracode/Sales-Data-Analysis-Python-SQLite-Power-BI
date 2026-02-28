import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# -------- gerar dataset -------- #

def gerar_dataset():
    if not os.path.exists("data"):
        os.makedirs("data")

    np.random.seed(42)
    n = 1000

    produtos = ['Notebook', 'Celular', 'Fone', 'Monitor', 'Teclado']
    cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Salvador']

    df = pd.DataFrame({
        'id_venda': range(1, n+1),
        'data': pd.date_range(start='2023-01-01', periods=n, freq='D'),
        'produto': np.random.choice(produtos, n),
        'cidade': np.random.choice(cidades, n),
        'quantidade': np.random.randint(1, 5, n),
        'valor_unitario': np.random.randint(100, 5000, n)
    })

    df['faturamento'] = df['quantidade'] * df['valor_unitario']

    df.to_csv("data/vendas.csv", index=False)
    print("✅ Dataset criado com sucesso!")



# -------- carregar dados -------- #

def carregar_dados():
    return pd.read_csv("data/vendas.csv")


 
# -------- calcular métricas -------- #

def calcular_metricas(df):
    faturamento_total = df['faturamento'].sum()
    ticket_medio = df['faturamento'].mean()

    produto_top = df.groupby('produto')['quantidade'].sum().sort_values(ascending=False)
    cidade_receita = df.groupby('cidade')['faturamento'].sum().sort_values(ascending=False)

    print("\n📊 MÉTRICAS PRINCIPAIS")
    print("Faturamento Total: R$", round(faturamento_total, 2))
    print("Ticket Médio: R$", round(ticket_medio, 2))

    print("\n📦 Produto mais vendido:")
    print(produto_top)

    print("\n🌎 Receita por cidade:")
    print(cidade_receita)

    return cidade_receita



# --------- gerar gráficos -------- #

def gerar_graficos(cidade_receita):
    cidade_receita.plot(kind='bar')
    plt.title('Receita por Cidade')
    plt.ylabel('Faturamento')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



# --------- função principal -------- #

def main():
    gerar_dataset()
    df = carregar_dados()
    cidade_receita = calcular_metricas(df)
    gerar_graficos(cidade_receita)


if __name__ == "__main__":
    main()