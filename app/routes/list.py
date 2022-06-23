from cgitb import reset
from typing import List
from unittest import async_case
from fastapi import APIRouter, Depends,HTTPException, Response,status
from app.models import database,schemas,models
from sqlalchemy.orm import Session
from app.auth import oauth2

router = APIRouter(prefix="/list",tags=["TODOLIST"])

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.TodoListResponse)
async def create_task(list:schemas.TodoCreate,db:Session = Depends(database.get_db),get_current_user:int = Depends(oauth2.get_current_user)):
    new_task = models.TodoList(**list.dict())
    new_task.userid = get_current_user.id
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task
    
@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.TodoListResponse])
def get_task(db:Session=Depends(database.get_db),get_current_user:int = Depends(oauth2.get_current_user)):
    task_list  = db.query(models.TodoList).filter(models.TodoList.userid == get_current_user.id).all()
    return task_list
    
    
@router.put("/{id}")
def update_task(id:int,task:schemas.TodoCreate,db:Session = Depends(database.get_db),get_current_user:int = Depends(oauth2.get_current_user)):
    task_to_update = db.query(models.TodoList).filter(models.TodoList.id == id)
    if not task_to_update.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Task does not exists")
    tas= task_to_update.first()
    
    if tas.userid != get_current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Access Denied")
    
    task_to_update.update(task.dict(),synchronize_session=False)
    db.commit()
    
    return task_to_update.first() 

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db:Session = Depends(database.get_db),get_current_user:int =Depends(oauth2.get_current_user)):
    task = db.query(models.TodoList).filter(models.TodoList.id == id)
    
    if task.first() is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = "Does not Exists")
    
    if task.first().id != get_current_user.id:
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail = "Access Denied")
     
    task.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.get("/count",status_code=status.HTTP_200_OK)
async def get_task_count(db:Session = Depends(database.get_db),get_current_user = Depends(oauth2.get_current_user)):
    completed_task = db.query(
        models.TodoList
    ).filter(models.TodoList.userid == get_current_user.id,
             models.TodoList.is_completed == True).count()
    
    pending_task = db.query(
        models.TodoList
    ).filter(
        models.TodoList.userid == get_current_user.id,
             models.TodoList.is_completed == False
    ).count()
    
    return {
        "completed":completed_task,
        "pending":pending_task
    }