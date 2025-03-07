from pydantic import BaseModel, Field

# Схема для создания связи между пациентами
class PatientLinkCreate(BaseModel):
    parent_id: int = Field(..., gt=0, description="ID родителя")
    child_id: int = Field(..., gt=0, description="ID ребенка")

# Схема для ответа API
class PatientLinkResponse(BaseModel):
    link_id: int
    parent_id: int
    child_id: int

    class Config:
        from_attributes = True 
