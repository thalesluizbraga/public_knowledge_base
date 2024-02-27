# importar sys
# importar csv???
# se len(argv) < 2:
    # return 'Too few arguments'
# se len(argv) > 2:
    # return 'Too many arguments'
# se arquivo nao encontrado no diretorio:
    # raise FileNotFoundError
# clausula with para iniciar o contexto de leitura do arquivo (tipo 'r')
# Se row is blank:
    # nao contar
# Se row begins with #
    # nao contar
# contar linhas

import sys

with open('C:/Users/Thales/Documents/repos/public_knowledge_base/python/cs50/lines.txt', 'r') as file:
    count = 0
    
    for row in file:
        if row.startswith('#'):
            continue
        elif row.strip():
            continue
        else: 
            count += 1

print(count)




