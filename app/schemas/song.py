from typing import Optional, List
from pydantic import BaseModel, Field

class SongBase(BaseModel):
    title: str
    artist: str
    duration: int
    genre: str
    image_url: str
    level: float = Field(ge=1.0, le=5.0)

class SongCreate(SongBase):
    pass

class SongDisplay(SongBase):
    id: int

    class Config:
        from_attributes = True

class SongListResponse(BaseModel):
    songs: List[SongDisplay]
    total: int 