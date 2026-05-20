from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # ── Base de datos ─────────────────────────────────────────────────────────
    DATABASE_URL: str

    # ── JWT ───────────────────────────────────────────────────────────────────
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # ── App ───────────────────────────────────────────────────────────────────
    ENVIRONMENT: str = "development"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Instancia global — importala desde cualquier módulo con:
# from app.config import settings
settings = Settings()
