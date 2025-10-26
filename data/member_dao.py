#This code has the functions to interact with the members table.
import sqlite3

DB_PATH = r"C:\Users\AISWARYA\OneDrive\Desktop\LMS\database\library.db"

def connect():
    return sqlite3.connect(DB_PATH)

# 1. Add a New Member
def add_member(name, email, phone, join_date):
    conn = connect()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO members (name, email, phone, join_date)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, join_date))
        conn.commit()
    except Exception as e:
        # print("Error adding member:", e)
        pass
    finally:
        conn.close()

# 2. Get All Members
def get_all_members():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    conn.close()
    return members

# 3. Search Members by Name or Phone
def search_members(keyword):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM members
        WHERE name LIKE ? OR phone LIKE ?
    """, (f"%{keyword}%", f"%{keyword}%"))
    results = cursor.fetchall()
    conn.close()
    return results

# 4. Update Member Details
def update_member(member_id, name, email, phone, join_date):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE members
        SET name = ?, email = ?, phone = ?, join_date = ?
        WHERE member_id = ?
    """, (name, email, phone, join_date, member_id))
    conn.commit()
    conn.close()

# 5. Delete Member
def delete_member(member_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE member_id = ?", (member_id,))
    conn.commit()
    conn.close()


class MemberDaoDAO:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def connect(*args, **kwargs):
        """Wrapper to module-level function connect"""
        return connect(*args, **kwargs)

    @staticmethod
    def add_member(*args, **kwargs):
        """Wrapper to module-level function add_member"""
        return add_member(*args, **kwargs)

    @staticmethod
    def get_all_members(*args, **kwargs):
        """Wrapper to module-level function get_all_members"""
        return get_all_members(*args, **kwargs)

    @staticmethod
    def search_members(*args, **kwargs):
        """Wrapper to module-level function search_members"""
        return search_members(*args, **kwargs)

    @staticmethod
    def update_member(*args, **kwargs):
        """Wrapper to module-level function update_member"""
        return update_member(*args, **kwargs)

    @staticmethod
    def delete_member(*args, **kwargs):
        """Wrapper to module-level function delete_member"""
        return delete_member(*args, **kwargs)
