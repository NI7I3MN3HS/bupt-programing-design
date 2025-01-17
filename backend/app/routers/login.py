from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, HTTPException, APIRouter
from ..core.security import (
    verify_password,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)

from ..sql_app import crud, schemas
from ..sql_app.database import get_db
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/login",
    tags=["login"],
)


@router.post("/", response_model=schemas.Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)
):
    # 验证用户名和密码是否正确
    user = crud.get_user_by_username(db, username=form_data.username)
    email = crud.get_user_by_email(db, email=form_data.username)
    if not user and not email:
        raise HTTPException(status_code=400, detail="Incorrect email or username")
    if user:
        if not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(
                status_code=400, detail="Incorrect username or password"
            )
    if email:
        if not verify_password(form_data.password, email.hashed_password):
            raise HTTPException(status_code=400, detail="Incorrect email or password")
        form_data.username = email.username
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": form_data.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
