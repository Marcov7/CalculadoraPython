from typing import Union
from fastapi import FastAPI
import math

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id = ": item_id + 100, "q = ": q}


@app.get("/calculadora1/{item_id1}/{item_id2}/{operacao}")
def calculadora1(item_id1: int, item_id2: int, operacao: str):
    if operacao == "ADD":
        return ({"operação": "ADD"},  {"resultado":item_id1 + item_id2})  
    elif operacao == "SUB":
        return ({"operação": "SUB"},  {"resultado":item_id1 - item_id2})    
    elif operacao == "PRO":
        return ({"operação": "PRO"},  {"resultado":item_id1 * item_id2})  
    elif operacao == "DIV":
        return ({"operação": "DIV"},  {"resultado":item_id1 / item_id2})   
    else:
        return {"ERR", 0}
    
    
@app.get("/calculadora2/{item_id1}/{item_id2}/{operacao}")
def calculadora2(item_id1: int, item_id2: int, operacao: str):
    if operacao == "POW":
        return ({"operação": "POW"},  {"resultado": math.pow(item_id1, item_id2)}) 
    elif operacao == "LOG": 
        return ({"operação": "LOG"},  {"resultado": math.log(item_id1, item_id2)}) 
    elif operacao == "SQRT":
        return ({"operação": "SQRT"}, {"resultado": math.pow(item_id1, 1/item_id2)})  
    elif operacao == "MOD":
        return ({"operação": "MOD"},  {"resultado": item_id1 % item_id2})  
    else:
        return {"ERR", 0}