from fastapi import Depends, FastAPI
from .routers import login

app = FastAPI()

app.include_router(login.router)
