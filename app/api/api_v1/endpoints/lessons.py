from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.song import Lesson
from app.schemas.lesson import LessonCreate, LessonResponse

router = APIRouter()

@router.get("/", response_model=List[LessonResponse])
def get_lessons(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    lessons = db.query(Lesson).offset(skip).limit(limit).all()
    return lessons

@router.get("/{lesson_id}", response_model=LessonResponse)
def get_lesson(
    lesson_id: int,
    db: Session = Depends(get_db)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if lesson is None:
        raise HTTPException(status_code=404, detail="Lesson not found")
    return lesson

@router.post("/", response_model=LessonResponse)
def create_lesson(
    lesson: LessonCreate,
    db: Session = Depends(get_db)
):
    db_lesson = Lesson(**lesson.dict())
    db.add(db_lesson)
    db.commit()
    db.refresh(db_lesson)
    return db_lesson 