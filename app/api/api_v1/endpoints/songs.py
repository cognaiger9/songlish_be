from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.models.song import Song
from app.schemas.song import SongDisplay, SongListResponse, SongCreate

router = APIRouter()

@router.get("/", response_model=SongListResponse)
async def get_songs(db: Session = Depends(get_db)):
    """
    Get all songs for selection
    """
    try:
        songs = db.query(Song).all()
        return SongListResponse(
            songs=songs,
            total=len(songs)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error getting songs: {str(e)}"
        )

@router.get("/{song_id}", response_model=SongDisplay)
async def get_song(song_id: int, db: Session = Depends(get_db)):
    """
    Get a specific song by ID
    """
    song = db.query(Song).filter(Song.id == song_id).first()
    if not song:
        raise HTTPException(
            status_code=404,
            detail="Song not found"
        )
    return song

@router.post("/", response_model=SongDisplay)
async def create_song(song_data: SongCreate, db: Session = Depends(get_db)):
    """
    Create a new song
    """
    try:
        # Create new song instance
        new_song = Song(
            title=song_data.title,
            artist=song_data.artist,
            duration=song_data.duration,
            genre=song_data.genre,
            image_url=song_data.image_url,
            level=song_data.level
        )
        
        # Add to database
        db.add(new_song)
        db.commit()
        db.refresh(new_song)
        
        return new_song
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating song: {str(e)}"
        ) 