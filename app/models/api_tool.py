from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.db import Base
import datetime

class APITool(Base):
    __tablename__ = "api_tools"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    name = Column(String, nullable=False)
    method = Column(String, nullable=False)
    endpoint = Column(String, nullable=False)
    headers = Column(Text, nullable=True)  # JSON string for headers
    body_params = Column(Text, nullable=True)  # JSON string for body params
    description = Column(String, nullable=True)
    trigger = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="api_tools")