# Suppose that you’re in the habit of making a list of items you need from the grocery store.
 
# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user
# inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list 
# in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted
# that item. No need to pluralize the items. Treat the user’s input case-insensitively.

def main():

    grocery = {} # A lista fica fora do loop, porque se ficar dentro ela reseta.

    try:
        while True:
            item = input().lower().strip() # Se deixar pra receber a var item fora do while, entra em loop infinito.

            # Nao tem for aqui porque se nao vai considerar a ocorrencia de cada letra [i] e eu quero a ocorrencia de cada palavra.
            grocery[item] = grocery.get(item, 0) + 1

    except EOFError: #Quando ctrl + d for pressionado, para.
        pass

    sorted_grocery = sorted(grocery.items(), key=lambda x: x[0])

    # Print the grocery list in the specified format
    for item, count in sorted_grocery:
        print(f"{count} {item.upper()}")



if __name__ == "__main__":
    main()
