from fastapi import APIRouter, Body
from models.cat_schema import Cat

cat_route = APIRouter()

@cat_route.post("/")
def create_cats(cat: Cat = Body(...)):
    try:
        return cat
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@cat_route.get("/")
def read_cats():
    return [{"name": "ludwin"}, {"agender": "masculine"}]

@cat_route.get("/{id}")
def read_cats(id: int):
    return {"id": id}

@cat_route.put("/{id}")
def update_cats(id: int):
    return {"id": id}

@cat_route.delete("/{id}")
def delete_cats(id: int):
    return {"id": id}
