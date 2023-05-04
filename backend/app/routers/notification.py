# 通知模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/notification", tags=["notification"])


# 获取通知信息
@router.post("/{notification_id.id}")
async def get_notification(
    notification_id: schemas.NotificationDelete,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_notification = crud.get_notification(db, notification_id=notification_id.id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return db_notification


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
    notification: schemas.NotificationDelete,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_notification = crud.get_notification(db, notification_id=notification.id)
    if db_notification is None:
        raise HTTPException(status_code=404, detail="Notification not found")
    return crud.delete_notification(db=db, notification_id=db_notification.id)