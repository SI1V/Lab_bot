from sqlalchemy import Column, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from backend.models.base import Base
from backend.models.enums import GenderEnum

class Patient(Base):
    __tablename__ = "patients"

    pat_id = Column(Integer, primary_key=True, autoincrement=True)
    pat_last_name = Column(String(100), nullable=False)
    pat_first_name = Column(String(100), nullable=False)
    pat_middle_name = Column(String(100), nullable=True)
    pat_gender = Column(Enum(GenderEnum), nullable=False)
    pat_birth_date = Column(Date, nullable=False)

    analyses = relationship("Analysis", back_populates="patient")
    children = relationship("PatientLink", foreign_keys="PatientLink.parent_id", back_populates="parent")
    parents = relationship("PatientLink", foreign_keys="PatientLink.child_id", back_populates="child")

    def __repr__(self):
        return f"<Patient(id={self.pat_id}, name={self.pat_last_name} {self.pat_first_name})>"