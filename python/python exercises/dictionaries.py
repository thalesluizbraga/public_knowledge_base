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

dict_a: dict = {'shoes': 10, 'bike': 1}
dict_b: dict = {'hat': 4 , 'ball': 3} # A chave tem que ser unica sempre, se nao vai ser sobreposta pelo registro posterior sempre
dict_merged: dict = dict_a | dict_b
print(dict_merged)


# %%

# 3 Iterating Through Dictionaries:

# Iterate through the combined inventory dictionary from
# the previous exercise and print each item along with its
# quantity.

for k in dict_merged.items():
    print(k)    

# %%
# Dictionary Manipulation:
# This exercise involves adding, updating, and removing items
# from a dictionary, which requires understanding basic dictionary
# manipulation methods.

# Adding



# Updating

# Removing

