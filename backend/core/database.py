from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from backend.core.settings import settings
from backend.models.base import Base

# Создаем асинхронный движок
engine = create_async_engine(settings.DB_URL, echo=settings.DB_ECHO)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Функция получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# Функция для создания всех таблиц (если нет миграций)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Функция для корректного завершения работы с БД
async def close_db():
    await engine.dispose()


