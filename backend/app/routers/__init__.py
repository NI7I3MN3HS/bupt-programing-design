# 路径路由

from fastapi import APIRouter

from . import login

class Router(APIRouter):
    def __init__(self, url_path:str="") -> None :
        super().__init__(prefix=url_path)
        self.include_router(login.router)