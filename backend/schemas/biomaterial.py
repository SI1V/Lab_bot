from pydantic import BaseModel

# Схема для создания биоматериала
class BioMaterialCreate(BaseModel):
    bio_name: str

# Схема для обновления биоматериала (может содержать только имя)
class BioMaterialUpdate(BaseModel):
    bio_name: str

# Схема для ответа API
class BioMaterialResponse(BaseModel):
    bio_id: int
    bio_name: str

    class Config:
        from_attributes = True
