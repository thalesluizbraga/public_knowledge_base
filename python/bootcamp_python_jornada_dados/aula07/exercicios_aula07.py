#%%

# 1 - Calcular Média de Valores em uma Lista
lista = [1,2,3,4,5]
def calcular_media_valores_lista(lista : list ) -> float:
    return sum(lista) / len(lista)

calcular_media_valores_lista(lista)

#%%

# 2 - Filtrar Dados Acima de um Limite
valores_acima_3 = []
def filtrar_dados_acima_3(lista: list, limite : float) -> list:
    for i in lista:
        if i > limite:
            valores_acima_3.append(i)
    return valores_acima_3

filtrar_dados_acima_3(lista, limite=3)

#%%

# 3 - Contar Valores Únicos em uma Lista
lista2 = [2,20,20,4,5,5,5,5]

def valores_unicos_lista(lista: list):
    return set(lista)

valores_unicos_lista(lista2)

#%%

# 4 - Calcular Desvio Padrão de uma Lista
import numpy as np

def calcular_std(lista: list) -> float: 
    return np.std(lista)

calcular_std(lista2)



