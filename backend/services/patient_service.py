from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.patients import (
    crud_get_all_patients, crud_get_patient_by_id,
    crud_create_patient, crud_update_patient, crud_delete_patient
)
from backend.schemas.patient import PatientCreate, PatientUpdate

async def get_all_patients_service(db: AsyncSession):
    return await crud_get_all_patients(db)

async def get_patient_by_id_service(db: AsyncSession, pat_id: int):
    return await crud_get_patient_by_id(db, pat_id)

async def create_patient_service(db: AsyncSession, patient_data: PatientCreate):
    return await crud_create_patient(db, patient_data)

async def update_patient_service(db: AsyncSession, pat_id: int, patient_data: PatientUpdate):
    return await crud_update_patient(db, pat_id, patient_data)

async def delete_patient_service(db: AsyncSession, pat_id: int):
    return await crud_delete_patient(db, pat_id)
