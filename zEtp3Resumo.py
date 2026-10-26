import pandas as pd
from rich.panel import Panel
from Etp1CarregarDados import CAMINHO_CSV_ORIGINAL
from Etp2Formatacao import console, numero_br


def mostrar_resultado(df):
    total_registros = len(df)
    total_vendas = df["CO_ID"].nunique()
    total_clientes = df["CL_ID"].nunique()
    total_produtos = df["PR_ID"].nunique()

    texto = (
        f"[bold] Registros: [/] {numero_br(total_registros)}\n"
        f"[bold] Vendas: [/] {numero_br(total_vendas)}\n"
        f"[bold] Clientes: [/] {numero_br(total_clientes)}\n"
        f"[bold] Produtos: [/] {numero_br(total_produtos)}\n"
    )

    console.print(Panel(texto, title="Varejo", expand=False))


if __name__ == "__main__":
    # 1. Carrega os dados usando o caminho que você já importou
    df_original = pd.read_csv(CAMINHO_CSV_ORIGINAL)

    # 2. Executa a função para mostrar o painel estilizado no terminal
    mostrar_resultado(df_original)

    # 3. Se ainda quiser ver as primeiras linhas no terminal:
    print("\nPrimeiras linhas do DataFrame:")
    print(df_original.head())