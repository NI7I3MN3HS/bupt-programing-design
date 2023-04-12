from fastapi import Depends, FastAPI
from .routers import login, register

app = FastAPI()

app.include_router(login.router)
app.include_router(register.router)
