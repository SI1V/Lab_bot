from pydantic import BaseModel

# Схема для создания исследования
class ResearchCreate(BaseModel):
    rch_name: str

# Схема для обновления исследования
class ResearchUpdate(BaseModel):
    rch_name: str | None = None

# Схема для ответа API
class ResearchResponse(BaseModel):
    rch_id: int
    rch_name: str

    class Config:
        from_attributes = True  # Позволяет преобразовывать SQLAlchemy -> Pydantic
