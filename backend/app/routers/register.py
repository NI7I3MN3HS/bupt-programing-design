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
async def send_verify_code(Email:schemas.Email, db: Session = Depends(get_db)):
    email=Email.email
    if (
        len(email) < 2
        or len(email) > 32
        or re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$ ", email)
    ):
        raise HTTPException(status_code=400, detail="Invalid Email")
    # 验证邮箱是否存在
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
    user:schemas.UserCreate,Code:schemas.Code,db: Session = Depends(get_db)
):
    code=Code.code
    username=user.username
    password=user.password
    if len(username) < 1 or len(username) > 20:
        raise HTTPException(status_code=400, detail="Username must be 1-20 characters")
    if len(password) < 6 or len(password) > 24:
        raise HTTPException(status_code=400, detail="Password must be 6-24 characters")
    db_code = crud.get_code_by_code(db, code=code)
    if not db_code:
        raise HTTPException(status_code=400, detail="Verification code error")
    user = schemas.UserCreate(username=username, email=db_code.email, password=password)
    # 验证用户是否存在
    db_user = crud.get_user_by_username(db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    crud.create_user(db=db, user=user)
    crud.delete_code(db, code=code)
    return {"msg": "User registered successfully."}


@router.post("/find_password/VerifyCode")
async def send_verify_code(email: str, db: Session = Depends(get_db)):
    if (
        len(email) < 2
        or len(email) > 32
        or re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$ ", email)
    ):
        raise HTTPException(status_code=400, detail="Invalid Email")
    # 验证邮箱是否存在
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
async def find_password(code: str, password: str, db: Session = Depends(get_db)):
    db_code = crud.get_code_by_code(db, code=code)
    if not db_code:
        raise HTTPException(status_code=400, detail="Verification code error")
    email = db_code.email
    if len(password) < 6 or len(password) > 24:
        raise HTTPException(status_code=400, detail="Password must be 6-24 characters")
    db_user = crud.get_user_by_email(db, email=email)
    if not db_user:
        raise HTTPException(status_code=400, detail="Email error")
    # 更新密码
    db_user.hashed_password = security.hash_password(password)
    db.commit()
    db.refresh(db_user)
    crud.delete_code(db, code=code)
    return {"msg": "Password reset successfully."}
