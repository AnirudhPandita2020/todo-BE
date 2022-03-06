from fastapi import FastAPI

from .models import models
from .models import database
from .routes import user,list
from .auth import auth


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(list.router)