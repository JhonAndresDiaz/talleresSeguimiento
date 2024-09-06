from fastapi import APIRouter, Body
from models.user_schema import User

user_route = APIRouter()

@user_route.post("/")
def create_users(user: User = Body(...)):
    try:
        return user
    except Exception as e:
        print(e)
        return {"error:":str(e)}

@user_route.get("/")
def read_users():
    return [{"username": "andres"}, {"username": "felipe"}]

@user_route.get("/{id}")
def read_user(id: int):
    return {"id": id}

@user_route.put("/{user_id}")
def update_user(user_id: int):
    return {"user_id": user_id}

@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    return {"user_id": user_id}