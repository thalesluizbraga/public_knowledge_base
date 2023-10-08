# Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a 
# tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each
# of X and Y is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in 
# the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if
# 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not
# necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))

        if (y == 0) or (x > y): # Condiçoes do or entre parenteses pra nao dar ruim.
            raise ValueError # Condiçao forte 

        fuel_percentage = (x / y) * 100

        if fuel_percentage <= 1:
            return 'E'
        elif fuel_percentage >= 99:
            return 'F'
        else:
            return str(round(fuel_percentage)) + '%'

    except (ValueError, ZeroDivisionError):
        print('Invalid input. Please enter a valid fraction (X/Y).')
        return None


def main():
    while True:
        fraction = input('Enter a fraction (X/Y): ')
        fuel_status = calculate_fuel_percentage(fraction)

        if fuel_status is not None:
            print(fuel_status)
            break


if __name__ == '__main__':
    main()

# Se tiver mais de uma funçao pra chamar na main() ela vai confundir, entao por isso tem que usar essa expressao
# Aqui o try/except ficar fora do loop, porque eu so quero validar uma regra, e nao continuar recebendo um resultado dentro do loop (um counter por exemplo)

