from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from backend.core.templates import templates
from backend.core.logger_config import logger

home_router = APIRouter(tags=["Главная страница"], include_in_schema=False)


@home_router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    logger.info("Обращение к главной странице")
    return templates.TemplateResponse("pages/index.html", {"request": request})