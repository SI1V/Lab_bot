from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from backend.models.base import Base

class PatientLink(Base):
    __tablename__ = "patient_links"

    link_id = Column(Integer, primary_key=True, autoincrement=True)
    parent_id = Column(Integer, ForeignKey("patients.pat_id"), nullable=False)
    child_id = Column(Integer, ForeignKey("patients.pat_id"), nullable=False)

    parent = relationship("Patient", foreign_keys=[parent_id], back_populates="children")
    child = relationship("Patient", foreign_keys=[child_id], back_populates="parents")

    def __repr__(self):
        return f"<PatientLink(id={self.link_id}, parent={self.parent_id}, child={self.child_id})>"