from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from backend.models.base import Base

class Laboratory(Base):
    __tablename__ = "laboratories"

    lab_id = Column(Integer, primary_key=True, autoincrement=True)
    lab_name = Column(String(100), nullable=False)
    lab_address = Column(String(200), nullable=True)

    analyses = relationship("Analysis", back_populates="laboratory")

    def __repr__(self):
        return f"<Laboratory(id={self.lab_id}, name={self.lab_name})>"