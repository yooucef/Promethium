from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional, List
from functools import lru_cache
from pathlib import Path

class Settings(BaseSettings):
    """
    Centralized application configuration.
    Reads from environment variables and .env file.
    """
    APP_NAME: str = "Promethium"
    APP_VERSION: str = "2.0.0-SoTA"
    DEBUG: bool = False
    
    # API
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    API_PREFIX: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["*"]

    # Database & Storage
    DATABASE_URL: str = "postgresql+asyncpg://admin:secret@db:5432/promethium"
    REDIS_URL: str = "redis://redis:6379/0"
    DATA_STORAGE_PATH: Path = Path("/data")
    ARTIFACT_STORAGE_PATH: Path = Path("/artifacts")

    # ML Configuration
    DEFAULT_DEVICE: str = "cuda"  # or "cpu"
    PRECISION: str = "16-mixed"

    # Worker
    CELERY_BROKER_URL: str = "redis://redis:6379/0"
    CELERY_RESULT_BACKEND: str = "redis://redis:6379/1"
    
    model_config = SettingsConfigDict(
        env_file=".env", 
        case_sensitive=True,
        extra="ignore"
    )

@lru_cache
def get_settings() -> Settings:
    return Settings()
