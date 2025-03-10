from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.api.routes import main_router
from backend.api.routes.auth import auth_router
from backend.api.routes.home import home_router
from backend.core.error_handlers import register_exception_handlers
from backend.dependencies.auth import get_current_user
from backend.core.database import apply_migrations
from backend.core.logger_config import get_logger
from middleware.handle_response import register_accept_middleware
from alembic import command
from alembic.config import Config

logger = get_logger()

app = FastAPI(
    title="Laboratory Results API",
    description="API для управления результатами лабораторных анализов",
    version="0.1.0",
    contact={
        "name": "S-i1-V",
        "email": "Vanosaprikin@gmail.com"
    },
    docs_url="/d",
    redoc_url="/r"
)

app.include_router(auth_router)
app.include_router(home_router)
app.include_router(main_router)

# Подключаем основной роутер с защитой по JWT
# app.include_router(main_router, dependencies=[Depends(get_current_user)])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все домены
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы (GET, POST, PUT, DELETE)
    allow_headers=["*"],  # Разрешаем все заголовки
)


# Подключаем статику
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

register_exception_handlers(app)
register_accept_middleware(app)


@app.on_event("startup")
def on_startup():
    logger.info("Применение миграций к БД ...")
    apply_migrations()
    logger.info("Успешный запуск приложения ...")


