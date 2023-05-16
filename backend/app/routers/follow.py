# 关注模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/follow", tags=["follow"])


# 关注用户
@router.post("/create")
async def create_follow(
    follow: schemas.FollowCreate,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.create_follow(db=db, follow=follow, user_id=current_user.id)


# 取消关注
@router.delete("/delete")
async def delete_follow(
    follow: schemas.FollowBase,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_follow = crud.get_follow_by_follower_and_followed(
        db, current_user.id, follow.followed_id
    )
    if db_follow is None:
        raise HTTPException(status_code=404, detail="Follow not found")
    return crud.delete_follow(db=db, follow_id=db_follow.id)


# 获取用户的所有关注
@router.get("/get_followed")
async def get_followed(
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.get_follows_by_user(db=db, user_id=current_user.id)


# 获取用户的所有粉丝
@router.get("/get_follower")
async def get_follower(
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.get_followers_by_user(db=db, followed_id=current_user.id)
