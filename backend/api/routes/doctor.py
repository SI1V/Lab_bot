from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.ext.asyncio import AsyncSession
from backend.services.doctor_service import (
    get_all_doctors_service, get_doctor_by_id_service,
    create_doctor_service, update_doctor_service, delete_doctor_service
)
from backend.schemas.doctor import DoctorCreate, DoctorUpdate, DoctorResponse
from backend.core.database import get_db
from backend.core.templates import templates
# from backend.core.logger_config import logger

router = APIRouter(prefix="/doctors", tags=["Доктора"])


@router.get("/", response_model=list[DoctorResponse], summary="Получить список всех докторов")
async def get_all_doctors(request: Request, db: AsyncSession = Depends(get_db)):
    doctors = await get_all_doctors_service(db)
    doctors =  templates.TemplateResponse("pages/doctors.html", {"request": request, "doctors": doctors})
    return doctors


@router.get("/{doc_id}", response_model=DoctorResponse, summary="Получить информацию о докторе по его id")
async def get_doctor_by_id(doc_id: int, db: AsyncSession = Depends(get_db)):
    return await get_doctor_by_id_service(db, doc_id)


@router.post("/", response_model=DoctorResponse, summary="Создать новую запись о докторе")
async def create_doctor(doctor_data: DoctorCreate, db: AsyncSession = Depends(get_db)):
    return await create_doctor_service(db, doctor_data)


@router.patch("/{doc_id}", response_model=DoctorResponse, summary="Обновить информацию о докторе")
async def update_doctor(doc_id: int, doctor_data: DoctorUpdate, db: AsyncSession = Depends(get_db)):
    return await update_doctor_service(db, doc_id, doctor_data)


@router.delete("/{doc_id}", summary="Удалить запись о докторе")
async def delete_doctor(doc_id: int, db: AsyncSession = Depends(get_db)):
    deleted_doctor = await delete_doctor_service(db, doc_id)
    return {"message": "Doctor deleted"} if deleted_doctor else {"error": "Doctor not found"}
