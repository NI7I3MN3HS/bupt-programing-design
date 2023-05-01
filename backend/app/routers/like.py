# 点赞模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/like", tags=["like"])


# 点赞
@router.post("/create")
async def create_like(
    like: schemas.LikeCreate,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.create_like(db=db, like=like, user_id=current_user.id)


# 取消点赞
@router.delete("/delete")
async def delete_like(
    like: schemas.LikeBase,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_like = crud.get_like_by_user_and_post_and_comment(
        db, current_user.id, like.post_id, like.comment_id
    )
    if db_like is None:
        raise HTTPException(status_code=404, detail="Like not found")
    return crud.delete_like(db=db, like_id=db_like.id)
