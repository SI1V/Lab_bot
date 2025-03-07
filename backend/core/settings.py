import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    SECRET_KEY: str = os.getenv("SECRET_KEY", "default_secret_key")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

    DB_URL: str = os.getenv("DB_URL", "sqlite+aiosqlite:///./lab_bot.db")
    DB_ECHO: bool = os.getenv("DB_ECHO", "False").lower() in ("true", "1")


settings = Settings()
