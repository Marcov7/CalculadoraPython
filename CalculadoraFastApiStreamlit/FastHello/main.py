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


@app.get("/calculadoraCircuferencia/{item_id1}/{operacao}")
def calculadoraCircuferencia(item_id1: int, item_id2: int, operacao: str):
    if operacao == "AREA":
        return ({"operação": "AREA"},  {"resultado": math.pi * math.pow(item_id1, 2)}) 
    elif operacao == "PERIMETER":
        return ({"operação": "PERIMETER"},  {"resultado": 2 * math.pi * item_id1})


@app.get("/calculadoraTriangulo/{item_id1}/{item_id2}/{item_id3}/{operacao}")
def CalculadoraTriangulo(item_id1: int, item_id2: int, item_id3: int, operacao: str):
    if operacao == "AREA":
        SemiPerimetro = acharPerimetroDoTriangulo(item_id1, item_id2, item_id3)/2
        return ({"operação": "AREA"},  {"resultado": math.sqrt(SemiPerimetro * (SemiPerimetro - item_id1) * (SemiPerimetro - item_id2) * (SemiPerimetro - item_id3))})
    elif operacao == "PERIMETER":
        return ({"operação": "PERIMETER"},  {"resultado": acharPerimetroDoTriangulo(item_id1, item_id2, item_id3)})

    
def acharPerimetroDoTriangulo(lado1: int, lado2: int, lado3: int):
    return lado1 + lado2 + lado3