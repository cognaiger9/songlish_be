from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.base import Base

class Waitlist(Base):
    __tablename__ = "waitlist"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    status = Column(String, default="pending")
    position = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now()) 