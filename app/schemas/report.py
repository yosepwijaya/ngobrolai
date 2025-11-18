from pydantic import BaseModel
from typing import Optional
import datetime

class ReportRequestCreate(BaseModel):
    channel: str
    params: Optional[str] = None
    period_start: Optional[datetime.datetime] = None
    period_end: Optional[datetime.datetime] = None

class ReportRequestRead(ReportRequestCreate):
    id: int
    user_id: int
    status: str
    file_url: Optional[str]
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True