from fastapi import Request, HTTPException, status, Depends
# from app.models.user import User # Ensure this model exists
from app.db import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(request: Request):
    # This is a placeholder. Implement actual JWT or Session check here.
    sub = request.cookies.get("user_sub")
    if not sub:
        # For development, you might want to return a mock user or raise 401
        # raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
        return {"id": 1, "role": "Creator", "sub": "mock_user"}
    
    # Logic to fetch user from DB would go here
    return {"id": 1, "role": "Creator", "sub": sub}

def require_role(required_role: str):
    def role_checker(user = Depends(get_current_user)):
        # Simple mock check
        if user["role"] != required_role:
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return role_checker
