from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # instancia da classe FastAPI

class item(BaseModel): # criacao da classe item herdando as caracteristicas da classe BaseModel
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get('/') # decorador get puxando as caracteristicas get da classe FastAPI dentro da variavel app
def read_root():
    return{'e ai otario'}

@app.get('items/{item_id}')
def read_item(item_id:int, q:Union[str,None]=None):
    return{'item_id':item_id, 'q':q}

@app.put('items/{item_id}')
def update_item(item_id:int, item: item):
    return{'item_name': item.name, 'item_id':item_id}