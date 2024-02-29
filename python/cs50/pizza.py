
import sys

def get_arg():

    if len(sys.argv) > 2:
        return 'Too many arguments.'
    elif len(sys.argv) < 2:
        return 'Too few arguments.'
    elif not sys.argv[1].endswith('.csv'):
        return 'Not a CSV file.'
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
