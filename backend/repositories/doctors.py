from fastapi import HTTPException

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.doctor import Doctor
from backend.schemas.doctor import DoctorCreate, DoctorUpdate

async def crud_get_all_doctors(db: AsyncSession):
    result = await db.execute(select(Doctor))
    return result.scalars().all()

async def crud_get_doctor_by_id(db: AsyncSession, doc_id: int):
    doctor = await db.get(Doctor, doc_id)
    if doctor is None:
        raise HTTPException(404, "Доктор не найден")
    return doctor

async def crud_create_doctor(db: AsyncSession, doctor_data: DoctorCreate):
    new_doctor = Doctor(**doctor_data.model_dump())
    db.add(new_doctor)
    await db.commit()
    await db.refresh(new_doctor)
    return new_doctor

async def crud_update_doctor(db: AsyncSession, doc_id: int, doctor_data: DoctorUpdate):
    doctor = await db.get(Doctor, doc_id)
    if not doctor:
        return None
    for key, value in doctor_data.model_dump(exclude_unset=True).items():
        setattr(doctor, key, value)
    await db.commit()
    await db.refresh(doctor)
    return doctor

async def crud_delete_doctor(db: AsyncSession, doc_id: int):
    doctor = await db.get(Doctor, doc_id)
    if doctor:
        await db.delete(doctor)
        await db.commit()
    return doctor
