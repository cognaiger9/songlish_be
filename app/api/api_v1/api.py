from fastapi import APIRouter
from app.api.api_v1.endpoints import songs, users, test, waitlist

api_router = APIRouter()

api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(songs.router, prefix="/songs", tags=["songs"])
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(waitlist.router, prefix="/waitlist", tags=["waitlist"]) 