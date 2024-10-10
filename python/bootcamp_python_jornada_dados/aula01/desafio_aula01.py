# Escreva um programa que 
    # Peça ao usuario que digite seu nome
    # Peça ao usuario que digite o valor do seu salario e converta o valor para float
    # Peça ao usuario que digite o valor do bonus recebido e converta o valor para float
    # Calcule o valor do bonus
    # Printe o valor do resultado do calculo para o usuario
    # Printe uma mensagem falando o nome do usuario, salario e bonus

#%%
name = input('Informe seu nome: ')
salary = float(input('Informe seu salario: '))
bonus = float(input('Informe o fator de bonus: '))
result = salary * bonus
print(f'{name}, com seu salario de {salary}, seu bonus é de {result}')


# %%
