from typing import List, Union, Optional
from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    username: str
    email: str
    introduction: Optional[str] = None


class UserCreate(UserBase):
    password_hash: str
    avatar_url: Optional[str] = None


class UserUpdate(UserBase):
    username: Optional[str] = None
    email: Optional[str] = None
    password_hash: Optional[str] = None
    avatar_url: Optional[str] = None
    introduction: Optional[str] = None
           

class User(UserBase):
    id: int
    avatar_url: Optional[str] = None
    create_time: datetime
    update_time: datetime
    is_admin: bool

    class Config:
        orm_mode = True

class PostBase(BaseModel):
    title: str
    content: str


class PostCreate(PostBase):
    user_id: int


class PostUpdate(PostBase):
    title: Optional[str] = None
    content: Optional[str] = None


class Post(PostBase):
    id: int
    user_id: int
    is_deleted: bool = False
    create_time:datetime
    update_time:datetime
    author: User
    class Config:
        orm_mode = True


class CommentBase(BaseModel):
    content: str
    user_id: int
    post_id: int
    parent_id: Union[int, None] = None


class CommentCreate(CommentBase):
    pass

class CommentUpdate(CommentBase):
    content: Optional[str] = None
    is_deleted: Optional[bool] = False

class Comment(CommentBase):
    id: int
    is_deleted: bool = False
    create_time:datetime
    update_time:datetime
    author: User
    post: Post
    parent: Union["Comment", None] = None
    children: List["Comment"] = []

    class Config:
        orm_mode = True


class FollowBase(BaseModel):
    follower_id: int
    followed_id: int


class FollowCreate(FollowBase):
    pass


class Follow(FollowBase):
    id: int
    follower: User
    followed: User

    class Config:
        orm_mode = True


class LikeBase(BaseModel):
    user_id: int
    post_id: Optional[int] = None
    comment_id: Optional[int] = None


class LikeCreate(LikeBase):
    pass


class Like(LikeBase):
    id: int
    author: User
    post: Post 
    comment: Comment 

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
    receiver: User

    class Config:
        orm_mode = True

class PrivateMessageBase(BaseModel):
    content: str
    sender_id: int
    receiver_id: int

class PrivateMessageCreate(PrivateMessageBase):
    pass

class PrivateMessage(PrivateMessageBase):
    id: int
    create_time: datetime
    is_read: bool
    sender: User
    receiver: User

    class Config:
        orm_mode = True
