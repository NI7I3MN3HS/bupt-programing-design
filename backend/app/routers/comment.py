# 评论模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/comment", tags=["comment"])


# 获取评论信息
@router.post("/{comment_id.id}")
async def get_comment(
    comment_id: schemas.CommentDelete,
    db: Session = Depends(get_db),
):
    db_comment = crud.get_comment(db, comment_id=comment_id.id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return db_comment


# 获取帖子的评论
@router.get("/{post_id}")
async def get_post_comments(
    post_id: int,
    db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return crud.get_comments_by_post(db=db, post_id=post_id)


# 创建评论
@router.post("/create")
async def create_comment(
    comment: schemas.CommentBase,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.create_comment(db=db, comment=comment, user_id=current_user.id)


# 删除评论
@router.delete("/delete")
async def delete_comment(
    comment_id: schemas.CommentDelete,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_comment = crud.get_comment(db, comment_id=comment_id.id)
    if db_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    db_post = crud.get_post(db, post_id=db_comment.post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    db_user = crud.get_user(db, user_id=db_post.user_id)
    if db_comment.user_id != current_user.id and db_user.id != current_user.id:
        raise HTTPException(status_code=403, detail="No permission")
    return crud.delete_comment(db=db, comment_id=comment_id.id)
