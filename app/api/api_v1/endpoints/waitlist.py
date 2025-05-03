from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.models.waitlist import Waitlist
from app.schemas.waitlist import WaitlistCreate, WaitlistResponse

router = APIRouter()

@router.post("/", response_model=WaitlistResponse)
def create_waitlist_entry(
    waitlist_entry: WaitlistCreate,
    db: Session = Depends(get_db)
):
    # Check if email already exists
    db_entry = db.query(Waitlist).filter(Waitlist.email == waitlist_entry.email).first()
    if db_entry:
        raise HTTPException(status_code=400, detail="Email already registered in waitlist")
    
    # Get the next position number
    last_position = db.query(Waitlist).order_by(Waitlist.position.desc()).first()
    next_position = (last_position.position + 1) if last_position else 1
    
    # Create new waitlist entry
    db_waitlist = Waitlist(
        email=waitlist_entry.email,
        status=waitlist_entry.status,
        position=next_position
    )
    db.add(db_waitlist)
    db.commit()
    db.refresh(db_waitlist)
    return db_waitlist

@router.get("/", response_model=List[WaitlistResponse])
def get_waitlist_entries(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    entries = db.query(Waitlist).offset(skip).limit(limit).all()
    return entries 