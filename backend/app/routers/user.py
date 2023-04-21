import os
from fastapi import Depends, HTTPException, APIRouter, UploadFile, File
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security
from .. import mail

UPLOAD_FOLDER = "static/avatar/"

router = APIRouter(prefix="/user", tags=["user"])


# 获取用户信息
@router.get("/")
async def get_me(user: schemas.User = Depends(security.get_current_user)):
    return user


# 更新用户信息
@router.put("/update")
async def update_me(
    user_update: schemas.UserUpdate,
    user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_user = crud.update_user(db, user.id, user_update)
    return db_user


# 上传头像
@router.post("/upload_avatar")
async def upload_avatar(
    avatar: UploadFile = File(...),
    user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    # 限制文件大小和类型
    if not avatar.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File type error")
    if avatar.size > 1024 * 1024 * 5:
        raise HTTPException(status_code=400, detail="File size error")
    # 保存文件
    avatar.filename = "avatar" + str(user.id) + os.path.splitext(avatar.filename)[1]
    file_path = UPLOAD_FOLDER + avatar.filename
    with open(file_path, "wb") as f:
        f.write(avatar.file.read())
    # 更新数据库
    db_user = crud.get_user(db, user_id=user.id)
    db_user.avatar_url = file_path
    db.commit()
    db.refresh(db_user)
    return db_user


# 重置密码
@router.put("/reset_password")
async def reset_password(
    origin_passowrd: schemas.password,
    new_password: schemas.password2,
    user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    if not security.verify_password(origin_passowrd.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    hashed_password = security.hash_password(new_password.password2)
    # 更新密码
    db_user = crud.get_user(db, user_id=user.id)
    db_user.hashed_password = hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user
