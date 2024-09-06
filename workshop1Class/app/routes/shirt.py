from fastapi import APIRouter, Body
from models.shirt_schema import Shirt

shirt_route = APIRouter()

@shirt_route.post("/")
def create_shirts(shirt: Shirt = Body(...)):
    try:
        return shirt
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@shirt_route.get("/")
def read_shirts():
    return [{"desing": "unic"}, {"color": "green"}]

@shirt_route.get("/{id}")
def read_shirts(id: int):
    return {"id": id}

@shirt_route.put("/{id}")
def update_shirts(id: int):
    return {"id": id}

@shirt_route.delete("/{id}")
def delete_shirts(id: int):
    return {"id": id}
