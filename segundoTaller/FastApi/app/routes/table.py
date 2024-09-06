from fastapi import APIRouter, Body
from models.table_schema import Table
from database import TableModel

table_route = APIRouter()

@table_route.post("/")
def create_tables(table: Table = Body(...)):
    TableModel.create(color=table.color, size=table.size, numberPeople=table.numberPeople)
    return {"message": "Table created successfully"}

@table_route.get("/")
def get_tables():
    table = TableModel.select().where(TableModel.id > 0).dicts()
    return list(table)

@table_route.get("/{table_id}")
def get_table(table_id: int):
    try:
        table = TableModel.get(TableModel.id == table_id)
        return table
    except TableModel.DoesNotExist:
        return {"error": "Table not found"}
    
@table_route.put("/{id}")
def update_tables(id: int, table: Table = Body(...)):
    try:
        table_update = TableModel.get(TableModel.id == id)
        table_update.size = table.size
        table_update.color = table.color
        table_update.numberPeople = table.numberPeople
        table_update.save() 
        return {"message": "{id} updated"}
    except TableModel.DoesNotExist:
        return {"error": "Failed to update "}

@table_route.delete("/{id}")
def delete_tables(id: int):
    try:
        table = TableModel.get(TableModel.id == id)
        table.delete_instance()
        return {"message": f"{id} eliminated"}
    except TableModel.DoesNotExist:
        return {"error": "Table not found"}
    