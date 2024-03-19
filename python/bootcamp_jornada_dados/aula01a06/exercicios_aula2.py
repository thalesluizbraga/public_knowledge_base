#%%

# Exercício 23: Calculadora Simples

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

#Exercício 24: Classificador de Números
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
