#In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, 
#as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is 
#essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full.

#If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) 
#Be sure to catch any exceptions like ValueError or ZeroDivisionError.

# prompt the user - ok
# x is int - ok
# y is int - ok
# result = x/y as percentage - ok
# if result <= 1: return 'E' - ok
# if result >= 99% return 'F' - ok
# valueError for x or y which is not int - ok
# ZeroDivisionError for x/y where x is 0 - ok



def division(gas):
    gas_split = gas.split('/')
    
    try:
        if gas_split[0].isdigit() and gas_split[1].isdigit() and int(gas_split[1]) !=0:
            result = round(int(gas_split[0]) / int(gas_split[1]) * 100,2)
        
        else:
            ValueError

    except:
        raise (ValueError, ZeroDivisionError) 
        # mais de uma exception fica entre parenteses.E o ZeroDivisionError acusa quando o denominador é zero.
    
    return result


def empty_fuel(result):   
    match result:
        case 99.0:
            return 'F'
        case 1.0:
            return 'E'
        case _: # É o else  
            return f'{result}%'


def main():
    gas = input('How much gas is in the tank?')
    result = division(gas)
    print(empty_fuel(result))

  
if __name__ == '__main__':
    main()


