#%%

# Calculadora Simples

#Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário.
# Use try-except para lidar com divisões por zero e entradas não numéricas. Utilize if-elif-else para realizar a
# operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.


def calculator(x,operator, y):

    try:
        if not (isinstance(x,(float, int)) and isinstance(y,(float,int))):
            return 'x e y precisam ser numeros.'
        else:
            if operator == '+':
                return x + y 
            elif operator == '-':
                return x - y
            elif operator == '/':
                return x / y
            elif operator == '*':
                return x * y
    except ZeroDivisionError:
        return 'Um numero nao pode ser dividido por zero.'

print(calculator(2,'+',0))


    
# %%

# Classificador de Números
#Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para 
#classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".


def classificador(num):
    
    try:
        if (num > 0) and (num %2 == 0):
            return 'positivo e par'
        elif (num > 0) and (num %2 != 0):
            return 'positivo e impar'
        elif num < 0 and (num %2 == 0):
            return 'negativo e par'
        elif num < 0 and (num %2 != 0):
            return 'negativo e impar'
        elif num == 0:
            return 'zero'
    except TypeError:
        'Input nao é um numero'

print(classificador('a'))

# %%

# Conversão de Tipo com Validação

# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de 
# entrada em uma lista de números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada 
# elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de 
# erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.


def validacao(list_num):

    try:
        for num in range(len(list_num)): # para iterar em listas vai ser sempre for i in range(len()):
            list_num[num] = int(list_num[num])
            return list_num 
    except:
        return 'conversao falhou'


print(validacao(['1','2','3']))



# %%
