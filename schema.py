from pydantic import *
class UserCreate(BaseModel):
    name : str
    age : int


class UserResponse(BaseModel):
    id: int
    name:str
    age:int

class config:
    orm_mode=True

