# In a file called game.py, implement a program that:

# Prompts the user for a level,n. If the user does not input a positive integer, the program should prompt again.
# Randomly generates an integer between 1 and n, inclusive, using the random module.
# Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
# If the guess is larger than that integer, the program should output Too large! and prompt the user again.
# If the guess is the same as that integer, the program should output Just right! and exit.

import random

def get_valid_value():

    while True:
        try:
            level = int(input('Type a level: '))
            if level > 0:
                return level
            else:
                print('Invalid level')
        except ValueError:
            print('Invalid type')

def play_game(level):
    rdm = random.randint(1,level)

    while True:
        try:
            guess = int(input('Guess: '))
            if guess > rdm:
                print('Too large!')
            elif guess < rdm:
                print('Too small!')
            else:
                print('Just right!')
                break
        except ValueError:
            print('Invalid type')

def main():
    level = get_valid_value()
    play = play_game(level)

if __name__ == '__main__':
    main()