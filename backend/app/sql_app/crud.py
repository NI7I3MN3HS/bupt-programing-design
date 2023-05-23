from sqlalchemy.orm import Session
from sqlalchemy import or_
from ..core import security
from . import models, schemas


# code crud
# 创建代码
def create_code(db: Session, code: str, email: str):
    db_code = models.Code(
        email=email,
        code=code,
    )
    db.add(db_code)
    db.commit()
    db.refresh(db_code)
    return db_code


# 根据邮箱获取验证码
def get_code_by_email(db: Session, email: str):
    return db.query(models.Code).filter(models.Code.email == email).first()


# 根据code获取验证码
def get_code_by_code(db: Session, code: str):
    return db.query(models.Code).filter(models.Code.code == code).first()


# 更新code
def update_code(db: Session, email: str, code: str):
    db_code = db.query(models.Code).filter(models.Code.email == email).first()
    if db_code:
        db_code.code = code
        db.commit()
        db.refresh(db_code)
        return db_code


# 根据用户邮箱删除验证码
def delete_code(db: Session, code: str):
    db_code = db.query(models.Code).filter(models.Code.code == code).first()
    if db_code:
        db.delete(db_code)
        db.commit()
        return db_code


# user crud
# 创建用户
def create_user(db: Session, user: schemas.UserCreate, email: str):
    db_user = models.User(
        username=user.username,
        email=email,
        hashed_password=security.hash_password(user.password),
    )
    db.add(db_user)
    db.commit()  # 提交保存到数据库中
    db.refresh(db_user)  # 刷新数据库中的数据
    return db_user


# 根据用户id获取用户信息
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# 根据用户名获取用户信息
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


# 根据电子邮件获取用户信息
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


# 获取所有用户信息
def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


# 更新用户信息
def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.dict(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user


# 根据用户id删除用户
def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user


# 搜索用户
def search_user(db: Session, keyword: str):
    return db.query(models.User).filter(models.User.username.like(f"%{keyword}%")).all()


# post crud
# 创建文章
def create_post(db: Session, post: schemas.PostBase, user_id: int):
    db_post = models.Post(title=post.title, content=post.content, user_id=user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


# 根据文章id获取文章信息
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


# 获取所有文章信息
def get_posts(db: Session):
    posts = db.query(models.Post).all()
    post_info = []
    for post in posts:
        post_info.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content[:300],
                "created_time": post.create_time,
                "user_id": post.user_id,
                "comment_count": get_comments_count_by_post(db, post.id),
                "like_count": get_post_like_count(db, post.id),
            }
        )
    return post_info


# 更新文章信息
def update_post(db: Session, post_id: int, post: schemas.PostUpdate):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        for key, value in post.dict(exclude_unset=True).items():
            setattr(db_post, key, value)
        db.commit()
        db.refresh(db_post)
        return db_post


# 根据文章id删除文章
def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return db_post


# 获取用户的所有文章
def get_posts_by_user(db: Session, user_id: int):
    posts = db.query(models.Post).filter(models.Post.user_id == user_id).all()
    post_info = []
    for post in posts:
        post_info.append(
            {
                "id": post.id,
                "title": post.title,
                "content": post.content[:300],
                "created_time": post.create_time,
                "user_id": post.user_id,
                "comment_count": get_comments_count_by_post(db, post.id),
                "like_count": get_post_like_count(db, post.id),
            }
        )
    return post_info


# 搜索文章
def search_post(db: Session, keyword: str):
    return (
        db.query(models.Post)
        .filter(
            or_(
                models.Post.title.ilike(f"%{keyword}%"),
                models.Post.content.ilike(f"%{keyword}%"),
            )
        )
        .all()
    )


# comment crud
# 创建评论
def create_comment(db: Session, comment: schemas.CommentCreate, user_id: int):
    db_comment = models.Comment(
        content=comment.content,
        reply_user_id=comment.reply_user_id,
        user_id=user_id,
        post_id=comment.post_id,
        parent_id=comment.parent_id,
    )
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment


# 根据评论id获取评论信息
def get_comment(db: Session, comment_id: int):
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


# 获取所有评论信息
def get_comments(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).offset(skip).limit(limit).all()


# 根据评论id删除评论
def delete_comment(db: Session, comment_id: int):
    db_comment = (
        db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    )
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment


