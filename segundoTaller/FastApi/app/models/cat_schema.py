from pydantic import BaseModel

class Cat(BaseModel):
    id: int
    name : str
    gender : str
    age : str
