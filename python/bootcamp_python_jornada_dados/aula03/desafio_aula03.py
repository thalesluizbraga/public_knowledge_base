
#%% 
while True:
    name =  input('Insira seu nome: ')
    if len(name) == 0 or name.isspace() or any(char.isdigit() for char in name):
        print('Digite um nome valido contendo apenas letras e com algum caractere')
    else:
        salary = float(input('Insira seu salario: ')) 
        if salary < 0:
            print('Digite um salario valido com apaenas numeros')
        else:
            bonus = float(input('Insira seu multiplo de bonus: '))
            if bonus < 0:
                print('Digite um bonus valido com apenas numeros')
            else:
                result = salary * bonus
                print(f'Seu salario é {salary}, seu multiplo de bonus é {bonus}, resultando um bonus de {result}') 
                break    

# %%

while True:
    try:
        name =  input('Insira seu nome: ')
        if len(name) == 0 or name.isspace() or any(char.isdigit() for char in name):
            print('Digite um nome valido contendo apenas letras e com algum caractere')
            continue # Volta para o inicio do loop pedindo o nome novamente
        
        salary = float(input('Insira seu salario: ')) 
        if salary < 0:
            print('Digite um salario valido com apaenas numeros')
            continue
        
        bonus = float(input('Insira seu multiplo de bonus: '))
        if bonus < 0:
            print('Digite um bonus valido com apenas numeros')
            continue
        
        result = salary * bonus
        print(f'Seu salario é {salary}, seu multiplo de bonus é {bonus}, resultando um bonus de {result}') 
        break    
    
    except ValueError:
        print('Erro: Por favor, insira um número válido para salário e bônus.')

# %%
