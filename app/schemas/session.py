from pydantic import BaseModel
from typing import Optional
import datetime

class SessionRead(BaseModel):
    id: int
    agent_id: int
    channel: Optional[str]
    started_at: datetime.datetime
    closed_at: Optional[datetime.datetime]
    tokens_in: int
    tokens_out: int
    avg_response_time: float
    avg_session_duration: float

    class Config:
        orm_mode = True