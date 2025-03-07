from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.research_service import (
    get_all_researches_service, get_research_by_id_service,
    create_research_service, update_research_service, delete_research_service
)
from backend.schemas.research import ResearchCreate, ResearchUpdate, ResearchResponse
from backend.core.database import get_db
from backend.core.templates import templates


router = APIRouter(prefix="/researches", tags=["Исследования"])

@router.get("/", response_model=list[ResearchResponse], summary="Получить список всех доступных исследований")
async def get_all_researches(db: AsyncSession = Depends(get_db)):
    return await get_all_researches_service(db)

@router.get("/{rch_id}", response_model=ResearchResponse, summary="Получить исследование по ID")
async def get_research_by_id(rch_id: int, db: AsyncSession = Depends(get_db)):
    return await get_research_by_id_service(db, rch_id)

@router.post("/", response_model=ResearchResponse, summary="Добавить исследование")
async def create_research(research_data: ResearchCreate, db: AsyncSession = Depends(get_db)):
    return await create_research_service(db, research_data)

@router.patch("/{rch_id}", response_model=ResearchResponse, summary="Обновить исследование по ID")
async def update_research(rch_id: int, research_data: ResearchUpdate, db: AsyncSession = Depends(get_db)):
    return await update_research_service(db, rch_id, research_data)

@router.delete("/{rch_id}", summary="Удалить исследование по ID")
async def delete_research(rch_id: int, db: AsyncSession = Depends(get_db)):
    deleted_research = await delete_research_service(db, rch_id)
    return {"message": "Research deleted"} if deleted_research else {"error": "Research not found"}
