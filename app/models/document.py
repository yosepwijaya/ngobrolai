from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base
import datetime

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True)
    filename = Column(String, nullable=False)
    filetype = Column(String, nullable=False)
    size = Column(Integer)
    status = Column(String, default="Processing")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    ready_at = Column(DateTime, nullable=True)
    uploader_id = Column(Integer, ForeignKey("users.id"))

    uploader = relationship("User", back_populates="documents")