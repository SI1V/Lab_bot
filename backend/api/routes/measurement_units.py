from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.measurement_unit_service import (
    get_all_units_service, get_unit_by_id_service,
    create_unit_service, update_unit_service, delete_unit_service
)
from backend.schemas.measurement_unit import MeasurementUnitCreate, MeasurementUnitUpdate, MeasurementUnitResponse
from backend.core.database import get_db
from backend.core.templates import templates

router = APIRouter(prefix="/units", tags=["Единицы измерения"], include_in_schema=False)

@router.get("/", response_model=list[MeasurementUnitResponse], summary="Получить все единицы измерения")
async def get_all_units(db: AsyncSession = Depends(get_db)):
    return await get_all_units_service(db)

@router.get("/{unit_id}", response_model=MeasurementUnitResponse, summary="Получить единицу измерения по ID")
async def get_unit_by_id(unit_id: int, db: AsyncSession = Depends(get_db)):
    return await get_unit_by_id_service(db, unit_id)

@router.post("/", response_model=MeasurementUnitResponse, summary="Создать новую единицу измерения")
async def create_unit(unit_data: MeasurementUnitCreate, db: AsyncSession = Depends(get_db)):
    return await create_unit_service(db, unit_data)

@router.patch("/{unit_id}", response_model=MeasurementUnitResponse, summary="Обновить данные единицы измерения")
async def update_unit(unit_id: int, unit_data: MeasurementUnitUpdate, db: AsyncSession = Depends(get_db)):
    return await update_unit_service(db, unit_id, unit_data)

@router.delete("/{unit_id}", summary="Удалить единицу измерения по ID")
async def delete_unit(unit_id: int, db: AsyncSession = Depends(get_db)):
    deleted_unit = await delete_unit_service(db, unit_id)
    return {"message": "Unit deleted"} if deleted_unit else {"error": "Unit not found"}
