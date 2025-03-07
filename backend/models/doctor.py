from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Doctor(Base):
    __tablename__ = "doctors"

    doc_id = Column(Integer, primary_key=True, autoincrement=True)
    doc_last_name = Column(String(100), nullable=False)
    doc_first_name = Column(String(100), nullable=False)
    doc_middle_name = Column(String(100), nullable=True)
    doc_clinic = Column(String(100), nullable=True)
    doc_specialization = Column(String(100), nullable=False)

    analyses = relationship("Analysis", back_populates="doctor")

    def __repr__(self):
        return f"<Doctor(id={self.doc_id}, name={self.doc_last_name} {self.doc_first_name})>"