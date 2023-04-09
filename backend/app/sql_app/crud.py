from sqlalchemy.orm import Session

from . import models, schemas

# user crud
# 创建用户
def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = user.password
    db_user = models.User(username=user.username, email=user.email, password_hash=hashed_password, avatar_url=user.avatar_url, introduction=user.introduction)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
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
    
# post crud
# 创建文章
def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(title=post.title, content=post.content, user_id=post.user_id)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

# 根据文章id获取文章信息
def get_post(db: Session, post_id: int):
    return db.query(models.Post).filter(models.Post.id == post_id).first()

# 获取所有文章信息
def get_posts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()

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
def get_posts_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Post).filter(models.Post.user_id == user_id).offset(skip).limit(limit).all()

# comment crud
# 创建评论
def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(content=comment.content, user_id=comment.user_id, post_id=comment.post_id, parent_id=comment.parent_id)
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

# 更新评论信息
def update_comment(db: Session, comment_id: int, comment: schemas.CommentUpdate):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        for key, value in comment.dict(exclude_unset=True).items():
            setattr(db_comment, key, value)
        db.commit()
        db.refresh(db_comment)
        return db_comment

# 根据评论id删除评论
def delete_comment(db: Session, comment_id: int):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment:
        db.delete(db_comment)
        db.commit()
        return db_comment

# 获取用户的所有评论
def get_comments_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).filter(models.Comment.user_id == user_id).offset(skip).limit(limit).all()

# 获取评论的所有评论
def get_comments_by_comment(db: Session, comment_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).filter(models.Comment.parent_id == comment_id).offset(skip).limit(limit).all()

# 获取文章的所有评论
def get_comments_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).offset(skip).limit(limit).all()

# follow crud
# 创建关注
def create_follow(db: Session, follow: schemas.FollowCreate):
    db_follow = models.Follow(follower_id=follow.follower_id, followed_id=follow.followed_id)
    db.add(db_follow)
    db.commit()
    db.refresh(db_follow)
    return db_follow

# 根据关注id获取关注信息
def get_follow(db: Session, follow_id: int):
    return db.query(models.Follow).filter(models.Follow.id == follow_id).first()

# 获取所有关注信息
def get_follows(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Follow).offset(skip).limit(limit).all()

# 获取用户的所有关注
def get_follows_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Follow).filter(models.Follow.follower_id == user_id).offset(skip).limit(limit).all()

# 获取用户的所有粉丝
def get_followers_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Follow).filter(models.Follow.followed_id == user_id).offset(skip).limit(limit).all()

# 根据关注id删除关注
def delete_follow(db: Session, follow_id: int):
    db_follow = db.query(models.Follow).filter(models.Follow.id == follow_id).first()
    if db_follow:
        db.delete(db_follow)
        db.commit()
        return db_follow

# 取消关注
def cancel_follow(db: Session, follower_id: int, followed_id: int):
    db_follow = db.query(models.Follow).filter(models.Follow.follower_id == follower_id, models.Follow.followed_id == followed_id).first()
    if db_follow:
        db.delete(db_follow)
        db.commit()
        return db_follow

# like crud
# 创建点赞
def create_like(db: Session, like: schemas.LikeCreate):
    db_like = models.Like(user_id=like.user_id, post_id=like.post_id, comment_id=like.comment_id)
    db.add(db_like)
    db.commit()
    db.refresh(db_like)
    return db_like

# 根据点赞id获取点赞信息
def get_like(db: Session, like_id: int):
    return db.query(models.Like).filter(models.Like.id == like_id).first()

# 获取所有点赞信息
def get_likes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Like).offset(skip).limit(limit).all()

# 获取文章的所有点赞
def get_likes_by_post(db: Session, post_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Like).filter(models.Like.post_id == post_id).offset(skip).limit(limit).all()

# 获取评论的所有点赞
def get_likes_by_comment(db: Session, comment_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Like).filter(models.Like.comment_id == comment_id).offset(skip).limit(limit).all()

# 取消文章点赞
def cancel_like_post(db: Session, user_id: int, post_id: int):
    db_like = db.query(models.Like).filter(models.Like.user_id == user_id, models.Like.post_id == post_id).first()
    if db_like:
        db.delete(db_like)
        db.commit()
        return db_like

# 取消评论点赞
def cancel_like_comment(db: Session, user_id: int, comment_id: int):
    db_like = db.query(models.Like).filter(models.Like.user_id == user_id, models.Like.comment_id == comment_id).first()
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
    db_notification = models.Notification(content=notification.content, user_id=notification.user_id)
    db.add(db_notification)
    db.commit()
    db.refresh(db_notification)
    return db_notification

# 根据通知id获取通知信息
def get_notification(db: Session, notification_id: int):
    return db.query(models.Notification).filter(models.Notification.id == notification_id).first()

# 获取所有通知信息
def get_notifications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).offset(skip).limit(limit).all()

# 获取用户的所有通知
def get_notifications_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.Notification).filter(models.Notification.user_id == user_id).offset(skip).limit(limit).all()

# 根据通知id删除通知
def delete_notification(db: Session, notification_id: int):
    db_notification = db.query(models.Notification).filter(models.Notification.id == notification_id).first()
    if db_notification:
        db.delete(db_notification)
        db.commit()
        return db_notification

# 根据用户id删除通知
def delete_notifications_by_user(db: Session, user_id: int):
    db_notifications = db.query(models.Notification).filter(models.Notification.user_id == user_id).all()
    if db_notifications:
        for db_notification in db_notifications:
            db.delete(db_notification)
        db.commit()
        return db_notifications

# private_message crud
# 创建私信
def create_private_message(db: Session, private_message: schemas.PrivateMessageCreate):
    db_private_message = models.PrivateMessage(content=private_message.content, sender_id=private_message.sender_id, receiver_id=private_message.receiver_id)
    db.add(db_private_message)
    db.commit()
    db.refresh(db_private_message)
    return db_private_message

# 根据私信id获取私信信息
def get_private_message(db: Session, private_message_id: int):
    return db.query(models.PrivateMessage).filter(models.PrivateMessage.id == private_message_id).first()

# 获取所有私信信息
def get_private_messages(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.PrivateMessage).offset(skip).limit(limit).all()

# 获取用户的所有私信
def get_private_messages_by_user(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(models.PrivateMessage).filter(models.PrivateMessage.sender_id == user_id).offset(skip).limit(limit).all()

# 根据私信id删除私信
def delete_private_message(db: Session, private_message_id: int):
    db_private_message = db.query(models.PrivateMessage).filter(models.PrivateMessage.id == private_message_id).first()
    if db_private_message:
        db.delete(db_private_message)
        db.commit()
        return db_private_message
    
