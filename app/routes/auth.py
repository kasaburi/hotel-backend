import os

from datetime import datetime, timedelta, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserLogin


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# =========================================================
# PASSWORD
# =========================================================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# =========================================================
# JWT
# =========================================================

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY is not configured")


ALGORITHM = "HS256"


def create_token(user_id: int):
    expire = datetime.now(timezone.utc) + timedelta(days=7)

    payload = {
        "userId": user_id,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )


# =========================================================
# SIGN UP
# =========================================================

@router.post("/sign_up")
def register(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):

    existing_user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=409,
            detail="This email address is already in use."
        )

    hashed_password = pwd_context.hash(
        user_data.password
    )

    user = User(
        first_name=user_data.firstName,
        last_name=user_data.lastName,
        age=user_data.age,
        email=user_data.email,
        password=hashed_password,
        address=user_data.address,
        phone=user_data.phone,
        zipcode=user_data.zipcode,
        avatar=user_data.avatar,
        gender=user_data.gender
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    token = create_token(user.id)

    return {
        "token": token,
        "userId": user.id,
        "userEmail": user.email,
        "message": "You have successfully registered."
    }


# =========================================================
# SIGN IN
# =========================================================

@router.post("/sign_in")
def login(
    user_data: UserLogin,
    db: Session = Depends(get_db)
):

    user = (
        db.query(User)
        .filter(User.email == user_data.email)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    if not pwd_context.verify(
        user_data.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password."
        )

    token = create_token(user.id)

    return {
        "token": token,
        "userId": user.id,
        "userEmail": user.email,
        "message": "You have successfully logged in."
    }