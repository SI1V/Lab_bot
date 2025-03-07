from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.patient_link import PatientLink
from backend.schemas.patient_link import PatientLinkCreate

async def crud_get_all_links(db: AsyncSession):
    result = await db.execute(select(PatientLink))
    return result.scalars().all()

async def crud_get_link_by_id(db: AsyncSession, link_id: int):
    return await db.get(PatientLink, link_id)

async def crud_create_link(db: AsyncSession, link_data: PatientLinkCreate):
    new_link = PatientLink(**link_data.model_dump())
    db.add(new_link)
    await db.commit()
    await db.refresh(new_link)
    return new_link

async def crud_delete_link(db: AsyncSession, link_id: int):
    link = await db.get(PatientLink, link_id)
    if link:
        await db.delete(link)
        await db.commit()
    return link
