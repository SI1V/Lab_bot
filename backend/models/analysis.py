from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Analysis(Base):
    __tablename__ = "analyses"

    ana_id = Column(Integer, primary_key=True, autoincrement=True)
    ana_patient_id = Column(Integer, ForeignKey("patients.pat_id"), nullable=False)
    ana_doctor_id = Column(Integer, ForeignKey("doctors.doc_id"), nullable=True)
    ana_research_id = Column(Integer, ForeignKey("research_catalog.rch_id"), nullable=False)
    ana_laboratory_id = Column(Integer, ForeignKey("laboratories.lab_id"), nullable=False)
    ana_biomaterial_id = Column(Integer, ForeignKey("bio_materials.bio_id"), nullable=False)
    ana_sample_taken = Column(DateTime, nullable=False)
    ana_sample_received = Column(DateTime, nullable=True)
    ana_result_printed = Column(DateTime, nullable=True)
    ana_age_years = Column(Integer, nullable=False)
    ana_age_months = Column(Integer, nullable=False)
    ana_comment = Column(String(500), nullable=True)
    ana_description = Column(String(500), nullable=True)
    ana_deviation_reason = Column(String(500), nullable=True)
    ana_expected_norm = Column(String(500), nullable=True)
    ana_target_range = Column(String(500), nullable=True)

    patient = relationship("Patient", back_populates="analyses")
    doctor = relationship("Doctor", back_populates="analyses")
    research = relationship("ResearchCatalog", back_populates="analyses")
    laboratory = relationship("Laboratory", back_populates="analyses")
    biomaterial = relationship("BioMaterial", back_populates="analyses")
    results = relationship("AnalysisResult", back_populates="analysis")

    def __repr__(self):
        return f"<Analysis(id={self.ana_id}, patient={self.ana_patient_id}, research={self.ana_research_id})>"