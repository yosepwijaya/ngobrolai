from pydantic import BaseModel
from typing import Optional
import datetime

class UserBase(BaseModel):
    email: str
    name: Optional[str] = None
    picture: Optional[str] = None
    role: str = "Creator"

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int
    created_at: datetime.datetime
    last_login: datetime.datetime

    class Config:
        orm_mode = True