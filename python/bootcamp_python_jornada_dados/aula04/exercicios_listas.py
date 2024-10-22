#%%

# Lista de números ao quadrado
numeros = [2,3,4,5]
for num in numeros:
    quadrados = num**2
    print(quadrados)

# %%

# Adicionar elemento em uma lista
nomes = ['thales', 'thaian', 'maria lais']
nomes.append('mari')
print(nomes)

#%%

# Contar ocorrências de caracteres
contagem = []
for n in nomes:
    contagem.append(len(n))
print(contagem)

# %%

#1. Soma de Elementos
#Escreva um programa que receba uma lista de números e retorne a soma de todos os elementos.
print(sum(numeros))

#%%

#2. Média dos Elementos
#Escreva um programa que receba uma lista de números e retorne a média dos elementos.
print(sum(numeros)/len(numeros))


#%%

#3. Contar Ocorrências de um Elemento
#Escreva um programa que receba uma lista e um número e retorne quantas vezes esse número aparece na lista.

# Adicionando mais numeros na lista. O append adiciona um por vez e o extend mais de um 
#numeros.extend([5,5])

# Contar quantas vezes aparece o numero 5

num_5 = 1
for n in numeros:
    if n == 5:
        num_5 += 1
print(numeros)
print(num_5)

#%%

#6. Remover Duplicatas
#Escreva um programa que receba uma lista e remova todos os elementos duplicados, retornando uma lista apenas com os elementos únicos.
set(numeros)


#%%

#7. Inverter a Lista
#Escreva um programa que inverta a ordem dos elementos de uma lista.
numeros.reverse()
numeros

#%%

#8. Listar Números Pares
#Escreva um programa que receba uma lista de números e retorne apenas os números pares dessa lista.

num_pares = []
for n in numeros:
    if n % 2 ==0 :
        num_pares.append(n)
print(num_pares)


#%%

#9. Concatenação de Listas
#Escreva um programa que receba duas listas e retorne a concatenação dessas duas listas.
lista1 = ['a', 'b', 'c', 'd']
lista2 = [1,2,3,4,5]

print(lista1 + lista2)



#%%

#10. Substituir Elementos por Zero
#Escreva um programa que substitua todos os números negativos de uma lista por zero.

lista_negativos = [1,-1,2,-2,3,-3]

# com lambda
list(map(lambda x: 0 if x < 0 else x, lista_negativos))

# com loop for 
for i in range(len(lista_negativos)):
    if lista_negativos[i] < 0:
        lista_negativos[i] = 0

# com list comprehension
lista_negativos = [0 if x < 0 else x for x in lista_negativos]
print(lista_negativos)

# %%
