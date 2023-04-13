from datetime import datetime, timedelta
from typing import Optional
from passlib.context import CryptContext
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from secrets import token_urlsafe


from sqlalchemy.orm import Session

from ..sql_app import schemas, crud
from ..sql_app.database import get_db


SECRET_KEY = token_urlsafe(32)  # 生成32位随机密钥
ALGORITHM = "HS256"  # 生成 JWT token 使用的算法
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # JWT token 过期时间，单位为分钟

# 用于对密码进行哈希加密和验证的工具
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# 用于获取 JWT token 的 OAuth2 认证方案
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


# 对密码进行哈希加密
def hash_password(password: str):
    return pwd_context.hash(password)


# 验证密码是否正确
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)


# 生成 JWT token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# 验证 JWT token
def verify_token(token: str,key:str = SECRET_KEY)->str:
    try:
        return jwt.decode(token, key, algorithms=[ALGORITHM])
    except JWTError:
        return HTTPException(status_code=403,detail="身份验证失败")


# 从 JWT token 中获取用户信息
async def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")  # type: ignore
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = crud.get_user_by_username(db, username=token_data.username)  # type: ignore
    if user is None:
        raise credentials_exception
    return user


# 从 JWT token 中获取用户信息，如果用户不存在或用户不是管理员则返回 None
async def get_current_admin(
    current_user: schemas.User = Depends(get_current_user),
):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return current_user
