from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base

class Song(Base):
    id = Column(Integer, primary_key=True, index=True)
    spotify_id = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    artist = Column(String, nullable=False)
    album = Column(String)
    release_date = Column(String)
    lyrics = Column(Text)
    difficulty_level = Column(Integer)  # 1-5 scale
    genre = Column(String)
    
    # Relationships
    lessons = relationship("Lesson", back_populates="song")

class Lesson(Base):
    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey("song.id"))
    title = Column(String, nullable=False)
    content = Column(Text)
    vocabulary = Column(Text)  # JSON string of vocabulary words and definitions
    grammar_points = Column(Text)  # JSON string of grammar points
    created_at = Column(String)  # ISO format datetime
    
    # Relationships
    song = relationship("Song", back_populates="lessons") 