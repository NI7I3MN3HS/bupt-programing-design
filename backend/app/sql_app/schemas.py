from typing import List, Union, Optional
from datetime import datetime
from pydantic import BaseModel, Field
from fastapi import UploadFile, File


class Code(BaseModel):
    code: str


class password(BaseModel):
    password: str = Field(min_length=6, max_length=24)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class Email(BaseModel):
    email: str = Field(regex=r"\w{2,32}\@\w+\.\w+", max_length=64)


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=20)


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=24)


class UserUpdate(UserBase):
    email: str = Field(regex=r"\w{2,32}\@\w+\.\w+", max_length=64)
    introduction: str = Field(None, max_length=1024)


class User(UserBase):
    id: int
    hashed_password: str
    email: str = Field(regex=r"\w{2,32}\@\w+\.\w+", max_length=64)
    avatar_url: str = Field(None, max_length=256)
    introduction: str = Field(None, max_length=1024)
    create_time: datetime
    update_time: datetime
    is_admin: bool
    is_active: bool

    class Config:
        orm_mode = True


class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=64)
    content: str = Field(min_length=1)


class PostUpdate(PostBase):
    id: int


class Post(PostBase):
    id: int
    user_id: int
    is_deleted: bool = False
    create_time: datetime
    update_time: datetime

    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str = Field(min_length=1)
    post_id: int
    parent_id: Union[int, None] = None


class CommentCreate(CommentBase):
    reply_user_id: int = 0


class Comment(CommentBase):
    id: int
    user_id: int
    reply_user_id: int = 0
    create_time: datetime
    update_time: datetime

    class Config:
        orm_mode = True


class FollowBase(BaseModel):
    followed_id: int


class FollowCreate(FollowBase):
    pass


class Follow(FollowBase):
    id: int
    follower_id: int

    class Config:
        orm_mode = True


class LikeBase(BaseModel):
    post_id: Optional[int] = None
    comment_id: Optional[int] = None


class LikeCreate(LikeBase):
    pass


class Like(LikeBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class NotificationBase(BaseModel):
    content: str
    user_id: int


class NotificationCreate(NotificationBase):
    pass


class Notification(NotificationBase):
    id: int
    create_time: datetime
    is_read: bool

    class Config:
        orm_mode = True
