from fastapi import APIRouter, Depends, HTTPException
from app.models.user import User
from app.schemas.user import UserRead
from app.db import SessionLocal

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def get_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users