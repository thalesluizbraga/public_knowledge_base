import random


def get_level():

    while True:
        try:
            level = int(input('Level: '))

            if level in [1,2,3]:
                return level
            else:
                continue

        except ValueError:
            pass # Porque faz um pass aqui?

def generate_integer(level):
    if level == 1:
        x, y = random.randint(0, 9), random.randint(0, 9)
    elif level == 2:
        x, y = random.randint(10, 99), random.randint(10, 99)
    elif level == 3:
        x, y = random.randint(100, 999), random.randint(100, 999)
    else:
        print('Invalid level')

    return x, y

def main():
    count = 10
    level = get_level()
    wrong_answers = 0
    right_answers = 0

    while count > 0:

        x,y = generate_integer(level)
        print(f"{x} + {y}")
        answer = int(input('Answer: '))

        if answer != x + y:
            wrong_answers += 1
            print('EEE')
            if wrong_answers == 3:
                print( x + y)
        else:
            right_answers += 1

        count -= 1

    print('Your score is:', right_answers)

# Tem que fazer um counter dentro do while pra ir diminuindo ate a decima jogada e depois somar o score (sendo cada jogada valendo um ponto)

if __name__ == '__main__':
    main()