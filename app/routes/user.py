from typing import List,Optional
from fastapi import APIRouter,Depends,HTTPException,status
from app.models import models
from app.utils import utils
from app.models import database
from sqlalchemy.orm import Session
from app.models import schemas


router = APIRouter(prefix="/users",tags = ["USER"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.User)
async def create_user(user:schemas.UserCreate,db:Session =Depends(database.get_db)):
    exists_user = db.query(models.User).filter(models.User.email == user.email).first()
    
    if exists_user:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="User already exists")
    
    user.password = utils.hash(user.password)
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user   


@router.get("",status_code=status.HTTP_200_OK,response_model=List[schemas.UserResponse])
async def get_user_by_name(db:Session = Depends(database.get_db),search:Optional[str] = ""):
    user = db.query(models.User).filter(models.User.username.contains(search)).all()
    return user
    

@router.get("/{id}",status_code=status.HTTP_200_OK,response_model=schemas.UserResponse)
async def get_user(id:int,db:Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status.HTTP_404_NOT_FOUND,"User not found")
    return user

