import sqlite3
from datetime import datetime
from .db_connector import get_connection

DB_PATH = r"C:\Users\AISWARYA\OneDrive\Desktop\LMS\database\library.db"

def connect():
    return sqlite3.connect(DB_PATH)

# 1. Issue a Book
def issue_book(member_id, book_id, issue_date, due_date):
    conn = connect()
    cur = conn.cursor()

    try:
        # Check if book is available
        cur.execute("SELECT available_copies FROM books WHERE book_id = ?", (book_id,))
        result = cur.fetchone()
        if result and result[0] > 0:
            # Add transaction
            cur.execute("""
                INSERT INTO transactions (member_id, book_id, issue_date, due_date)
                VALUES (?, ?, ?, ?)
            """, (member_id, book_id, issue_date, due_date))
            
            # Decrease available_copies
            cur.execute("""
                UPDATE books SET available_copies = available_copies - 1
                WHERE book_id = ?
            """, (book_id,))

            conn.commit()
            return True
        else:
            # print("❌ Book not available.")
            return False
    except Exception as e:
        # print("❌ Error issuing book:", e)
        return False
    finally:
        conn.close()

# 2. Return a Book
def return_book(transaction_id, return_date, fine):
    conn = connect()
    cur = conn.cursor()

    try:
        # Get book_id from transaction
        cur.execute("SELECT book_id FROM transactions WHERE transaction_id = ?", (transaction_id,))
        result = cur.fetchone()
        if not result:
            # print("❌ Transaction not found.")
            return False

        book_id = result[0]

        # Update transaction
        cur.execute("""
            UPDATE transactions SET return_date = ?, fine = ?
            WHERE transaction_id = ?
        """, (return_date, fine, transaction_id))

        # Increase available_copies
        cur.execute("""
            UPDATE books SET available_copies = available_copies + 1
            WHERE book_id = ?
        """, (book_id,))

        conn.commit()
        return True
    except Exception as e:
        # print("❌ Error returning book:", e)
        return False
    finally:
        conn.close()

# 3. Get All Issued Books (Not Yet Returned)
def get_issued_books():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT t.transaction_id, m.name, b.title, t.issue_date, t.due_date
        FROM transactions t
        JOIN members m ON t.member_id = m.member_id
        JOIN books b ON t.book_id = b.book_id
        WHERE t.return_date IS NULL
    """)
    results = cur.fetchall()
    conn.close()
    return results

# 4. Get Overdue Books
def get_overdue_books():
    today = datetime.now().strftime("%Y-%m-%d")
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT t.transaction_id, m.name, b.title, t.issue_date, t.due_date
        FROM transactions t
        JOIN members m ON t.member_id = m.member_id
        JOIN books b ON t.book_id = b.book_id
        WHERE t.return_date IS NULL AND t.due_date < ?
    """, (today,))
    results = cur.fetchall()
    conn.close()
    return results

# 5. Get All Transactions (for return book listbox)
def get_all_transactions():
    conn = connect()
    cur = conn.cursor()
    cur.execute("""
        SELECT t.transaction_id, m.name, b.title, t.issue_date, t.due_date, t.return_date, t.fine
        FROM transactions t
        JOIN members m ON t.member_id = m.member_id
        JOIN books b ON t.book_id = b.book_id
        ORDER BY t.transaction_id DESC
    """)
    results = cur.fetchall()
    conn.close()
    return results



#fetches and returns members name by using member id
def get_member_name(member_id):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM members WHERE member_id = ?", (member_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else "Unknown"


class TransactionDaoDAO:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def connect(*args, **kwargs):
        """Wrapper to module-level function connect"""
        return connect(*args, **kwargs)

    @staticmethod
    def issue_book(*args, **kwargs):
        """Wrapper to module-level function issue_book"""
        return issue_book(*args, **kwargs)

    @staticmethod
    def return_book(*args, **kwargs):
        """Wrapper to module-level function return_book"""
        return return_book(*args, **kwargs)

    @staticmethod
    def get_issued_books(*args, **kwargs):
        """Wrapper to module-level function get_issued_books"""
        return get_issued_books(*args, **kwargs)

    @staticmethod
    def get_overdue_books(*args, **kwargs):
        """Wrapper to module-level function get_overdue_books"""
        return get_overdue_books(*args, **kwargs)

    @staticmethod
    def get_all_transactions(*args, **kwargs):
        """Wrapper to module-level function get_all_transactions"""
        return get_all_transactions(*args, **kwargs)


    @staticmethod
    def get_member_name(*args, **kwargs):
        """Wrapper to module-level function get_member_name"""
        return get_member_name(*args, **kwargs)
