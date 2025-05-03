from pydantic import BaseModel
from typing import Optional

class LessonBase(BaseModel):
    song_id: int
    title: str
    content: Optional[str] = None
    vocabulary: Optional[str] = None
    grammar_points: Optional[str] = None
    created_at: Optional[str] = None

class LessonCreate(LessonBase):
    pass

class LessonResponse(LessonBase):
    id: int

    class Config:
        from_attributes = True 