from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from backend.core.templates import templates

def register_accept_middleware(app: FastAPI):
    """Middleware для автоматического выбора HTML или JSON по заголовку Accept"""

    @app.middleware("http")
    async def handle_response(request: Request, call_next):
        response = await call_next(request)
        accept_header = request.headers.get("accept", "")

        if "text/html" in accept_header and hasattr(response, 'body') and response.body:
            try:
                response_json = response.json()
                return templates.TemplateResponse(
                    "base_template.html", {"request": request, "data": response_json}
                )
            except:
                pass  # Если не JSON, то пропускаем

        return response
