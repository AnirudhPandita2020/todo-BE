
from datetime import datetime

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
    
class UserResponse(BaseModel):
    id:int
    username:str
    email:str
    
    class Config:
        orm_mode = True
    
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
        
class FriendReq(BaseModel):
    toid:int
    accepted:Optional[bool] = False
class FriendReqAccept(BaseModel):
    fromid:int
    accepted:Optional[bool] =True
    
class FriendReqList(BaseModel):
    id:int
    username:str
    email:str
    class Config:
        orm_mode =True
        
class Count(BaseModel):
    completed:int
    pending:int
        