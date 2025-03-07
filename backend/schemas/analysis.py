from pydantic import BaseModel, ConfigDict
from datetime import datetime
from typing import Optional

class AnalysisBase(BaseModel):
    ana_patient_id: int
    ana_doctor_id: Optional[int] = None
    ana_research_id: int
    ana_laboratory_id: int
    ana_biomaterial_id: int
    ana_sample_taken: datetime
    ana_sample_received: Optional[datetime] = None
    ana_result_printed: Optional[datetime] = None
    ana_age_years: int
    ana_age_months: int
    ana_comment: Optional[str] = None
    ana_description: Optional[str] = None
    ana_deviation_reason: Optional[str] = None
    ana_expected_norm: Optional[str] = None
    ana_target_range: Optional[str] = None

class AnalysisCreate(AnalysisBase):
    pass

class AnalysisUpdate(BaseModel):
    ana_doctor_id: Optional[int] = None
    ana_sample_received: Optional[datetime] = None
    ana_result_printed: Optional[datetime] = None
    ana_comment: Optional[str] = None
    ana_description: Optional[str] = None
    ana_deviation_reason: Optional[str] = None
    ana_expected_norm: Optional[str] = None
    ana_target_range: Optional[str] = None

class AnalysisResponse(AnalysisBase):
    ana_id: int

    class Config:
        from_attributes = True
