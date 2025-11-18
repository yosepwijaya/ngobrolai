from sqlalchemy import Column, Integer, ForeignKey, String, LargeBinary
from app.db import Base

class DocumentVector(Base):
    __tablename__ = "document_vectors"
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    passage_text = Column(String)
    embedding = Column(LargeBinary)
    chunk_index = Column(Integer)