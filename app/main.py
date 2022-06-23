from fastapi import FastAPI


from .routes import user,list,friends
from .auth import auth



app = FastAPI(
    title="Todo List",
    description="Simple Todo List backend using FastAPI",
    version="1.0.2",
    contact={
        "name": "Anirudh Pandita",
        "url": "https://www.linkedin.com/in/anirudh-pandita-a0b532200/",
        "email": "kppkanu@gmail.com",
    }
)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(list.router)
app.include_router(friends.router)