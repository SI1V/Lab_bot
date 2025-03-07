from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.biomaterial_service import (
    get_all_biomaterials_service, get_biomaterial_by_id_service,
    create_biomaterial_service, update_biomaterial_service, delete_biomaterial_service
)
from backend.schemas.biomaterial import BioMaterialCreate, BioMaterialUpdate, BioMaterialResponse
from backend.core.database import get_db
from backend.core.templates import templates

router = APIRouter(prefix="/biomaterials", tags=["Биоматериалы"])

# TODO Надо отображать страницу которая будет рендериться jinja2 и при запросе роута выводить ее
@router.get("/", response_model=list[BioMaterialResponse], summary="Получить все доступные биоматериалы")
async def get_all_biomaterials(db: AsyncSession = Depends(get_db)):
    return await get_all_biomaterials_service(db)

@router.get("/{bio_id}", response_model=BioMaterialResponse, summary="Получить информацию о биоматериале по его id")
async def get_biomaterial_by_id(bio_id: int, db: AsyncSession = Depends(get_db)):
    return await get_biomaterial_by_id_service(db, bio_id)

@router.post("/", response_model=BioMaterialResponse, summary="Создать новую запись о биоматериале")
async def create_biomaterial(biomaterial_data: BioMaterialCreate, db: AsyncSession = Depends(get_db)):
    return await create_biomaterial_service(db, biomaterial_data)

@router.patch("/{bio_id}", response_model=BioMaterialResponse, summary="Обновить информацию о биоматериале")
async def update_biomaterial(bio_id: int, biomaterial_data: BioMaterialUpdate, db: AsyncSession = Depends(get_db)):
    return await update_biomaterial_service(db, bio_id, biomaterial_data)

@router.delete("/{bio_id}", summary="Удалить запись о биоматериале")
async def delete_biomaterial(bio_id: int, db: AsyncSession = Depends(get_db)):
    deleted_biomaterial = await delete_biomaterial_service(db, bio_id)
    return {"message": "Biomaterial deleted"} if deleted_biomaterial else {"error": "Biomaterial not found"}
