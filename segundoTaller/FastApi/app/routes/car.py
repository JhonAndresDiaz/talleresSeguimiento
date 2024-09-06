from fastapi import APIRouter, Body
from models.car_schema import Car
from database import CarModel

car_route = APIRouter()

@car_route.post("/")
def create_cars(car: Car = Body(...)):
    CarModel.create(color=car.color, amount=car.amount, price=car.price, year=car.year)
    return {"message": "Car created successfully"}
    
@car_route.get("/")
def read_cars():
    return [{"color": "blue"}, {"amount": "four"}]

@car_route.get("/{id}")
def read_cars(id: int):
    return {"id": id}

@car_route.put("/{id}")
def update_cars(id: int, car: Car = Body(...)):
    try:
        car_update = CarModel.get(CarModel.id == id)
        car_update.color = car.color
        car_update.amount = car.amount
        car_update.price = car.price
        car_update.year = car.year
        car_update.save() 
        return {"message": "{id} updated"}
    except CarModel.DoesNotExist:
        return {"error": "Failed to update "}

@car_route.delete("/{id}")
def delete_cars(id: int):
    try:
        car = CarModel.get(CarModel.id == id)
        car.delete_instance()
        return {"message": f"{id} eliminated"}
    except CarModel.DoesNotExist:
        return {"error": "Car not found"}
