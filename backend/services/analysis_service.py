from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.analyses import (
    crud_get_all_analyses, crud_get_analysis_by_id,
    crud_create_analysis, crud_update_analysis, crud_delete_analysis
)
from backend.schemas.analysis import AnalysisCreate, AnalysisUpdate

async def get_all_analyses_service(db: AsyncSession):
    return await crud_get_all_analyses(db)

async def get_analysis_by_id_service(db: AsyncSession, analysis_id: int):
    return await crud_get_analysis_by_id(db, analysis_id)

async def create_analysis_service(db: AsyncSession, analysis_data: AnalysisCreate):
    return await crud_create_analysis(db, analysis_data)

async def update_analysis_service(db: AsyncSession, analysis_id: int, analysis_data: AnalysisUpdate):
    return await crud_update_analysis(db, analysis_id, analysis_data)

async def delete_analysis_service(db: AsyncSession, analysis_id: int):
    return await crud_delete_analysis(db, analysis_id)
