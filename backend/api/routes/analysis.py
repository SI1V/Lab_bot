from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.ext.asyncio import AsyncSession
from backend.core.database import get_db
from backend.services.analysis_service import (
    get_all_analyses_service, get_analysis_by_id_service,
    create_analysis_service, update_analysis_service, delete_analysis_service
)
from backend.schemas.analysis import AnalysisCreate, AnalysisUpdate, AnalysisResponse
from backend.core.templates import templates

router = APIRouter(prefix="/analyses", tags=["Анализы"])


@router.get("/", response_model=list, summary="Получить все анализы")
async def get_all_analyses(request: Request, db: AsyncSession = Depends(get_db)):
    # Получаем все анализы из сервиса
    analyses = await get_all_analyses_service(db)

    # Рендерим шаблон и передаем данные анализов в шаблон
    return templates.TemplateResponse("pages/analyses.html", {
        "request": request,
        "analyses": analyses
    })

@router.get("/{analysis_id}", response_model=AnalysisResponse, summary="Получить анализ по ID",
            description="Получить анализ по его уникальному идентификатору")
async def get_analysis_by_id(analysis_id: int, db: AsyncSession = Depends(get_db)):
    analysis = await get_analysis_by_id_service(db, analysis_id)
    if not analysis:
        raise HTTPException(status_code=404, detail="Анализ не найден")
    return analysis

@router.post("/", response_model=AnalysisResponse, status_code=201, summary="Создать новую запись по анализу")
async def create_analysis(analysis_in: AnalysisCreate, db: AsyncSession = Depends(get_db)):
    return await create_analysis_service(db, analysis_in)

@router.patch("/{analysis_id}", response_model=AnalysisResponse, summary="Обновить запись по анализу")
async def update_analysis(analysis_id: int, analysis_in: AnalysisUpdate, db: AsyncSession = Depends(get_db)):
    updated_analysis = await update_analysis_service(db, analysis_id, analysis_in)
    if not updated_analysis:
        raise HTTPException(status_code=404, detail="Анализ не найден")
    return updated_analysis

@router.delete("/{analysis_id}", status_code=204, summary="Удалить запись анализа по ID")
async def delete_analysis(analysis_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await delete_analysis_service(db, analysis_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Анализ не найден")
