from fastapi import FastAPI, Body
from starlette.responses import RedirectResponse
from routes.user import user_route
from routes.table import table_route
from routes.shirt import shirt_route
from routes.cat import cat_route
from routes.car import car_route

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

app.include_router(user_route, prefix="/users", tags=["Usuarios"])
app.include_router(table_route, prefix="/table", tags=["Tablas"])
app.include_router(shirt_route, prefix="/shirts", tags=["Camisas"])
app.include_router(cat_route, prefix="/cats", tags=["Gatos"])
app.include_router(car_route, prefix="/cars", tags=["Carros"])