from pydantic import BaseModel
from typing import Optional
import datetime

class APIToolBase(BaseModel):
    name: str
    method: str
    endpoint: str
    headers: Optional[str] = None
    body_params: Optional[str] = None
    description: Optional[str] = None
    trigger: Optional[str] = None

class APIToolCreate(APIToolBase):
    pass

class APIToolRead(APIToolBase):
    id: int
    user_id: int
    created_at: datetime.datetime

    class Config:
        orm_mode = True