# 获取用户的所有评论
def get_comments_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Comment)
        .filter(models.Comment.user_id == user_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


# 获取评论的所有评论
def get_comments_by_comment(db: Session, comment_id: int):
    comments = (
        db.query(models.Comment).filter(models.Comment.parent_id == comment_id).all()
    )
    comment_info = []
    for comment in comments:
        comment_info.append(
            {
                "id": comment.id,
                "content": comment.content,
                "created_time": comment.create_time,
                "update_time": comment.update_time,
                "reply_user_id": comment.reply_user_id,
                "user_id": comment.user_id,
                "post_id": comment.post_id,
                "parent_id": comment.parent_id,
                "like_count": get_comments_count_by_comment(db, comment.id),
            }
        )
    return comment_info


# 获取评论的评论数
def get_comments_count_by_comment(db: Session, comment_id: int):
    return (
        db.query(models.Comment).filter(models.Comment.parent_id == comment_id).count()
    )


# 获取文章的所有评论
def get_comments_by_post(db: Session, post_id: int):
    return (
        db.query(models.Comment)
        .filter(models.Comment.post_id == post_id, models.Comment.parent_id == 0)
        .all()
    )


# 获取文章的评论数
def get_comments_count_by_post(db: Session, post_id: int):
    return (
        db.query(models.Comment)
        .filter(models.Comment.post_id == post_id, models.Comment.parent_id == 0)
        .count()
    )


# follow crud
# 创建关注
def create_follow(db: Session, follow: schemas.FollowCreate, user_id: int):
    db_follow = models.Follow(follower_id=user_id, followed_id=follow.followed_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow


# 根据关注者和关注对象获取关注信息
def get_follow_by_follower_and_followed(
    db: Session, follower_id: int, followed_id: int
):
    return (
        db.query(models.Follow)
        .filter(
            models.Follow.follower_id == follower_id,
            models.Follow.followed_id == followed_id,
        )
        .first()
    )


# 根据关注id获取关注信息
def get_follow(db: Session, follow_id: int):
    return db.query(models.Follow).filter(models.Follow.id == follow_id).first()


# 获取所有关注信息
def get_follows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Follow).offset(skip).limit(limit).all()


# 获取用户的所有关注
def get_follows_by_user(db: Session, user_id: int):
    return db.query(models.Follow).filter(models.Follow.follower_id == user_id).all()


# 获取用户的所有粉丝
def get_followers_by_user(db: Session, user_id: int):
    return db.query(models.Follow).filter(models.Follow.followed_id == user_id).all()


# 获取用户的关注数
def get_follows_count_by_user(db: Session, user_id: int):
    return db.query(models.Follow).filter(models.Follow.follower_id == user_id).count()


# 获取用户的粉丝数
def get_followers_count_by_user(db: Session, user_id: int):
    return db.query(models.Follow).filter(models.Follow.followed_id == user_id).count()


# 根据关注id删除关注
def delete_follow(db: Session, follow_id: int):
    db_follow = db.query(models.Follow).filter(models.Follow.id == follow_id).first()
    if db_follow:
        db.delete(db_follow)
        db.commit()
        return db_follow


# 取消关注
def cancel_follow(db: Session, follower_id: int, followed_id: int):
    db_follow = (
        db.query(models.Follow)
        .filter(
            models.Follow.follower_id == follower_id,
            models.Follow.followed_id == followed_id,
        )
        .first()
    )
    if db_follow:
        db.delete(db_follow)
        db.commit()
        return db_follow


# like crud
# 创建点赞
def create_like(db: Session, like: schemas.LikeCreate, user_id: int):
    db_like = models.Like(
        user_id=user_id, post_id=like.post_id, comment_id=like.comment_id
    )
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like


# 获取帖子的点赞数
def get_post_like_count(db: Session, post_id: int):
    return (
        db.query(models.Like)
        .filter(models.Like.post_id == post_id, models.Like.comment_id == 0)
        .count()
    )


# 获取评论的点赞数
def get_comment_like_count(db: Session, comment_id: int):
    return db.query(models.Like).filter(models.Like.comment_id == comment_id).count()


# 根据点赞id获取点赞信息
def get_like(db: Session, like_id: int):
    return db.query(models.Like).filter(models.Like.id == like_id).first()


# 根据用户id和文章id和评论id获取点赞信息
def get_like_by_user_and_post_and_comment(
    db: Session, user_id: int, post_id: int, comment_id: int
):
    return (
        db.query(models.Like)
        .filter(
            models.Like.user_id == user_id,
            models.Like.post_id == post_id,
            models.Like.comment_id == comment_id,
        )
        .first()
    )


# 获取所有点赞信息
def get_likes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Like).offset(skip).limit(limit).all()


# 获取文章的所有点赞
def get_likes_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Like)
        .filter(models.Like.post_id == post_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


# 获取评论的所有点赞
def get_likes_by_comment(db: Session, comment_id: int, skip: int = 0, limit: int = 100):
    return (
        db.query(models.Like)
        .filter(models.Like.comment_id == comment_id)
        .offset(skip)
        .limit(limit)
        .all()
    )


# 取消文章点赞
def cancel_like_post(db: Session, user_id: int, post_id: int):
    db_like = (
        db.query(models.Like)
        .filter(models.Like.user_id == user_id, models.Like.post_id == post_id)
        .first()
    )
    if db_like:
        db.delete(db_like)
        db.commit()
        return db_like


# 取消评论点赞
def cancel_like_comment(db: Session, user_id: int, comment_id: int):
    db_like = (
        db.query(models.Like)
        .filter(models.Like.user_id == user_id, models.Like.comment_id == comment_id)
        .first()
    )
    if db_like:
        db.delete(db_like)
        db.commit()
        return db_like


# 根据点赞id删除点赞
def delete_like(db: Session, like_id: int):
    db_like = db.query(models.Like).filter(models.Like.id == like_id).first()
    if db_like:
        db.delete(db_like)
        db.commit()
        return db_like


# notification crud
# 创建通知
def create_notification(db: Session, notification: schemas.NotificationCreate):
    db_notification = models.Notification(
        content=notification.content, user_id=notification.user_id
    )
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification


# 根据通知id获取通知信息
def get_notification(db: Session, notification_id: int):
    return (
        db.query(models.Notification)
        .filter(models.Notification.id == notification_id)
        .first()
    )


# 获取所有通知信息
def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).offset(skip).limit(limit).all()


# 获取用户的所有通知
def get_notifications_by_user(db: Session, user_id: int):
    return (
        db.query(models.Notification)
        .filter(models.Notification.user_id == user_id)
        .all()
    )


# 根据通知id删除通知
def delete_notification(db: Session, notification_id: int):
    db_notification = (
        db.query(models.Notification)
        .filter(models.Notification.id == notification_id)
        .first()
    )
    if db_notification:
        db.delete(db_notification)
        db.commit()
        return db_notification


# 根据用户id删除通知
def delete_notifications_by_user(db: Session, user_id: int):
    db_notifications = (
        db.query(models.Notification)
        .filter(models.Notification.user_id == user_id)
        .all()
    )
    if db_notifications:
        for db_notification in db_notifications:
            db.delete(db_notification)
        db.commit()
        return db_notifications
