from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class WaitlistBase(BaseModel):
    email: EmailStr
    status: str = "pending"
    position: Optional[int] = None

class WaitlistCreate(WaitlistBase):
    pass

class WaitlistResponse(WaitlistBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True 