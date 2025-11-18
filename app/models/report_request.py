from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.db import Base
import datetime

class ReportRequest(Base):
    __tablename__ = "report_requests"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    channel = Column(String, nullable=False)
    status = Column(String, default="New")
    params = Column(String, nullable=True)
    period_start = Column(DateTime, nullable=True)
    period_end = Column(DateTime, nullable=True)
    file_url = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow)