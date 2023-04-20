# 用户注册接口
import re
from secrets import token_hex
from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from ..sql_app import schemas, crud
from ..sql_app.database import get_db
from ..core import security
from .. import mail


router = APIRouter(
    prefix="/register",
    tags=["register"],
)


@router.post("/VerifyCode")
async def send_verify_code(Email: schemas.Email, db: Session = Depends(get_db)):
    email = Email.email
    db_user = crud.get_user_by_email(db, email=email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    origin_code = token_hex(2)  # 生成验证码
    db_code = crud.get_code_by_email(db, email=email)
    if db_code:
        crud.update_code(db, email=email, code=origin_code)
    else:
        crud.create_code(db, email=email, code=origin_code)

    mail.get_code_email(email, origin_code)  # 发送验证码

    return {
        "msg": "Verification code sent to your email. Please check and input the code."
    }


@router.post("/")
async def register(
    user: schemas.UserCreate,
    Code: schemas.Code,
    db: Session = Depends(get_db),
):
    db_code = crud.get_code_by_code(db, code=Code.code)
    if not db_code:
        raise HTTPException(status_code=400, detail="Verification code error")
    # 验证用户是否存在
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    crud.create_user(db=db, user=user, email=db_code.email)
    crud.delete_code(db, code=Code.code)
    return {"msg": "User registered successfully."}


@router.post("/find_password/VerifyCode")
async def send_verify_code(Email: schemas.Email, db: Session = Depends(get_db)):
    email = Email.email
    db_user = crud.get_user_by_email(db, email=email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email not registered")
    origin_code = token_hex(2)  # 生成验证码
    db_code = crud.get_code_by_email(db, email=email)
    if db_code:
        crud.update_code(db, email=email, code=origin_code)
    else:
        crud.create_code(db, email=email, code=origin_code)

    mail.get_code_email(email, origin_code)  # 发送验证码

    return {
        "msg": "Verification code sent to your email. Please check and input the code."
    }


# 找回密码
@router.post("/find_password")
async def find_password(
    Code: schemas.Code,
    password: schemas.password,
    db: Session = Depends(get_db),
):
    code = Code.code
    db_code = crud.get_code_by_code(db, code=code)
    if not db_code:
        raise HTTPException(status_code=400, detail="Verification code error")
    email = db_code.email
    db_user = crud.get_user_by_email(db, email=email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email error")
    # 更新密码
    db_user.hashed_password = security.hash_password(password.password)
    db.commit()
    db.refresh(db_user)
    crud.delete_code(db, code=code)
    return {"msg": "Password reset successfully."}
