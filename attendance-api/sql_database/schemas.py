from pydantic import BaseModel

class UserBase(BaseModel):
    name: str

class User(UserBase):
    title: str
    lesson: str
    
    class Config:
        orm_mode = True