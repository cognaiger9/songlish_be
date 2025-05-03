from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
import os

app = FastAPI(
    title="Songlish API",
    description="Backend API for Songlish - Learn English through songs",
    version="1.0.0"
)

# Get environment
ENVIRONMENT = os.getenv("ENVIRONMENT", "development")

# Configure CORS
if ENVIRONMENT == "development":
    # In development, allow all origins
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    # In production, restrict to specific domains
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[
            "http://localhost:3000",  # Local development
            "https://*.vercel.app",   # Vercel deployments
            "https://songlish.vercel.app",  # Your production domain
            "https://*.ngrok.io",     # ngrok domains
            "https://*.ngrok-free.app" # New ngrok domains
        ],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# Import and include routers
from app.api.api_v1.api import api_router
app.include_router(api_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to Songlish API"} 