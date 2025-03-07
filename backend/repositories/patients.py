from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from backend.models.patient import Patient
from backend.schemas.patient import PatientCreate, PatientUpdate

async def crud_get_all_patients(db: AsyncSession):
    result = await db.execute(select(Patient))
    return result.scalars().all()

async def crud_get_patient_by_id(db: AsyncSession, pat_id: int):
    return await db.get(Patient, pat_id)

async def crud_create_patient(db: AsyncSession, patient_data: PatientCreate):
    new_patient = Patient(**patient_data.model_dump())
    db.add(new_patient)
    await db.commit()
    await db.refresh(new_patient)
    return new_patient

async def crud_update_patient(db: AsyncSession, pat_id: int, patient_data: PatientUpdate):
    patient = await db.get(Patient, pat_id)
    if not patient:
        return None
    for key, value in patient_data.model_dump(exclude_unset=True).items():
        setattr(patient, key, value)
    await db.commit()
    await db.refresh(patient)
    return patient

async def crud_delete_patient(db: AsyncSession, pat_id: int):
    patient = await db.get(Patient, pat_id)
    if patient:
        await db.delete(patient)
        await db.commit()
    return patient
