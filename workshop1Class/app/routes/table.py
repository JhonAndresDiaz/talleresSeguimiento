from fastapi import APIRouter, Body
from models.table_schema import Table

table_route = APIRouter()

@table_route.post("/")
def create_tables(table: Table = Body(...)):
    try:
        return table
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@table_route.get("/")
def read_tables():
    return [{"color": "red"}, {"size": "big"}]

@table_route.get("/{id}")
def read_tables(id: int):
    return {"id": id}

@table_route.put("/{id}")
def update_tables(id: int):
    return {"id": id}

@table_route.delete("/{id}")
def delete_tables(id: int):
    return {"id": id}
