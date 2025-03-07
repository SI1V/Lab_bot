from sqlalchemy import Column, Integer, Float, String, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import Base

class AnalysisResult(Base):
    __tablename__ = "analysis_results"

    ars_id = Column(Integer, primary_key=True, autoincrement=True)
    ars_analysis_id = Column(Integer, ForeignKey("analyses.ana_id", ondelete="CASCADE"), nullable=False)
    ars_value = Column(Float, nullable=False)  # Значение результата анализа
    ars_reference_range = Column(String(100), nullable=False)  # Референсный диапазон (например, "normal", "high")
    ars_reference_min = Column(Float, nullable=False)  # Минимальное значение референсного диапазона
    ars_reference_max = Column(Float, nullable=False)  # Максимальное значение референсного диапазона
    ars_unit_id = Column(Integer, ForeignKey("measurement_units.unit_id", ondelete="SET NULL"), nullable=True)  # Единица измерения

    analysis = relationship("Analysis", back_populates="results")
    unit = relationship("MeasurementUnit", back_populates="analysis_results")

    def __repr__(self):
        return f"<AnalysisResult(id={self.ars_id}, analysis={self.ars_analysis_id}, value={self.ars_value})>"