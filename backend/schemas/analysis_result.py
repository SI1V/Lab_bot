from pydantic import BaseModel, Field
from backend.models.analysis_result import AnalysisResult
from backend.models.enums import ReferenceEnum

class AnalysisResultCreate(AnalysisResult):
    ars_analysis_id: int = Field(..., description="ID анализа")

class AnalysisResultUpdate(BaseModel):
    ars_value: float | None = None
    ars_reference_range: ReferenceEnum | None = None
    ars_reference_min: float | None = None
    ars_reference_max: float | None = None
    ars_unit_id: int | None = None

class AnalysisResultResponse(AnalysisResult):
    ars_id: int
    ars_analysis_id: int

    class Config:
        from_attributes = True  # Поддержка SQLAlchemy
