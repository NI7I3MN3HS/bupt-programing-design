# 用户注册接口
from secrets import token_hex
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..sql_app import schemas, crud
from ..sql_app.database import get_db
from .. import mail


origin_code = token_hex(4)  # 生成验证码

router = APIRouter(
    prefix="/register",
    tags=["register"],
)


@router.post("/VerifyCode")
async def send_verify_code(email: str):
    mail.get_code_email(email, origin_code)  # 发送验证码

    return {
        "msg": "Verification code sent to your email. Please check and input the code."
    }


@router.post("/")
async def register(user: schemas.UserCreate, code: str, db: Session = Depends(get_db)):
    # 验证用户是否存在
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    # 验证邮箱是否存在
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    if code != origin_code:
        raise HTTPException(status_code=400, detail="Verification code error")
    crud.create_user(db=db, user=user)
    return {"msg": "User registered successfully."}
