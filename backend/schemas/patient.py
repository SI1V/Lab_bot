from pydantic import BaseModel
from datetime import date
from backend.models.enums import GenderEnum

# Схема для создания пациента
class PatientCreate(BaseModel):
    pat_last_name: str
    pat_first_name: str
    pat_middle_name: str | None = None
    pat_gender: GenderEnum
    pat_birth_date: date

# Схема для обновления пациента (необязательные поля)
class PatientUpdate(BaseModel):
    pat_last_name: str | None = None
    pat_first_name: str | None = None
    pat_middle_name: str | None = None
    pat_gender: GenderEnum | None = None
    pat_birth_date: date | None = None

# Схема для ответа API
class PatientResponse(BaseModel):
    pat_id: int
    pat_last_name: str
    pat_first_name: str
    pat_middle_name: str | None
    pat_gender: GenderEnum
    pat_birth_date: date

    class Config:
        from_attributes = True  # Позволяет преобразовывать SQLAlchemy -> Pydantic
