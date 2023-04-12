# 用户注册接口
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..sql_app import schemas, crud
from ..sql_app.database import get_db

router = APIRouter(
    prefix="/register",
    tags=["register"],
)


@router.post("/", response_model=schemas.User)
async def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 验证用户是否存在
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # 验证邮箱是否存在
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db=db, user=user)
