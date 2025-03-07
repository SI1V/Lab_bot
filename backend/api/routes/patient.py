from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.patient_service import (
    get_all_patients_service, get_patient_by_id_service,
    create_patient_service, update_patient_service, delete_patient_service
)
from backend.schemas.patient import PatientCreate, PatientUpdate, PatientResponse
from backend.core.database import get_db
from backend.core.templates import templates

router = APIRouter(prefix="/patients", tags=["Пациенты"])

@router.get("/", response_model=list[PatientResponse], summary="Получение записей по всем пациентам")
async def get_all_patients(db: AsyncSession = Depends(get_db)):
    return await get_all_patients_service(db)

@router.get("/{pat_id}", response_model=PatientResponse, summary="Получение записи по ID пациента")
async def get_patient_by_id(pat_id: int, db: AsyncSession = Depends(get_db)):
    return await get_patient_by_id_service(db, pat_id)

@router.post("/", response_model=PatientResponse, summary="Создание новой записи по пациенту")
async def create_patient(patient_data: PatientCreate, db: AsyncSession = Depends(get_db)):
    return await create_patient_service(db, patient_data)

@router.patch("/{pat_id}", response_model=PatientResponse, summary="Обновление данных по пациенту")
async def update_patient(pat_id: int, patient_data: PatientUpdate, db: AsyncSession = Depends(get_db)):
    return await update_patient_service(db, pat_id, patient_data)

@router.delete("/{pat_id}", summary="Удаление записи по ID пациента")
async def delete_patient(pat_id: int, db: AsyncSession = Depends(get_db)):
    deleted_patient = await delete_patient_service(db, pat_id)
    return {"message": "Patient deleted"} if deleted_patient else {"error": "Patient not found"}
