from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from backend.core.settings import settings
from backend.models.base import Base
from alembic import command
from alembic.config import Config

# Создаем асинхронный движок
engine = create_async_engine(settings.DB_URL, echo=settings.DB_ECHO)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Функция получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Функция для корректного завершения работы с БД
async def close_db():
    await engine.dispose()


# Функция для применения миграций
async def apply_migrations():
    """Применяем миграции при старте приложения"""
    config = Config("alembic.ini")  # Указываем путь к alembic.ini

    # Устанавливаем URL подключения к базе данных из настроек
    config.set_main_option("sqlalchemy.url", settings.DB_URL)

    # Применяем миграции
    command.upgrade(config, "head")  # Применяем все миграции до последней версии

