from sqlalchemy import Column, Integer, ForeignKey, Table
from app.db import Base

agent_knowledge = Table(
    "agent_knowledge",
    Base.metadata,
    Column("agent_id", Integer, ForeignKey("agents.id"), primary_key=True),
    Column("document_id", Integer, ForeignKey("documents.id"), primary_key=True)
)