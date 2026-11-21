import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

# Load environment variables from the project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(PROJECT_ROOT / ".env")

# Read database configuration
DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
    "username": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
}

# Validate configuration
missing = [key for key, value in DB_CONFIG.items() if not value]

if missing:
    raise ValueError(
        f"Missing database configuration values: {', '.join(missing)}"
    )

# Create PostgreSQL connection URL safely
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=DB_CONFIG["username"],
    password=DB_CONFIG["password"],
    host=DB_CONFIG["host"],
    port=int(DB_CONFIG["port"]),
    database=DB_CONFIG["database"],
)

# Create database engine
engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def test_connection():
    """Test the PostgreSQL database connection."""
    with engine.connect() as connection:
        result = connection.execute(text("SELECT version();"))
        print("Database connection successful!")
        print(result.scalar())


if __name__ == "__main__":
    test_connection()