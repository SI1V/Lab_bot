from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.measurement_units import MeasurementUnit
from backend.schemas.measurement_unit import MeasurementUnitCreate, MeasurementUnitUpdate

async def crud_get_all_units(db: AsyncSession):
    result = await db.execute(select(MeasurementUnit))
    return result.scalars().all()

async def crud_get_unit_by_id(db: AsyncSession, unit_id: int):
    return await db.get(MeasurementUnit, unit_id)

async def crud_create_unit(db: AsyncSession, unit_data: MeasurementUnitCreate):
    new_unit = MeasurementUnit(**unit_data.model_dump())
    db.add(new_unit)
    await db.commit()
    await db.refresh(new_unit)
    return new_unit

async def crud_update_unit(db: AsyncSession, unit_id: int, unit_data: MeasurementUnitUpdate):
    unit = await db.get(MeasurementUnit, unit_id)
    if not unit:
        return None
    for key, value in unit_data.model_dump(exclude_unset=True).items():
        setattr(unit, key, value)
    await db.commit()
    await db.refresh(unit)
    return unit

async def crud_delete_unit(db: AsyncSession, unit_id: int):
    unit = await db.get(MeasurementUnit, unit_id)
    if unit:
        await db.delete(unit)
        await db.commit()
    return unit
