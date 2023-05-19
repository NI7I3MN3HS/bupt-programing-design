# 通知模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/notification", tags=["notification"])


# 获取用户的所有通知信息
@router.get("/all")
async def get_all_notification(
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.get_notifications_by_use(db, user_id=current_user.id)


# 创建通知信息
@router.post("/create")
async def create_notification(
    notification: schemas.NotificationCreate,
    db: Session = Depends(get_db),
):
    return crud.create_notification(db=db, notification=notification)


# 删除通知信息
@router.delete("/delete")
async def delete_notification(
    notification_id: int,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_notification = crud.get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.delete_notification(db=db, notification_id=db_notification.id)


# 获取通知信息
@router.get("/{notification_id}")
async def get_notification(
    notification_id: int,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_notification = crud.get_notification(db, notification_id=notification_id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification
