from pydantic import BaseModel

class Table(BaseModel):
    id: int
    color: str
    size : str
    numberPeople : str
