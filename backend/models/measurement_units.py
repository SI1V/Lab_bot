from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base

class MeasurementUnit(Base):
    __tablename__ = "measurement_units"

    unit_id = Column(Integer, primary_key=True, autoincrement=True)
    unit_name = Column(String(100), nullable=False)

    analysis_results = relationship("AnalysisResult", back_populates="unit")

    def __repr__(self):
        return f"<MeasurementUnit(id={self.unit_id}, name={self.unit_name})>"