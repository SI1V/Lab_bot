from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base

class BioMaterial(Base):
    __tablename__ = "bio_materials"

    bio_id = Column(Integer, primary_key=True, autoincrement=True)
    bio_name = Column(String(100), nullable=False)

    analyses = relationship("Analysis", back_populates="biomaterial")

    def __repr__(self):
        return f"<BioMaterial(id={self.bio_id}, name={self.bio_name})>"