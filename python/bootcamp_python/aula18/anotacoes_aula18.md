Estrutura Tipagem com Pydant:
  - importar BaseModel do Pydantic
  - criar classe da tabela instanciando dentro dela a clase BaseModel do Pydantic
    - tipar dados
    - class_confi: orm = True

Estrutura get API:
  - importar lib requests
  - fazer o get com a url da api
  - trazer o json que veio no get para uma response
  - pegar as partes que importam e depois trabalhar com dicionarios ou listas (json >> dict >> lista/banco/etc)



MVC (Model, View, Controller)
  - 
  - 
  - 








Possiveis Erros 

1 - Pydantic

1.1 - ValidationError: 1 validation error for PokemonSchema
name
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='arbok', input_type=str]
    For further information visit https://errors.pydantic.dev/2.6/v/int_parsing

    voltar nos 35m da aula 18

MVC (model, view, control) no caso do projeto:
  - db.py > deixa os comandos de engine e acessoa o banco apartado do model por questao de seguranca
  - model > banco de dados, definicoes das classes das tabelas
  - view > schema (visao de como os dados chegam, poderia ser um dashboard tambem)
  - controller
  - arquivo main que roda tudo isso

	

obs:
backfill - alimentar uma base retroativamente por adicao de coluna por exemplo
salvar json bruto pra preservar os dados brutos