#%%

# 1 Creating and Accessing Dictionaries:
# Create a dictionary representing a person with keys for name, age, and city. Access and print each 
# value individually.

dict1: dict = {'name' : 'thales', 'age': 28, 'city': 'uberlandia'}

print(dict1['name'])
print(dict1['age'])
print(dict1['city'])

# %%

#2 - Dictionary Operations:
#Create two dictionaries representing the inventory of two 
#stores, each with items and their respective quantities.
# Merge these dictionaries into a single dictionary 
#representing the combined inventory of both stores.

dict_a: dict = {'shoes': 10, 'bike': 1, 'abc':123}
dict_b: dict = {'hat': 4 , 'ball': 3} # A chave tem que ser unica sempre, se nao vai ser sobreposta pelo registro posterior sempre
dict_merged: dict = dict_a | dict_b
print(dict_merged)
# o merge acontece mesmo com dicionarios de tmanho diferentes


# %%

# 3 Iterating Through Dictionaries:

# Iterate through the combined inventory dictionary from
# the previous exercise and print each item along with its
# quantity.

for k in dict_merged.items():
    print(k)    

# %%
# 4- Dictionary Manipulation:
# This exercise involves adding, updating, and removing items
# from a dictionary, which requires understanding basic dictionary
# manipulation methods.

# Adding
dict_a['chave_nova'] = 'valor_novo'

# Updating
dict_1 = {'A': 123, 'B': 789}
dict_2 = {'A': 178, 'B': 117}
dict_1.update(dict_2) 
# por conta de ser a mesma chave, o novo valor é atualizado, se for chave diferente,
# ele faz um merge

# Removing
dict_1.pop('A') # passa a chave do que é pra ser removido
dict_1

# %%

#5 - Word Frequency Counter: Write a function that takes a list of words as input and returns a dictionary where the keys are the 
#words and the values are the frequencies of those words in the list.

def frequency_count(word_list: list) -> dict:

    dict_new: dict = {}
    chave: list = []
    valor: list = []

    for w in words_list:
        if w not in chave:
            chave.append(w)
            valor.append(1)
        else:
            index = chave.index(w)
            valor[index] += 1

    for i in range(len(chave)):
        dict_new[chave[i]] = valor[i]
    
    return dict_new

words_list: list = ['isso', 'e', 'um', 'teste', 'teste']        
print(frequency_count(words_list))

#%%

# 6 - Unique Values: Write a function that takes a dictionary as input and returns a 
# list of unique values from that dictionary.

def unique_values(dict_m: dict) -> list:
    return list(set(dict_m.values()))

dict_m = {'ala': 124, 'mama': 448, 'papa': 552}
print(unique_values(dict_m))

# %%

#Value Lookup: Write a function that takes a dictionary and a value as input, 
# and returns a list of keys that map to that value in the dictionary.



#
#Invert Dictionary: Write a function that takes a dictionary as input and returns a 
#new dictionary where the keys and values are swapped.
#
#Nested Dictionaries: Write a function that takes a dictionary with nested dictionaries as input and returns a flattened dictionary where the keys are concatenated with a separator.
#
#Dictionary Sorting: Write a function that takes a dictionary as input and returns a new dictionary sorted by keys or values in ascending or descending order.
#
#Dictionary Filtering: Write a function that takes a dictionary and a predicate function as input and returns a new dictionary containing only the key-value pairs that satisfy the predicate.
#
#Dictionary Intersection: Write a function that takes two dictionaries as input and returns a new dictionary containing only the key-value pairs that are common to both dictionaries.
#
#Dictionary Grouping: Write a function that takes a list of dictionaries as input and returns a new dictionary where the keys are unique values found across all dictionaries, and the values are lists of dictionaries containing that key.
# %%
