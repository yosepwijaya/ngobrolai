from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserRead
from app.models.user import User
from app.db import SessionLocal

router = APIRouter()

@router.post("/login", response_model=UserRead)
def login(email: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    db.close()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user