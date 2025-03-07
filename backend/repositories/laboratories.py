from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.laboratory import Laboratory
from backend.schemas.laboratory import LaboratoryCreate, LaboratoryUpdate

async def crud_get_all_labs(db: AsyncSession):
    result = await db.execute(select(Laboratory))
    return result.scalars().all()

async def crud_get_lab_by_id(db: AsyncSession, lab_id: int):
    return await db.get(Laboratory, lab_id)

async def crud_create_lab(db: AsyncSession, lab_data: LaboratoryCreate):
    new_lab = Laboratory(**lab_data.model_dump())
    db.add(new_lab)
    await db.commit()
    await db.refresh(new_lab)
    return new_lab

async def crud_update_lab(db: AsyncSession, lab_id: int, lab_data: LaboratoryUpdate):
    lab = await db.get(Laboratory, lab_id)
    if not lab:
        return None
    for key, value in lab_data.model_dump(exclude_unset=True).items():
        setattr(lab, key, value)
    await db.commit()
    await db.refresh(lab)
    return lab

async def crud_delete_lab(db: AsyncSession, lab_id: int):
    lab = await db.get(Laboratory, lab_id)
    if lab:
        await db.delete(lab)
        await db.commit()
    return lab
