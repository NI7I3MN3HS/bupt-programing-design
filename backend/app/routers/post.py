# 帖子模块
from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from ..sql_app import models, schemas, crud
from ..sql_app.database import get_db
from ..core import security

router = APIRouter(prefix="/post", tags=["post"])


# 获取所有帖子信息 点赞数 评论数
@router.get("/all")
async def get_all_posts(
    db: Session = Depends(get_db),
):
    return crud.get_posts(db=db)


# 创建帖子
@router.post("/create")
async def create_post(
    post: schemas.PostBase,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    return crud.create_post(db=db, post=post, user_id=current_user.id)


# 更新帖子
@router.put("/update")
async def update_post(
    post_update: schemas.PostUpdate,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id=post_update.id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No permission")
    return crud.update_post(db=db, post_id=post_update.id, post=post_update)


# 删除帖子
@router.delete("/delete")
async def delete_post(
    post_id: int,
    current_user: schemas.User = Depends(security.get_current_user),
    db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    if db_post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="No permission")
    return crud.delete_post(db=db, post_id=post_id)


# 获取帖子信息
@router.get("/{post_id}")
async def get_post(
    post_id: int,
    db: Session = Depends(get_db),
):
    db_post = crud.get_post(db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return {
        "post": db_post,
        "comment_count": crud.get_comments_count_by_post(db, post_id=post_id),
        "like_count": crud.get_post_like_count(db, post_id=post_id),
    }


# 获取用户发帖信息
@router.get("/user/{user_id}")
async def get_user_posts(
    user_id: int,
    db: Session = Depends(get_db),
):
    return crud.get_posts_by_user(db, user_id=user_id)


# 搜索文章
@router.post("/search")
async def search_posts(
    keyword: str,
    db: Session = Depends(get_db),
):
    return crud.search_post(db, keyword=keyword)
