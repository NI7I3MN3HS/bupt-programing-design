from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base,engine,SessionLocal

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    avatar_url = Column(String)
    introduction = Column(String)
    create_time = Column(String)
    update_time = Column(String)
    is_admin = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="author")
    comments = relationship("Comment", back_populates="author")
    followers = relationship(
        "Follow", back_populates="follower", foreign_keys="Follow.follower_id"
    )
    followed = relationship(
        "Follow", back_populates="followed", foreign_keys="Follow.followed_id"
    )
    likes = relationship("Like", back_populates="author")
    notifications = relationship("Notification", back_populates="receiver")
    sent_messages = relationship(
        "PrivateMessage", back_populates="sender", foreign_keys="PrivateMessage.sender_id"
    )
    received_messages = relationship(
        "PrivateMessage",
        back_populates="recipient",
        foreign_keys="PrivateMessage.recipient_id",
    )
'''
用户表（users）
id：用户ID，主键
username：用户名，唯一
email：电子邮件，唯一
password_hash：密码哈希值
avatar_url：头像URL
introduction：个人介绍
create_time：注册时间
update_time：最后一次更新时间
is_admin：是否为管理员，布尔类型
'''
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    create_time = Column(String)
    update_time = Column(String)
    is_deleted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    author = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post")
    likes = relationship("Like", back_populates="post")
'''
帖子表（posts）
id：帖子ID，主键
title：帖子标题
content：帖子内容
create_time：帖子创建时间
update_time：最后一次更新时间
is_deleted：是否已被删除，布尔类型
user_id：发帖用户ID，外键
'''
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    create_time = Column(String)
    update_time = Column(String)
    is_deleted = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    parent_id = Column(Integer, ForeignKey("comments.id"))

    author = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")
    parent = relationship("Comment", back_populates="children", remote_side=[id])
    children = relationship("Comment", back_populates="parent")
    likes = relationship("Like", back_populates="comment")
'''
评论表（comments）
id：评论ID，主键
content：评论内容
create_time：评论创建时间
update_time：最后一次更新时间
is_deleted：是否已被删除，布尔类型
user_id：评论用户ID，外键
post_id：所属帖子ID，外键
parent_id：父评论ID，外键，可以为空
'''
class Follow(Base):
    __tablename__ = "follows"

    id = Column(Integer, primary_key=True, index=True)
    follower_id = Column(Integer, ForeignKey("users.id"))
    followed_id = Column(Integer, ForeignKey("users.id"))

    follower = relationship("User", back_populates="followers", foreign_keys=[follower_id])
    followed = relationship("User", back_populates="followed", foreign_keys=[followed_id])
'''
关注表（follows）
id：关注ID，主键
follower_id：关注者ID，外键
followed_id：被关注者ID，外键
'''
class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    post_id = Column(Integer, ForeignKey("posts.id"))
    comment_id = Column(Integer, ForeignKey("comments.id"))

    author = relationship("User", back_populates="likes")
    post = relationship("Post", back_populates="likes")
    comment = relationship("Comment", back_populates="likes")
'''
点赞表（likes）
id：点赞ID，主键
user_id：点赞用户ID，外键
post_id：被点赞帖子ID，外键
comment_id：被点赞评论ID，外键，可以为空
'''
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    create_time = Column(String)
    is_read = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    receiver = relationship("User", back_populates="notifications")
'''
通知表（notifications）
id：通知ID，主键
content：通知内容
create_time：通知创建时间
is_read：是否已读，布尔类型
user_id：接收通知的用户ID，外键
'''
class PrivateMessage(Base):
    __tablename__ = "private_messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    create_time = Column(String)
    is_read = Column(Boolean, default=False)
    sender_id = Column(Integer, ForeignKey("users.id"))
    recipient_id = Column(Integer, ForeignKey("users.id"))

    sender = relationship("User", back_populates="sent_messages", foreign_keys=[sender_id])
    recipient = relationship(
        "User", back_populates="received_messages", foreign_keys=[recipient_id]
    )
'''
站内信表（private_messages）
id：站内信ID，主键
content：站内信内容
create_time：站内信创建时间
is_read：是否已读，布尔类型
sender_id：发送者ID，外键
recipient_id：接收者ID，外键
'''