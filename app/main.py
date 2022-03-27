from fastapi import FastAPI


from .routes import user,list,friends
from .auth import auth


app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(list.router)
app.include_router(friends.router)