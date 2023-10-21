# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the
# user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether 
# inputted in uppercase or lowercase.


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    word_output = ''

    for letter in word:
        if letter not in vowels:
            word_output += letter

    return word_output

def main():
    word = str(input('Input:')).strip()
    shorten_word = shorten(word)


    print('Output:',shorten_word)



if __name__ == "__main__":
    main()