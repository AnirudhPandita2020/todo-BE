
from ast import For
from .database import Base
from sqlalchemy import TIME, TIMESTAMP, Column, ForeignKey, Integer,String, null, text,Boolean
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    username =Column(String,nullable=False,unique=True)
    email = Column(String,nullable=False,unique=True)
    password = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
class TodoList(Base):
    __tablename__ = "list"
    id =Column(Integer,nullable=False,primary_key=True,autoincrement=True)
    title = Column(String,nullable=False)
    content =Column(String,nullable=False)
    userid = Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    is_completed = Column(Boolean,server_default='False',nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    
    user = relationship("User")

class Friendsreq(Base):
    __tablename__ = "fr"
    fromid = Column(Integer,primary_key=True,nullable = False)
    toid = Column(Integer,primary_key=True,nullable=False)
    accepted = Column(Boolean,server_default='False')
    
    