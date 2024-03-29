#%%
import requests

def get_pokemon(url: str) -> list:
    request = requests.get(url)
    response = request.json()

    data = response['types']
    types_list = []

    for d in data:
        types_list.append(d['type']['name'])

    return types_list

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/15' # url para busca dos dados do pokemon numero 15
    print(get_pokemon(url))
    

# %%
