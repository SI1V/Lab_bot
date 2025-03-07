from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base

class ResearchCatalog(Base):
    __tablename__ = "research_catalog"

    rch_id = Column(Integer, primary_key=True, autoincrement=True)
    rch_name = Column(String(100), nullable=False)

    analyses = relationship("Analysis", back_populates="research")

    def __repr__(self):
        return f"<ResearchCatalog(id={self.rch_id}, name={self.rch_name})>"