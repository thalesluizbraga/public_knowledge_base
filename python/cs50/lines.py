# importar sys - ok
# se len(argv) < 2:
    # return 'Too few arguments'
# se len(argv) > 2:
    # return 'Too many arguments'
# se arquivo nao encontrado no diretorio:
    # raise FileNotFoundError


# clausula with para iniciar o contexto de leitura do arquivo (tipo 'r') - ok
# Se row is blank: - ok
    # nao contar - ok
# Se row begins with # - ok
    # nao contar
# contar linhas - ok

#import sys
#

#print(count)

import sys

def get_arg():

    if len(sys.argv) > 2:
        return 'Too many arguments.'
    elif len(sys.argv) < 2:
        return 'Too few arguments.'
    elif not sys.argv[1].endswith('.py'):
        return 'Not a python file.'
    else:   
        return sys.argv[1]
    
            
if __name__ == '__main__':
    arg = get_arg()
    
    try:

        with open(arg, 'r') as file:
            count = 0    
            for row in file:
                if row.startswith('#'):
                    continue
                elif row.isspace():
                    continue
                else: 
                    count += 1
                    
        print(f'Total of lines in file: {count}')

    except FileNotFoundError:
        raise 'File not Found.'



