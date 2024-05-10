#%% 
import requests
from pydantic import BaseModel

# Criando a classe PokemonSchema que herda as funcionalidades da classe BaseModel da lib pydantic
class PokemonSchema(BaseModel):
    name: str # tipagem de dados
    type: str 

    class Config:
        orm_mode = True
    
def get_pokemon(id: int) -> PokemonSchema:
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    data = response.json()
    print(data)
    data_types = data['types']  # Supondo que 'data' é o dicionário com os dados do Pokémon
    types_list = []
    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon/15'
    pokemon = get_pokemon(24)
    print(pokemon)



# %%
