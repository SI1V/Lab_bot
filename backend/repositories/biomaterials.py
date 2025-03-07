from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.biomaterial import BioMaterial
from backend.schemas.biomaterial import BioMaterialCreate, BioMaterialUpdate

async def crud_get_all_biomaterials(db: AsyncSession):
    result = await db.execute(select(BioMaterial))
    return result.scalars().all()

async def crud_get_biomaterial_by_id(db: AsyncSession, bio_id: int):
    biomaterial = await db.get(BioMaterial, bio_id)
    if biomaterial is None:
        raise HTTPException(404, "Биоматериал не найден")
    return biomaterial

async def crud_create_biomaterial(db: AsyncSession, biomaterial_data: BioMaterialCreate):
    new_biomaterial = BioMaterial(**biomaterial_data.model_dump())
    db.add(new_biomaterial)
    await db.commit()
    await db.refresh(new_biomaterial)
    return new_biomaterial

async def crud_update_biomaterial(db: AsyncSession, bio_id: int, biomaterial_data: BioMaterialUpdate):
    biomaterial = await db.get(BioMaterial, bio_id)
    if not biomaterial:
        return None
    for key, value in biomaterial_data.model_dump(exclude_unset=True).items():
        setattr(biomaterial, key, value)
    await db.commit()
    await db.refresh(biomaterial)
    return biomaterial

async def crud_delete_biomaterial(db: AsyncSession, bio_id: int):
    biomaterial = await db.get(BioMaterial, bio_id)
    if biomaterial:
        await db.delete(biomaterial)
        await db.commit()
    return biomaterial
