#Funções
#Ler CSV:
#
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

import csv


with open('../vendas.csv', 'r') as file:   
    reader = csv.DictReader(file)

for row in reader:
    key = row[0]
    values = row[1]

    dict_vendas: dict = {} 

print(dict_vendas)     


# %%

import csv


def csv_to_dict(file_path):
    data_dict = {}
    with open(file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        # Assuming the first row contains the column headers
        headers = next(csv_reader)
        for row in csv_reader:
            # Assuming the first column contains the keys
            key = row[0]
            # Assuming the remaining columns contain the values
            values = row[1:]
            # Create a dictionary using the headers as keys and row values as values
            row_dict = dict(zip(headers[1:], values))
            # Add the row dictionary to the data dictionary using the key
            data_dict[key] = row_dict
    return data_dict

# Example usage:
file_path = 'vendas.csv'  # Path to your CSV file
result_dict = csv_to_dict(file_path)
print(result_dict)
