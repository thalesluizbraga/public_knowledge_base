#%%

# Criar um arquivo csv
# importar a lib csv
# indicar o path
# criar uma lista vazia para receber os dados
# abrir o arquivo como leitura com o contexto with open as
# usar o metodo dictreader criar um leitor csv
# iterar sobre cada linha do leitor  
# adicionar cada iteraçao na lista vazia

import csv

path = 'C:/Users/Thales/Documents/repos/public_knowledge_base/python/bootcamp_python_jornada_dados/aula04/arquivo_aula04.csv'
dados = []

with open(path, mode = 'r') as arquivo: # Aqui eu uso o contexto with, passo o path, indico o modo de leitura e dou um nome para o arquivo
    leitor_csv = csv.DictReader(arquivo)
    for linha in leitor_csv:
        dados.append(linha)    
for registro in dados:
    print(registro)

