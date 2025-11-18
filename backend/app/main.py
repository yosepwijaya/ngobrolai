from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Note: You will need to create these router files in app/routers/
# from app.routers import auth, user, agent, analytics, document, api_tool, report

app = FastAPI(title="Ngobrol.ai Dashboard")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Uncomment these when you have created the router files
# app.include_router(auth.router, prefix="/auth", tags=["auth"])
# app.include_router(user.router, prefix="/users", tags=["users"])
# app.include_router(agent.router, prefix="/agents", tags=["agents"])
# app.include_router(analytics.router, prefix="/analytics", tags=["analytics"])
# app.include_router(document.router, prefix="/documents", tags=["documents"])
# app.include_router(api_tool.router, prefix="/api-tools", tags=["api-tools"])
# app.include_router(report.router, prefix="/reports", tags=["reports"])

@app.get("/")
def read_root():
    return {"message": "Welcome to Ngobrol.ai API"}
