#%%

# Ler o arquivo CSV e carregar os dados.
# Processar os dados em um dicionário, onde a chave é a categoria, e o valor é uma lista de dicionários, cada um contendo informações do produto (Produto, Quantidade, Venda).
# Calcular o total de vendas (Quantidade * Venda) por categoria.

# Desafio usando pandas

# Imports
import pandas as pd

# Definicao de path
path = '../aula07/vendas.csv'

# Funçao Leitura do arquivo
def ler_csv(path):
    df = pd.read_csv(path)
    return df

# Funcao calculo total de vendas
def calcular_total_vendas(df, col_resultado, col1, col2):
    df[col_resultado] = 'NA'
    df[col_resultado] = df[col1] * df[col2]
    return df


# Chamada das funcoes
df = ler_csv(path)
calcular_total_vendas(df, col_resultado = 'Total Vendas', col1 = 'Quantidade', col2 = 'Venda')
df

# %%

# Desafio usando o csv

import csv
lista_csv = []

# Funcao leitura arquivo csv
def ler_arquivo_csv(path, lista):
    with open(path, 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            lista.append(row)
        return lista
    
# Funcao calculo total vendas

for q in lista_csv:
   print(q['Quantidade'])


# Chamda funcoes
print(ler_arquivo_csv(path,lista_csv))

# Acessar as quantidades da lista. Como e uma lista com dicionarios dentro, o esquema é similar ao pandas
for q in lista_csv:
   total_venda = int(q['Quantidade']) * int(q['Venda'])
   print(total_venda)
   lista_csv.append(total_venda)
    

# %%    

# Filtrar produtos entregues
