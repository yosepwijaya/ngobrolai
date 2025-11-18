from pydantic import BaseModel
from typing import Optional
import datetime

class DocumentBase(BaseModel):
    filename: str
    filetype: str
    size: Optional[int] = None
    status: Optional[str] = "Processing"

class DocumentRead(DocumentBase):
    id: int
    created_at: datetime.datetime
    ready_at: Optional[datetime.datetime]
    uploader_id: int

    class Config:
        orm_mode = True