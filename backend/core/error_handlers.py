from fastapi import Request, FastAPI
from fastapi.responses import HTMLResponse
from backend.core.templates import templates

def register_exception_handlers(app: FastAPI):
    """Функция для регистрации глобальных обработчиков ошибок"""

    # 401 - Неавторизованный доступ
    @app.exception_handler(401)
    async def forbidden_exception_handler(request: Request, exc):
        return templates.TemplateResponse("pages/error.html", {
            "request": request,
            "status_code": 401,
            "message": "Не авторизован"
        }, status_code=401)


    # 403 - Доступ запрещен
    @app.exception_handler(403)
    async def forbidden_exception_handler(request: Request, exc):
        return templates.TemplateResponse("pages/error.html", {
            "request": request,
            "status_code": 403,
            "message": "Доступ запрещен"
        }, status_code=403)

    # 404 - Страница не найдена
    @app.exception_handler(404)
    async def not_found_exception_handler(request: Request, exc):
        return templates.TemplateResponse("pages/error.html", {
            "request": request,
            "status_code": 404,
            "message": "Страница не найдена"
        }, status_code=404)

    # 500 - Внутренняя ошибка сервера
    @app.exception_handler(500)
    async def internal_server_error_handler(request: Request, exc):
        return templates.TemplateResponse("pages/error.html", {
            "request": request,
            "status_code": 500,
            "message": "Ошибка на сервере"
        }, status_code=500)
