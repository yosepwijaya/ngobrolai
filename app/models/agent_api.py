from sqlalchemy import Column, Integer, ForeignKey, Table
from app.db import Base

agent_api = Table(
    "agent_api",
    Base.metadata,
    Column("agent_id", Integer, ForeignKey("agents.id"), primary_key=True),
    Column("api_tool_id", Integer, ForeignKey("api_tools.id"), primary_key=True)
)