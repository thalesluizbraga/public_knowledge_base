#Função: ler_csv
#Entrada: Nome do arquivo CSV
#Saída: Lista de dicionários com dados lidos
#Processar Dados:
#
#Função: processar_dados
#Entrada: Lista de dicionários
#Saída: Dicionário processado conforme descrito
#Calcular Vendas por Categoria:
#
#Função: calcular_vendas_categoria
#Entrada: Dicionário processado
#Saída: Dicionário com total de vendas por categoria

import pandas as pd

def read_csv(path) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

def calcular_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df1 = df[['Venda', 'Categoria']].groupby('Categoria').sum().reset_index()
    return df1 


if __name__ == '__main__':
    path = 'vendas.csv'
    df = read_csv(path)
    df1 = calcular_vendas(df)
    print(df1)


