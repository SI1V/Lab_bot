from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.analysis import Analysis
from backend.schemas.analysis import AnalysisCreate, AnalysisUpdate

async def crud_create_analysis(session: AsyncSession, analysis_in: AnalysisCreate) -> Analysis:
    new_analysis = Analysis(**analysis_in.model_dump())
    session.add(new_analysis)
    await session.commit()
    await session.refresh(new_analysis)
    return new_analysis

async def crud_get_analysis_by_id(session: AsyncSession, analysis_id: int) -> Analysis | None:
    return await session.get(Analysis, analysis_id)

async def crud_get_all_analyses(session: AsyncSession) -> list[Analysis]:
    results = await session.execute(select(Analysis))
    return results.scalars().all()

async def crud_update_analysis(session: AsyncSession, analysis_id: int, analysis_in: AnalysisUpdate) -> Analysis | None:
    analysis = await session.get(Analysis, analysis_id)
    if not analysis:
        return None
    for key, value in analysis_in.model_dump(exclude_unset=True).items():
        setattr(analysis, key, value)
    await session.commit()
    await session.refresh(analysis)
    return analysis

async def crud_delete_analysis(session: AsyncSession, analysis_id: int) -> bool:
    analysis = await session.get(Analysis, analysis_id)
    if not analysis:
        return False
    await session.delete(analysis)
    await session.commit()
    return True
