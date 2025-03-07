from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.biomaterials import (
    crud_get_all_biomaterials, crud_get_biomaterial_by_id,
    crud_create_biomaterial, crud_update_biomaterial, crud_delete_biomaterial
)
from backend.schemas.biomaterial import BioMaterialCreate, BioMaterialUpdate

async def get_all_biomaterials_service(db: AsyncSession):
    return await crud_get_all_biomaterials(db)

async def get_biomaterial_by_id_service(db: AsyncSession, bio_id: int):
    return await crud_get_biomaterial_by_id(db, bio_id)

async def create_biomaterial_service(db: AsyncSession, biomaterial_data: BioMaterialCreate):
    return await crud_create_biomaterial(db, biomaterial_data)

async def update_biomaterial_service(db: AsyncSession, bio_id: int, biomaterial_data: BioMaterialUpdate):
    return await crud_update_biomaterial(db, bio_id, biomaterial_data)

async def delete_biomaterial_service(db: AsyncSession, bio_id: int):
    return await crud_delete_biomaterial(db, bio_id)
