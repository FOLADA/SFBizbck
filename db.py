import sqlite3
from pathlib import Path

DB_PATH = Path("businesses.db")

def init_db() -> None:
    """Create the businesses table if not exists"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS businesses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT,
                description TEXT,
                services TEXT,
                contact TEXT,
                image_url TEXT,
                location TEXT,
                rating REAL
            )
        """)
        conn.commit()

def get_db():
    """Return a SQLite connection with dict-like row factory"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn
