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

dict_a: dict = {'item': 'bike', 'qtd': 1}
dict_b: dict = {'item': 'shoes' ,'qtd': 3}
# dict_merged: dict = dict_a | dict_b # Se fizer assim, o dict_b sobrepoe o dict_a... nao da certo 
dict_merged: dict = {**dict_a, **dict_b}
print(dict_a)
print(dict_b)
print(dict_merged)

# %%

# 3 Iterating Through Dictionaries:

# Iterate through the combined inventory dictionary from
# the previous exercise and print each item along with its
# quantity.

for k in dict_merged.items():
    print(k)    
# %%
