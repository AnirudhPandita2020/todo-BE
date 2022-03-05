from datetime import datetime
from email import contentmanager
from re import L
from typing import Optional
from pydantic import BaseModel,EmailStr

class User(BaseModel):
    id:int
    email:EmailStr
    created_at:datetime
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    username:str
    email:str
    password:str
    
class TodoCreate(BaseModel):
    title:str
    content:str
    is_completed:Optional[bool] = False
    
    
class TodoListResponse(BaseModel):
    id:int
    title:str
    content:str
    userid:int
    is_completed:bool
    created_at:datetime
    user:User
    
    class Config:
        orm_mode = True
        

class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
    id:Optional[str] = None
    
class TaskList(TodoCreate):
    class Config:
        orm_mode = True