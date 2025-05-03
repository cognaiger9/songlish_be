# Songlish Backend

This is the backend service for Songlish, built with FastAPI and PostgreSQL (hosted on Supabase).

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up Supabase:
   - Go to [Supabase](https://supabase.com/) and create a new project
   - Get your project URL, API key, and database connection string
   - Create a `.env` file in the backend directory with the following variables:
```
# Supabase Settings
SUPABASE_URL=your_project_url
SUPABASE_KEY=your_api_key
SUPABASE_DB_URL=your_database_connection_string

# Local Database Settings (for development)
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=songlish

# API Keys
OPENAI_API_KEY=your_openai_api_key
SPOTIFY_CLIENT_ID=your_spotify_client_id
SPOTIFY_CLIENT_SECRET=your_spotify_client_secret

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, you can access the API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
backend/
├── app/
│   ├── api/
│   │   └── api_v1/
│   │       ├── endpoints/
│   │       └── api.py
│   ├── core/
│   │   └── config.py
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   ├── models/
│   │   ├── user.py
│   │   └── song.py
│   └── schemas/
│       └── song.py
├── requirements.txt
└── README.md
```

## Database Setup

The project uses Supabase for PostgreSQL hosting. To set up the database:

1. Go to the Supabase dashboard
2. Navigate to the SQL editor
3. Run the following SQL to create the necessary tables:

```sql
-- Create users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    is_active BOOLEAN DEFAULT TRUE,
    is_superuser BOOLEAN DEFAULT FALSE
);

-- Create songs table
CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    spotify_id VARCHAR(255) UNIQUE NOT NULL,
    title VARCHAR(255) NOT NULL,
    artist VARCHAR(255) NOT NULL,
    album VARCHAR(255),
    release_date VARCHAR(255),
    lyrics TEXT,
    difficulty_level INTEGER,
    genre VARCHAR(255)
);

-- Create lessons table
CREATE TABLE lessons (
    id SERIAL PRIMARY KEY,
    song_id INTEGER REFERENCES songs(id),
    title VARCHAR(255) NOT NULL,
    content TEXT,
    vocabulary TEXT,
    grammar_points TEXT,
    created_at VARCHAR(255)
);
```

## Development Tips

- Use the Supabase dashboard to manage your database
- The database connection will automatically use Supabase if SUPABASE_DB_URL is set
- For local development, you can use a local PostgreSQL instance
- Make sure to keep your `.env` file secure and never commit it to version control

### Port
Postgres: 2504