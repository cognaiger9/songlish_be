from sqlalchemy import create_engine
from app.core.config import settings
from app.db.base import Base
from app.models.waitlist import Waitlist

def init_db():
    # Create database engine
    engine = create_engine(settings.SUPABASE_DB_URL)
    
    # Create all tables
    Base.metadata.create_all(bind=engine)
    
    print("Database tables created successfully!")

if __name__ == "__main__":
    init_db() 