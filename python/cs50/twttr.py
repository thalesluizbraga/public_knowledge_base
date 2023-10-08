# When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, 
# much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the
# user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether 
# inputted in uppercase or lowercase.

vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
sentence_input = str(input('Input:')).strip()
sentence_output = ''

for s in sentence_input:
    if s not in vowels:
        sentence_output += s

print('Output:',sentence_output)