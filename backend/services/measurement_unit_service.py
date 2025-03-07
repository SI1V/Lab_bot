from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.measurement_units import (
    crud_get_all_units, crud_get_unit_by_id,
    crud_create_unit, crud_update_unit, crud_delete_unit
)
from backend.schemas.measurement_unit import MeasurementUnitCreate, MeasurementUnitUpdate

async def get_all_units_service(db: AsyncSession):
    return await crud_get_all_units(db)

async def get_unit_by_id_service(db: AsyncSession, unit_id: int):
    return await crud_get_unit_by_id(db, unit_id)

async def create_unit_service(db: AsyncSession, unit_data: MeasurementUnitCreate):
    return await crud_create_unit(db, unit_data)

async def update_unit_service(db: AsyncSession, unit_id: int, unit_data: MeasurementUnitUpdate):
    return await crud_update_unit(db, unit_id, unit_data)

async def delete_unit_service(db: AsyncSession, unit_id: int):
    return await crud_delete_unit(db, unit_id)
