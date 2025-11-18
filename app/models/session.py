from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.db import Base
import datetime

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, ForeignKey("agents.id"))
    channel = Column(String, nullable=True)
    started_at = Column(DateTime, default=datetime.datetime.utcnow)
    closed_at = Column(DateTime, nullable=True)
    tokens_in = Column(Integer, default=0)
    tokens_out = Column(Integer, default=0)
    avg_response_time = Column(Float, default=0.0)
    avg_session_duration = Column(Float, default=0.0)

    agent = relationship("Agent", back_populates="sessions")
    messages = relationship("Message", back_populates="session")