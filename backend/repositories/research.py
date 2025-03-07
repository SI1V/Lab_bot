from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.research import ResearchCatalog
from backend.schemas.research import ResearchCreate, ResearchUpdate

async def crud_get_all_researches(db: AsyncSession):
    result = await db.execute(select(ResearchCatalog))
    return result.scalars().all()

async def crud_get_research_by_id(db: AsyncSession, rch_id: int):
    return await db.get(ResearchCatalog, rch_id)

async def crud_create_research(db: AsyncSession, research_data: ResearchCreate):
    new_research = ResearchCatalog(**research_data.model_dump())
    db.add(new_research)
    await db.commit()
    await db.refresh(new_research)
    return new_research

async def crud_update_research(db: AsyncSession, rch_id: int, research_data: ResearchUpdate):
    research = await db.get(ResearchCatalog, rch_id)
    if not research:
        return None
    for key, value in research_data.model_dump(exclude_unset=True).items():
        setattr(research, key, value)
    await db.commit()
    await db.refresh(research)
    return research

async def crud_delete_research(db: AsyncSession, rch_id: int):
    research = await db.get(ResearchCatalog, rch_id)
    if research:
        await db.delete(research)
        await db.commit()
    return research
