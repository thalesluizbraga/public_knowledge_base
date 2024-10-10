### Desafio - Refatorar o projeto da aula anterior evitando Bugs!

# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

 
 # %%
#x
#resultado = salary * bonus
try:
    name =  input('Insira seu nome: ')
    if len(name) == 0 or name.isspace():
        print('O nome deve ter alguma letra')
    elif any(char.isdigit() for char in name):
        print('O nome deve conter apenas letras')
except:
    print('Alguma coisa esta errada com o nome')

try:
    salary = float(input('Insira seu salario: '))
    if salary == 0:
        print('O salario deve ser um numero maior do que zero')
except:
    print('Alguma coisa esta errada com o salario')

try:
    bonus = float(input('Insira seu multiplo de bonus: '))
    if bonus == 0:
        print('O multiplo de bonus deve ser maios do que zero')
    else:
        result = salary * bonus
        print(f'Seu salario é {salary}, seu multiplo de bonus é {bonus}, resultando um bonus de {result}') 
except:
    print('Alguma coisa esta errada com o multiplo de bonus')


# %%
