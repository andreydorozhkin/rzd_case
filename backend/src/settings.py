from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    PROJECT_NAME: str

    class Config:
        env_file = Path(__file__).resolve().parent.parent.parent / ".env"
        case_sensitive = True


settings = Settings()
