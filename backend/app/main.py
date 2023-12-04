from fastapi import Depends, FastAPI
from .routers import (
    login,
    register,
    user,
    post,
    comment,
    follow,
    like,
    notification,
    admin,
    translate,
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173","http://localhost:3000","http://127.0.0.1:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login.router)
app.include_router(register.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(comment.router)
app.include_router(follow.router)
app.include_router(like.router)
app.include_router(notification.router)
app.include_router(admin.router)
app.include_router(translate.router)
