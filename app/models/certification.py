from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Certification(Base):
    __tablename__ = "certifications"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    duration = Column(String, nullable=True)
    cost = Column(String, nullable=True)
    website = Column(String, nullable=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)

    state = relationship("State")
