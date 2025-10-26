import sqlite3
import os
from data.resource_path import ensure_writable_db

# Path to your SQLite DB file
DB_PATH = ensure_writable_db()  # copies bundled DB to %LOCALAPPDATA%\LMS\library.db
# r"C:\Users\AISWARYA\OneDrive\Desktop\LMS\database\library.db"
def get_connection():
    # print(f"🔍 Connecting to DB at: {DB_PATH}")
    return sqlite3.connect(DB_PATH)

def create_tables():
    # print("✅ Creating tables...")
    conn = get_connection()
    cursor = conn.cursor()

    # Books Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            isbn TEXT UNIQUE NOT NULL,
            total_copies INTEGER NOT NULL CHECK (total_copies >= 0),
            available_copies INTEGER NOT NULL CHECK (available_copies >= 0)
        )
    ''')

    # Members Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT,
            phone TEXT,
            join_date TEXT NOT NULL
        )
    ''')

    # Transactions Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            book_id INTEGER NOT NULL,
            issue_date TEXT NOT NULL,
            due_date TEXT NOT NULL,
            return_date TEXT,
            fine REAL DEFAULT 0,
            FOREIGN KEY(member_id) REFERENCES members(member_id),
            FOREIGN KEY(book_id) REFERENCES books(book_id)
        )
    ''')

    # Users Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT CHECK(role IN ('librarian', 'staff')) NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_tables()


class DbConnectorDAO:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def get_connection(*args, **kwargs):
        """Wrapper to module-level function get_connection"""
        return get_connection(*args, **kwargs)

    @staticmethod
    def create_tables(*args, **kwargs):
        """Wrapper to module-level function create_tables"""
        return create_tables(*args, **kwargs)
