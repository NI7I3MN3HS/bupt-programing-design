from fastapi import Depends, FastAPI
from .routers import login, register, user, post, comment
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(login.router)
app.include_router(register.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
