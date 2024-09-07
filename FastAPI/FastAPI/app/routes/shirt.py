from fastapi import APIRouter, Body
from models.shirt_schema import Shirt
from database import ShirtModel

shirt_route = APIRouter()

@shirt_route.post("/")
def create_shirts(shirt: Shirt = Body(...)):
    ShirtModel.create(design=shirt.design, color=shirt.color, typeGarment=shirt.typeGarment, size=shirt.size)
    return {"message": "Shirt created successfully"}
    
@shirt_route.get("/")
def read_shirts():
    return [{"desing": "unic"}, {"color": "green"}]

@shirt_route.get("/{id}")
def read_shirts(id: int):
    return {"id": id}

@shirt_route.put("/{id}")
def update_shirts(id: int, shirt: Shirt = Body(...)):
    try:
        shirt_update = ShirtModel.get(ShirtModel.id == id)
        shirt_update.design = shirt.design
        shirt_update.color = shirt.color
        shirt_update.typeGarment = shirt.typeGarment
        shirt_update.size = shirt.size
        shirt_update.save() 
        return {"message": "{id} updated"}
    except ShirtModel.DoesNotExist:
        return {"error": "Failed to update "}

@shirt_route.delete("/{id}")
def delete_tables(id: int):
    try:
        shirt = ShirtModel.get(ShirtModel.id == id)
        shirt.delete_instance()
        return {"message": f"{id} eliminated"}
    except ShirtModel.DoesNotExist:
        return {"error": "Shirt not found"}