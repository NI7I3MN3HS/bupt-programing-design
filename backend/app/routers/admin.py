# 管理员模块
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..core.security import (
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/admin", tags=["admin"])

admin_password = "admin"


# 管理员登录
@router.post("/", response_model=schemas.Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # 验证用户名和密码是否正确
    user = crud.get_user_by_username(db, username=form_data.username)

    email = crud.get_user_by_email(db, email=form_data.username)
    if not user and not email:
        raise HTTPException(status_code=400, detail="Incorrect email or username")
    if user:
        if not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
        if user.is_admin == False:
            raise HTTPException(status_code=400, detail="Not admin")
    if email:
        if not verify_password(form_data.password, email.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        if email.is_admin == False:
            raise HTTPException(status_code=400, detail="Not admin")
        form_data.username = email.username
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# 注册管理员用户
@router.post("/register")
async def create_admin_user(
    password: str,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    if password != admin_password:
        raise HTTPException(status_code=400, detail="Incorrect admin password")
    return crud.create_admin_user(db=db, user_id=current_user.id)


# 获取所有用户信息
@router.get("/users")
async def get_all_users(
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    return crud.get_users(db)


# 获取所有帖子信息
@router.get("/posts")
async def get_all_posts(
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    return crud.get_posts(db)


# 获取所有评论信息
@router.get("/comments")
async def get_all_comments(
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    return crud.get_comments(db)


# 获取所有通知信息
@router.get("/notifications")
async def get_all_notifications(
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    return crud.get_notifications(db)


# 删除用户信息
@router.delete("/users/delete")
async def delete_user(
    user_id: int,
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.delete_user(db=db, user_id=db_user.id)


# 删除帖子信息
@router.delete("/posts/delete")
async def delete_post(
    post_id: int,
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.delete_post(db=db, post_id=db_post.id)


# 删除评论信息
@router.delete("/comments/delete")
async def delete_comment(
    comment_id: int,
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    db_comment = crud.get_comment(db, comment_id=comment_id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return crud.delete_comment(db=db, comment_id=db_comment.id)


# 删除通知信息
@router.delete("/notifications/delete")
async def delete_notification(
    notification_id: int,
    current_user: schemas.User = Depends(security.get_current_admin),
    db: Session = Depends(get_db),
):
    db_notification = crud.get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.delete_notification(db=db, notification_id=db_notification.id)
