from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # API Settings
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Songlish"
    
    # Supabase Settings
    SUPABASE_URL: str = "https://your-project-ref.supabase.co"  # Replace with your Supabase project URL
    SUPABASE_KEY: str = "your-anon-key"  # Replace with your Supabase anon/public key
    SUPABASE_DB_URL: str = "postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres"  # Replace with your Supabase database connection string
    
    # Database Settings (for local development)
    POSTGRES_SERVER: str = "db.[YOUR-PROJECT-REF].supabase.co"  # Replace with your Supabase database host
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "[YOUR-PASSWORD]"  # Replace with your Supabase database password
    POSTGRES_DB: str = "postgres"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None
    
    # OpenAI Settings
    OPENAI_API_KEY: str = ""
    
    # Spotify Settings
    SPOTIFY_CLIENT_ID: str = ""
    SPOTIFY_CLIENT_SECRET: str = ""
    
    # JWT Settings
    SECRET_KEY: str = "your-secret-key-here"  # Change in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        case_sensitive = True
        env_file = ".env"

# Create settings instance
settings = Settings()


# Set database URI - prioritize Supabase connection if available
if settings.SUPABASE_DB_URL:
    settings.SQLALCHEMY_DATABASE_URI = settings.SUPABASE_DB_URL
    print("Using Supabase database URL")
elif not settings.SQLALCHEMY_DATABASE_URI:
    settings.SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}"
        f"@{settings.POSTGRES_SERVER}/{settings.POSTGRES_DB}"
    ) 