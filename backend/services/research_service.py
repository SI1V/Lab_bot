from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.research import (
    crud_get_all_researches, crud_get_research_by_id,
    crud_create_research, crud_update_research, crud_delete_research
)
from backend.schemas.research import ResearchCreate, ResearchUpdate

async def get_all_researches_service(db: AsyncSession):
    return await crud_get_all_researches(db)

async def get_research_by_id_service(db: AsyncSession, rch_id: int):
    return await crud_get_research_by_id(db, rch_id)

async def create_research_service(db: AsyncSession, research_data: ResearchCreate):
    return await crud_create_research(db, research_data)

async def update_research_service(db: AsyncSession, rch_id: int, research_data: ResearchUpdate):
    return await crud_update_research(db, rch_id, research_data)

async def delete_research_service(db: AsyncSession, rch_id: int):
    return await crud_delete_research(db, rch_id)
