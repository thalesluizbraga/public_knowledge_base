# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y,  wherein each of X and Y is an integer, - OK
# and then outputs, as a percentage rounded to the nearest integer,
# how much fuel is in the tank. If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. And if 99% or more remains, output F instead to indicate that the tank is essentially full. - OK
# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.


def convert(fraction):
    if "/" in fraction:
        x, y = fraction.split("/")
        if int(x) > int(y) and int(y) != 0: raise ValueError()
        else:
            div = int(x) / int(y)
            return round(div * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

def main():
    print(gauge(convert(input("Fraction: "))))

if __name__ == "__main__":
    main()



