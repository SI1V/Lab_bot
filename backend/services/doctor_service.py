from sqlalchemy.ext.asyncio import AsyncSession
from backend.repositories.doctors import (
    crud_get_all_doctors, crud_get_doctor_by_id,
    crud_create_doctor, crud_update_doctor, crud_delete_doctor
)
from backend.schemas.doctor import DoctorCreate, DoctorUpdate

async def get_all_doctors_service(db: AsyncSession):
    return await crud_get_all_doctors(db)

async def get_doctor_by_id_service(db: AsyncSession, doc_id: int):
    return await crud_get_doctor_by_id(db, doc_id)

async def create_doctor_service(db: AsyncSession, doctor_data: DoctorCreate):
    return await crud_create_doctor(db, doctor_data)

async def update_doctor_service(db: AsyncSession, doc_id: int, doctor_data: DoctorUpdate):
    return await crud_update_doctor(db, doc_id, doctor_data)

async def delete_doctor_service(db: AsyncSession, doc_id: int):
    return await crud_delete_doctor(db, doc_id)
