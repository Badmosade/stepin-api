from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Resource(Base):
    __tablename__ = "resources"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    website = Column(String, nullable=True)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    state = relationship("State", foreign_keys=[state_id])
    category = relationship("Category", foreign_keys=[category_id])
