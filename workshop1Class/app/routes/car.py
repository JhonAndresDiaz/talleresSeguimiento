from fastapi import APIRouter, Body
from models.car_schema import Car

car_route = APIRouter()

@car_route.post("/")
def create_cars(car: Car = Body(...)):
    try:
        return car
    except Exception as e:
        print(e)
        return {"error:":str(e)}
    
@car_route.get("/")
def read_cars():
    return [{"color": "blue"}, {"amount": "four"}]

@car_route.get("/{id}")
def read_cars(id: int):
    return {"id": id}

@car_route.put("/{id}")
def update_cars(id: int):
    return {"id": id}

@car_route.delete("/{id}")
def delete_cars(id: int):
    return {"id": id}