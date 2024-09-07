from pydantic import BaseModel

class Car(BaseModel):
    id: int
    color : str
    amount : str
    price : str
    year : str