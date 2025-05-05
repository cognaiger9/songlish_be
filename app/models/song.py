from sqlalchemy import Column, Integer, String, Float, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    artist = Column(String(255), nullable=False)
    duration = Column(Integer)  # Duration in seconds
    genre = Column(String(100))
    image_url = Column(String(512))
    level = Column(Float, default=1.0)  # 1.0 to 5.0 scale
    
