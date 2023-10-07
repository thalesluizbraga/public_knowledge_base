#%%
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


# %%
