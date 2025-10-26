#This code has the functions to interact with the books table.
import sqlite3

DB_PATH = r"C:\Users\AISWARYA\OneDrive\Desktop\LMS\database\library.db"

def connect():
    return sqlite3.connect(DB_PATH)

# 1. Add Book
def add_book(title, author, isbn, total_copies):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO books (title, author, isbn, total_copies, available_copies)
            VALUES (?, ?, ?, ?, ?)
        """, (title, author, isbn, total_copies, total_copies))
        conn.commit()
    except sqlite3.IntegrityError as e:
        # print("Error:", e)
        pass
    finally:
        conn.close()

# 2. Get All Books
def get_all_books():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

# 3. Search Books by Title or Author
def search_books(keyword):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM books 
        WHERE title LIKE ? OR author LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    result = cursor.fetchall()
    conn.close()
    return result

# 4. Update Book
def update_book(book_id, title, author, isbn, total_copies, available_copies):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE books
        SET title = ?, author = ?, isbn = ?, total_copies = ?, available_copies = ?
        WHERE book_id = ?
    """, (title, author, isbn, total_copies, available_copies, book_id))
    conn.commit()
    conn.close()

# 5. Delete Book
def delete_book(book_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE book_id = ?", (book_id,))
    conn.commit()
    conn.close()


class BookDaoDAO:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def connect(*args, **kwargs):
        """Wrapper to module-level function connect"""
        return connect(*args, **kwargs)

    @staticmethod
    def add_book(*args, **kwargs):
        """Wrapper to module-level function add_book"""
        return add_book(*args, **kwargs)

    @staticmethod
    def get_all_books(*args, **kwargs):
        """Wrapper to module-level function get_all_books"""
        return get_all_books(*args, **kwargs)

    @staticmethod
    def search_books(*args, **kwargs):
        """Wrapper to module-level function search_books"""
        return search_books(*args, **kwargs)

    @staticmethod
    def update_book(*args, **kwargs):
        """Wrapper to module-level function update_book"""
        return update_book(*args, **kwargs)

    @staticmethod
    def delete_book(*args, **kwargs):
        """Wrapper to module-level function delete_book"""
        return delete_book(*args, **kwargs)
