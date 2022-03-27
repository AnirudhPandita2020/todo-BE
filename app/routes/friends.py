from typing import List
from fastapi import APIRouter,Depends,HTTPException,status
from app.models import models

from app.models import database
from sqlalchemy.orm import Session
from app.models import schemas
from app.auth import oauth2

router = APIRouter(prefix="/fr",tags=["FRIENDS"])

@router.get("",status_code=status.HTTP_200_OK,response_model=List[schemas.FriendReqList])
async def get_friends_request_list(get_current_user:int = Depends(oauth2.get_current_user),
                                   db:Session = Depends(database.get_db),
                                   only_accepted:bool = False,
                                   get_all:bool = False):
    if only_accepted is True:
        fr_list = db.query(models.User).join(
            models.Friendsreq,models.Friendsreq.toid == models.User.id
                                            ).filter(
            models.Friendsreq.fromid == get_current_user.id,models.Friendsreq.accepted == True
            ).union(
                db.query(models.User).join(
                    models.Friendsreq,models.Friendsreq.fromid == models.User.id
                    ).filter(
                        models.Friendsreq.toid == get_current_user.id,models.Friendsreq.accepted == True
                        ))
        return fr_list.all()
    elif get_all:
        fr_list = db.query(models.User).join(
            models.Friendsreq,models.Friendsreq.toid == models.User.id
                                            ).filter(
            models.Friendsreq.fromid == get_current_user.id
            ).union(
                db.query(models.User).join(
                    models.Friendsreq,models.Friendsreq.fromid == models.User.id
                    ).filter(
                        models.Friendsreq.toid == get_current_user.id))
        return fr_list.all()
    
    elif only_accepted is False:
        fr_list = db.query(models.User).join(
            models.Friendsreq,models.Friendsreq.toid == models.User.id
                                            ).filter(
            models.Friendsreq.fromid == get_current_user.id,models.Friendsreq.accepted == False
            ).union(
                db.query(models.User).join(
                    models.Friendsreq,models.Friendsreq.fromid == models.User.id
                    ).filter(
                        models.Friendsreq.toid == get_current_user.id,models.Friendsreq.accepted == False
                        ))
        return fr_list.all()
    
        
        

@router.post("/",status_code=status.HTTP_201_CREATED)
async def send_request(req:schemas.FriendReq,db:Session = Depends(database.get_db),
                       get_current_user:int = Depends(oauth2.get_current_user)):
    sender = db.query(models.User).filter(models.User.id == get_current_user.id)
    rec = db.query(models.User).filter(models.User.id == req.toid)
    check_req = db.query(models.Friendsreq).filter(models.Friendsreq.fromid == get_current_user.id,models.Friendsreq.toid == req.toid).first()
    print(check_req)
    if not sender.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Does not exists")
    if not rec.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Does not exists")
    if check_req:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Request Already send")
    
    new_req = models.Friendsreq(**req.dict())
    new_req.fromid = get_current_user.id
    db.add(new_req)
    db.commit()
    db.refresh(new_req)
    return {"message":"Request send"}

@router.put("/")
async def accept_request(req:schemas.FriendReqAccept,db:Session = Depends(database.get_db),get_current_user:int=Depends(oauth2.get_current_user)):
    req_updation = db.query(models.Friendsreq).filter(models.Friendsreq.toid == get_current_user.id,models.Friendsreq.fromid== req.fromid)
    if not req_updation.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No request")
    
    req_updation.update(req.dict(),
                        synchronize_session=False)
    db.commit()
    
    return req_updation.first()