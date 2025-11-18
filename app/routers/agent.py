from fastapi import APIRouter, HTTPException
from app.models.agent import Agent
from app.schemas.agent import AgentRead, AgentCreate
from app.db import SessionLocal

router = APIRouter()

@router.get("/", response_model=list[AgentRead])
def get_agents():
    db = SessionLocal()
    agents = db.query(Agent).all()
    db.close()
    return agents

@router.post("/", response_model=AgentRead)
def create_agent(agent: AgentCreate):
    db = SessionLocal()
    obj = Agent(**agent.dict())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    db.close()
    return obj