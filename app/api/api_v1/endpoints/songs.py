from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.song import Song
from app.schemas.song import SongCreate, SongResponse

router = APIRouter()

@router.get("/", response_model=List[SongResponse])
def get_songs(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    songs = db.query(Song).offset(skip).limit(limit).all()
    return songs

@router.get("/{song_id}", response_model=SongResponse)
def get_song(
    song_id: int,
    db: Session = Depends(get_db)
):
    song = db.query(Song).filter(Song.id == song_id).first()
    if song is None:
        raise HTTPException(status_code=404, detail="Song not found")
    return song

@router.post("/", response_model=SongResponse)
def create_song(
    song: SongCreate,
    db: Session = Depends(get_db)
):
    db_song = Song(**song.dict())
    db.add(db_song)
    db.commit()
    db.refresh(db_song)
    return db_song 