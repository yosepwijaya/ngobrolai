from fastapi import Request, HTTPException, status, Depends
from app.models.user import User
from app.db import SessionLocal
def get_current_user(request: Request):
    sub = request.cookies.get("user_sub")
    if not sub:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    db = SessionLocal()
    user = db.query(User).filter(User.sub == sub).first()
    db.close()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated")
    return user
def require_role(required_role: str):
    def role_checker(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return role_checker