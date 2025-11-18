from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from app.db import Base
import datetime

class APITestLog(Base):
    __tablename__ = "api_test_logs"
    id = Column(Integer, primary_key=True)
    api_tool_id = Column(Integer, ForeignKey("api_tools.id"))
    tested_by = Column(Integer, ForeignKey("users.id"))
    status = Column(String)
    response = Column(Text)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)