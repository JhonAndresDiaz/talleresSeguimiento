from pydantic import BaseModel

class Shirt(BaseModel):
    id: int
    design : str
    color: str
    typeGarment : str
    size : str