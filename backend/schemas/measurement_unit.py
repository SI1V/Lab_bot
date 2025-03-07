from pydantic import BaseModel

# Схема для создания единицы измерения
class MeasurementUnitCreate(BaseModel):
    unit_name: str

# Схема для обновления единицы измерения
class MeasurementUnitUpdate(BaseModel):
    unit_name: str | None = None

# Схема для ответа API
class MeasurementUnitResponse(BaseModel):
    unit_id: int
    unit_name: str

    class Config:
        from_attributes = True
