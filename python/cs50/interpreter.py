# Python already supports math, whereby you can write code to add, subtract, multiply, or divide values and even 
# variables. But let’s write a program that enables users to do math, even without knowing Python.

# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then
#  calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the 
# user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# x is an integer
# y is +, -, *, or /
# z is an integer
# For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.
 
# Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!


def main():
    expression = input("Enter the expression (e.g., 10 + 5): ")
    operands = expression.split()

    if len(operands) != 3:
        print("Invalid expression. Please enter a valid expression.")
        return

    x = float(operands[0])
    operator = operands[1]
    z = float(operands[2])

    result = calculator(x, operator, z)

    if result is not None:
        print('Result:', result)
    else:
        print('Invalid operator. Please enter a valid operator (+, -, *, /).')

def calculator(x, operator, z):
    if operator == '+':
        total = x + z
    elif operator == '-':
        total = x - z
    elif operator == '/':
        total = x / z
    elif operator == '*':
        total = x * z
    else:
        total = None
    return total

main()
