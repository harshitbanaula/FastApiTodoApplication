# app/schemas.py
from pydantic import BaseModel, EmailStr
from typing import Optional, List

# Auth tokens
class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class TokenRefreshIn(BaseModel):
    refresh_token: str

# User
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    class Config:
        orm_mode = True

# ToDo
class ToDoBase(BaseModel):
    title: str
    description: Optional[str] = None

class ToDoCreate(ToDoBase):
    pass

class ToDoOut(ToDoBase):
    id: int
    completed: bool
    class Config:
        orm_mode = True


