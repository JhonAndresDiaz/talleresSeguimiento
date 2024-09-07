from fastapi import APIRouter, Body
from models.cat_schema import Cat
from database import CatModel

cat_route = APIRouter()

@cat_route.post("/")
def create_cats(cat: Cat = Body(...)):
    CatModel.create(name=cat.name, gender=cat.gender, age=cat.age)
    return {"message": "Cat created successfully"}
    
@cat_route.get("/")
def read_cats():
    return [{"name": "ludwin"}, {"agender": "masculine"}]

@cat_route.get("/{id}")
def read_cats(id: int):
    return {"id": id}

@cat_route.put("/{id}")
def update_cats(id: int, cat: Cat = Body(...)):
    try:
        cat_update = CatModel.get(CatModel.id == id)
        cat_update.name = cat.name
        cat_update.gender = cat.gender
        cat_update.age = cat.age
        cat_update.save() 
        return {"message": "{id} updated"}
    except CatModel.DoesNotExist:
        return {"error": "Failed to update "}

@cat_route.delete("/{id}")
def cats(id: int):
    try:
        cat = CatModel.get(CatModel.id == id)
        cat.delete_instance()
        return {"message": f"{id} eliminated"}
    except CatModel.DoesNotExist:
        return {"error": "Cat not found"}
