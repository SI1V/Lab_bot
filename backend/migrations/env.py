import sys
import asyncio
from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context

# Добавляем backend в sys.path
sys.path.append("..")

# Импорт моделей
from backend.models.base import Base

# Загружаем конфигурацию из alembic.ini
config = context.config
fileConfig(config.config_file_name)

# Метаданные таблиц для Alembic
target_metadata = Base.metadata

# Получаем URL базы данных из alembic.ini
db_url = config.get_main_option("sqlalchemy.url")

# Если используется асинхронный движок, заменяем его на синхронный
if "sqlite+aiosqlite" in db_url:
    sync_db_url = db_url.replace("sqlite+aiosqlite", "sqlite")
elif "postgresql+asyncpg" in db_url:
    sync_db_url = db_url.replace("postgresql+asyncpg", "postgresql")
else:
    sync_db_url = db_url


def run_migrations_offline():
    """Запуск миграций в режиме без подключения к БД (использует SQL-скрипты)"""
    context.configure(url=sync_db_url, target_metadata=target_metadata, literal_binds=True)
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Запуск миграций с подключением к БД"""
    if "async" in db_url:  # Если используется асинхронная БД
        connectable = create_async_engine(db_url, poolclass=pool.NullPool)
        asyncio.run(async_migrations(connectable))
    else:  # Если используется обычная (синхронная) БД
        connectable = engine_from_config(config.get_section(config.config_ini_section), prefix="sqlalchemy.", poolclass=pool.NullPool)
        with connectable.connect() as connection:
            context.configure(connection=connection, target_metadata=target_metadata)
            with context.begin_transaction():
                context.run_migrations()


async def async_migrations(engine):
    """Асинхронное выполнение миграций для asyncpg/aiosqlite"""
    async with engine.connect() as connection:
        await connection.run_sync(do_migrations)


def do_migrations(connection):
    """Настройка и запуск миграций"""
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()


# Выбор режима выполнения миграций
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
