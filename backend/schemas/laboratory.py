from pydantic import BaseModel
from typing import Optional


class LaboratoryCreate(BaseModel):
    lab_name: str
    lab_address: Optional[str] = None


class LaboratoryUpdate(BaseModel):
    lab_name: Optional[str] = None
    lab_address: Optional[str] = None


class LaboratoryResponse(BaseModel):
    lab_id: int
    lab_name: str
    lab_address: Optional[str] = None

    class Config:
        from_attributes = True
