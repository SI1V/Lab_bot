from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.laboratories import (
    crud_get_all_labs, crud_get_lab_by_id,
    crud_create_lab, crud_update_lab, crud_delete_lab
)
from backend.schemas.laboratory import LaboratoryCreate, LaboratoryUpdate

async def get_all_labs_service(db: AsyncSession):
    return await crud_get_all_labs(db)

async def get_lab_by_id_service(db: AsyncSession, lab_id: int):
    return await crud_get_lab_by_id(db, lab_id)

async def create_lab_service(db: AsyncSession, lab_data: LaboratoryCreate):
    return await crud_create_lab(db, lab_data)

async def update_lab_service(db: AsyncSession, lab_id: int, lab_data: LaboratoryUpdate):
    return await crud_update_lab(db, lab_id, lab_data)

async def delete_lab_service(db: AsyncSession, lab_id: int):
    return await crud_delete_lab(db, lab_id)
