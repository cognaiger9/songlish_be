from typing import List, Tuple
from sqlalchemy.orm import Session
from app.models.song import Song
from app.schemas.song import SongDisplay, SongCreate

class SongService:
    def __init__(self, db: Session):
        self.db = db

    def get_songs(self) -> Tuple[List[Song], int]:
        """
        Get all songs from database
        """
        songs = self.db.query(Song).all()
        return songs, len(songs)

    def get_song_by_id(self, song_id: int) -> Song:
        """
        Get a specific song by ID
        """
        return self.db.query(Song).filter(Song.id == song_id).first()

    def create_song(self, song_data: SongCreate) -> Song:
        """
        Create a new song in database
        """
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
        self.db.add(new_song)
        self.db.commit()
        self.db.refresh(new_song)
        
        return new_song 