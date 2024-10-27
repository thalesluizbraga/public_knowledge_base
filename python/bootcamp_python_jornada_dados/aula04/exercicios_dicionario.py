#%%

# Verificar tipos de dados em um dicionario
dicionario = {'thales':29, 'thaian': 27, 'maria lais': 26, 'mari': 31}
for key, value in dicionario.items():
    print(type(key))
    print(type(value))


#1. Contar Ocorrências - Crie um programa que conta quantas vezes cada palavra aparece em uma frase e armazene o resultado em um dicionário.

# tenho que contar quantas vezes cada palavra aparece
# tenho que transformar cada palavra em chave
# tenho que alocar a contagem de cada palavra nas chaves como valor

frase = ['eu prefiro praia do que o praia clube']
contagem = []



#%%

#2. Soma dos Valores - Escreva um programa que receba um dicionário onde as chaves são strings e os valores são números. O programa deve calcular a soma de todos os valores numéricos.
dicionario = {'thales':29, 'thaian': 27, 'maria lais': 26, 'mari': 31}
soma = 0 # Contador para armazenar os valores da soma
for value in dicionario.values(): # Loop for para acessar apenas os valores
    soma += int(value)
print(soma)

#%%

#3. Inverter Chaves e Valores - Escreva um programa que receba um dicionário e crie um novo dicionário invertendo as chaves e os valores.

#%%

#4. Atualizar Valores - Escreva um programa que receba um dicionário e aumente em 10% todos os valores que forem numéricos.

for key,value in dicionario.items(): # Tenho que iterar na chave e valor porque vou mudar a estrutura do dicionario com novos valores
    if isinstance(value,int):
        dicionario[key] =  value * 1.1 # pra armazenar a mudança nos valoeres do dicionario tem que passar ele + [key]
print(dicionario)

#%%

#5. Remover Entradas com Valor Específico - Escreva um programa que remova todas as entradas de um dicionário que possuam um valor igual a zero.


remove_list = [] # Lista vazia para receber as chaves a serem deletadas por conta do valor maior que a regra
for key, value in dicionario.items():
    if int(value) > 30:
        remove_list.append(key) # Append das chaves a serem deletadas

for r in remove_list: # Loop que itera na lista com as chaves a serem deletadas
    dicionario.pop(r) # Metodo para deletar do dicionario tudo o que for igual as chaves da lista de delete
dicionario


#%%
#6. Mesclar Dicionários - Crie um programa que receba dois dicionários e os mescle em um só, somando os valores das chaves em comum.
dicionario1 = {'matematica': 10, 'historia': 9, 'artes': 8}
dicionario2 = {'matematica': 9, 'geografia': 7, 'portugues': 6, 'ingles': 10}
dict_merge = dict(dicionario1.items() | dicionario2.items())
print(dict_merge)

for key, value in dicionario1:
    if not key in dicionario2:
        dicionario1.pop(key)


    

#%%

#7. Encontrar a Chave com o Maior Valor
#Escreva um programa que receba um dicionário e retorne a chave que possui o maior valor.
max(dicionario, key=dicionario.get) # Metodo get retorna o valor da chave pedida, que no caso foi a chave com valor max


#%%

#8. Contar Itens em um Dicionário de Listas
#Escreva um programa que receba um dicionário cujos valores são listas e conte quantos itens existem em todas as listas combinadas.

dicionario_lista = {'lista1': [1,2,3,4], 'lista2': ['a', 'b', 'c', 'd']}
contador = 0

for lista in dicionario_lista.values():
    contador += len(lista)
print(contador)

#%%

#9. Adicionar Nova Entrada
#Escreva um programa que receba um dicionário e adicione uma nova chave com um valor fornecido pelo usuário.

dicionario4 = {'manoel':15}
dicionario.update(dicionario4) # Nao preciso atribuir para reescrever no dicionario o novo item, so usar o metodo
dicionario

#%%

#10. Multiplicar Valores por uma Constante
#Escreva um programa que multiplique todos os valores numéricos de um dicionário por uma constante fornecida pelo usuário.

for key,value in dicionario.items(): # Tenho que iterar na chave e valor porque vou mudar a estrutura do dicionario com novos valores
    if isinstance(value,int):
        dicionario[key] =  value * 1.1 # pra armazenar a mudança nos valoeres do dicionario tem que passar ele + [key]
print(dicionario)
