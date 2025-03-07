from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.patient_link_service import (
    get_all_links_service, get_link_by_id_service,
    create_link_service, delete_link_service
)
from backend.schemas.patient_link import PatientLinkCreate, PatientLinkResponse
from backend.core.database import get_db
from backend.core.templates import templates

router = APIRouter(prefix="/patient-links", tags=["Пациенты"])

@router.get("/", response_model=list[PatientLinkResponse], summary="Получить пациентов которые добавлены для наблюдения")
async def get_all_links(db: AsyncSession = Depends(get_db)):
    return await get_all_links_service(db)

@router.get("/{link_id}", response_model=PatientLinkResponse, summary="Получить пациента по ID")
async def get_link_by_id(link_id: int, db: AsyncSession = Depends(get_db)):
    return await get_link_by_id_service(db, link_id)

@router.post("/", response_model=PatientLinkResponse, summary="Добавить пациента для наблюдения")
async def create_link(link_data: PatientLinkCreate, db: AsyncSession = Depends(get_db)):
    return await create_link_service(db, link_data)

@router.delete("/{link_id}", summary="Удалить пациента по ID")
async def delete_link(link_id: int, db: AsyncSession = Depends(get_db)):
    deleted_link = await delete_link_service(db, link_id)
    return {"message": "Link deleted"} if deleted_link else {"error": "Link not found"}
