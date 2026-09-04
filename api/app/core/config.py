import os
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field

class Settings(BaseSettings):
    PROJECT_NAME: str = "Vasooli Tracker API"
    
    POSTGRES_SERVER: Optional[str] = "localhost"
    POSTGRES_USER: Optional[str] = "postgres"
    POSTGRES_PASSWORD: Optional[str] = "postgres"
    POSTGRES_DB: Optional[str] = "vasooli"
    POSTGRES_PORT: int = 5432

    @computed_field
    @property
    def SQLALCHEMY_DATABASE_URI(self) -> str:
        # Fallback to SQLite: use /tmp on Vercel/serverless since /var/task is read-only
        if os.environ.get("VERCEL") or os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
            return "sqlite+aiosqlite:////tmp/vasooli.db"
        return "sqlite+aiosqlite:///./vasooli.db"

    SECRET_KEY: str = "supersecretkeyfortestingenvironmentonly"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    
    FINNHUB_API_KEY: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
