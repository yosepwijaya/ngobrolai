import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ngobrolai.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecret")
    GOOGLE_CLIENT_ID: str = os.getenv("GOOGLE_CLIENT_ID", "")
    GOOGLE_CLIENT_SECRET: str = os.getenv("GOOGLE_CLIENT_SECRET", "")
    CALLBACK_URL: str = os.getenv("CALLBACK_URL", "http://localhost:8000/auth/callback")
    
    class Config:
        env_file = ".env"

settings = Settings()
