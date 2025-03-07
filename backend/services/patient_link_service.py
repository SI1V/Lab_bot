from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.patient_links import (
    crud_get_all_links, crud_get_link_by_id,
    crud_create_link, crud_delete_link
)
from backend.schemas.patient_link import PatientLinkCreate

async def get_all_links_service(db: AsyncSession):
    return await crud_get_all_links(db)

async def get_link_by_id_service(db: AsyncSession, link_id: int):
    return await crud_get_link_by_id(db, link_id)

async def create_link_service(db: AsyncSession, link_data: PatientLinkCreate):
    return await crud_create_link(db, link_data)

async def delete_link_service(db: AsyncSession, link_id: int):
    return await crud_delete_link(db, link_id)
