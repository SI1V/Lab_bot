from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse, HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.lab_service import (
    get_all_labs_service, get_lab_by_id_service,
    create_lab_service, update_lab_service, delete_lab_service
)
from backend.schemas.laboratory import LaboratoryCreate, LaboratoryUpdate, LaboratoryResponse
from backend.core.database import get_db
from backend.core.templates import templates

router = APIRouter(prefix="/labs", tags=["Лаборатории"])


@router.get("/", summary="Получить все лаборатории")
async def get_all_labs(request: Request, db: AsyncSession = Depends(get_db)):
    """
    Получает список всех лабораторий.
    Возвращает HTML или JSON в зависимости от заголовка Accept.
    """
    # Получаем список лабораторий
    labs = await get_all_labs_service(db)

    # Проверяем заголовок Accept в запросе
    accept_header = request.headers.get("accept", "")

    # Если запрос от браузера (HTML)
    if "text/html" in accept_header:
        return templates.TemplateResponse("pages/labs.html", {"request": request, "labs": labs})

    # В противном случае (API-запрос, JSON)
    return labs

@router.get("/{lab_id}", response_model=LaboratoryResponse, summary="Получить лабораторию по ID")
async def get_lab_by_id(lab_id: int, db: AsyncSession = Depends(get_db)):
    return await get_lab_by_id_service(db, lab_id)

@router.post("/", response_model=LaboratoryResponse, summary="Создать запись о лаборатории")
async def create_lab(lab_data: LaboratoryCreate, db: AsyncSession = Depends(get_db)):
    return await create_lab_service(db, lab_data)

@router.patch("/{lab_id}", response_model=LaboratoryResponse, summary="Обновить запись о лаборатории")
async def update_lab(lab_id: int, lab_data: LaboratoryUpdate, db: AsyncSession = Depends(get_db)):
    return await update_lab_service(db, lab_id, lab_data)

@router.delete("/{lab_id}", summary="Удалить запись о лаборатории")
async def delete_lab(lab_id: int, db: AsyncSession = Depends(get_db)):
    deleted_lab = await delete_lab_service(db, lab_id)
    return {"message": "Lab deleted"} if deleted_lab else {"error": "Lab not found"}
