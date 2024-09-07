from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import database as connection
from database import *
from routes.user import user_route
from routes.table import table_route
from routes.shirt import shirt_route
from routes.cat import cat_route
from routes.car import car_route

@asynccontextmanager
async def lifespan(app: FastAPI):

    if connection.is_closed():
        connection.connect()
        connection.create_tables([UserModel, TableModel, ShirtModel, CatModel, CarModel])

    try:
        yield
    
    finally:
        if not connection.is_closed():
            connection.close

app = FastAPI(lifespan = lifespan)

app.include_router(user_route, prefix="/api/users", tags={"users"})
app.include_router(table_route, prefix="/api/tables", tags={"tables"})
app.include_router(shirt_route, prefix="/api/shirts", tags={"shirts"})
app.include_router(cat_route, prefix="/api/cats", tags={"cats"})
app.include_router(car_route, prefix="/api/cars", tags={"cars"})