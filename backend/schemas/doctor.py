from pydantic import BaseModel, ConfigDict
from typing import Optional

# Схема для создания доктора
class DoctorCreate(BaseModel):
    doc_last_name: str
    doc_first_name: str
    doc_middle_name: Optional[str] = None
    doc_clinic: Optional[str] = None
    doc_specialization: str


# Схема для обновления доктора
class DoctorUpdate(BaseModel):
    doc_last_name: Optional[str] = None
    doc_first_name: Optional[str] = None
    doc_middle_name: Optional[str] = None
    doc_clinic: Optional[str] = None
    doc_specialization: Optional[str] = None


# Схема ответа API
class DoctorResponse(BaseModel):
    doc_id: int
    doc_last_name: str
    doc_first_name: str
    doc_middle_name: Optional[str]
    doc_clinic: Optional[str]
    doc_specialization: str

    class Config:
        from_attributes = True
