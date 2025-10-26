import sqlite3

DB_PATH = r"C:\Users\AISWARYA\OneDrive\Desktop\LMS\database\library.db"

def connect():
    return sqlite3.connect(DB_PATH)

# 1. Add User (register)
def add_user(username, password, role):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        """, (username, password, role))
        conn.commit()
    except sqlite3.IntegrityError:
        # print("❌ Username already exists.")
        pass
    finally:
        conn.close()

# 2. Login Authentication
def authenticate_user(username, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT user_id, role FROM users
        WHERE username = ? AND password = ?
    """, (username, password))
    result = cursor.fetchone()
    conn.close()
    return result  # (user_id, role) or None

# 3. Get User by ID
def get_user_by_id(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT username, role FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result


class UserDaoDAO:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def connect(*args, **kwargs):
        """Wrapper to module-level function connect"""
        return connect(*args, **kwargs)

    @staticmethod
    def add_user(*args, **kwargs):
        """Wrapper to module-level function add_user"""
        return add_user(*args, **kwargs)

    @staticmethod
    def authenticate_user(*args, **kwargs):
        """Wrapper to module-level function authenticate_user"""
        return authenticate_user(*args, **kwargs)

    @staticmethod
    def get_user_by_id(*args, **kwargs):
        """Wrapper to module-level function get_user_by_id"""
        return get_user_by_id(*args, **kwargs)
