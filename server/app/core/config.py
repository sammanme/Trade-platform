# from pydantic import BaseSettings
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Trading Platform"
    debug: bool = False
    class Config:
        env_file = ".env"
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://user:pass@localhost:5432/marketdb"
    REDIS_URL: str = "redis://localhost:6379"

settings = Settings()
