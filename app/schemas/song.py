from pydantic import BaseModel
from typing import Optional

class SongBase(BaseModel):
    spotify_id: str
    title: str
    artist: str
    album: Optional[str] = None
    release_date: Optional[str] = None
    lyrics: Optional[str] = None
    difficulty_level: Optional[int] = None
    genre: Optional[str] = None

class SongCreate(SongBase):
    pass

class SongResponse(SongBase):
    id: int

    class Config:
        from_attributes = True 