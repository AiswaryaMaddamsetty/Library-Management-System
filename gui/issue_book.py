import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from business.book_service import BookService
from business.member_service import MemberService
from business.transaction_service import TransactionService  

def issue_book_gui():
    def submit_issue():
        book = book_var.get()
        member = member_var.get()

        if not book or not member:
            messagebox.showwarning("Input Error", "Please select both book and member.")
            return

        book_id = int(book.split('-')[0])
        member_id = int(member.split('-')[0])
        issue_date = datetime.now().strftime("%Y-%m-%d")
        due_date = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")

        # ✅ Now issue book through business layer
        success = TransactionService.issue_book(member_id, book_id, issue_date, due_date)

        if success:
            messagebox.showinfo("Success", "Book issued successfully.")
            window.destroy()
        else:
            messagebox.showerror("Error", "Failed to issue book. It may already be issued or unavailable.")

    # --- GUI Window ---
    window = tk.Toplevel()
    window.title("Issue Book")

    # --- Book Dropdown ---
    tk.Label(window, text="Select Book").pack()
    book_var = tk.StringVar(window)
    book_options = [f"{b[0]} - {b[1]}" for b in BookService.get_all_books()]
    tk.OptionMenu(window, book_var, *book_options).pack()

    # --- Member Dropdown ---
    tk.Label(window, text="Select Member").pack()
    member_var = tk.StringVar(window)
    member_options = [f"{m[0]} - {m[1]}" for m in MemberService.get_all_members()]
    tk.OptionMenu(window, member_var, *member_options).pack()

    # --- Submit Button ---
    tk.Button(window, text="Issue Book", command=submit_issue).pack(pady=10)
    window.mainloop()


def launch_issue_book():
    issue_book_gui()


class IssueBookGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def issue_book_gui(*args, **kwargs):
        """Wrapper to module-level function issue_book_gui"""
        return issue_book_gui(*args, **kwargs)

    @staticmethod
    def launch_issue_book(*args, **kwargs):
        """Wrapper to module-level function launch_issue_book"""
        return launch_issue_book(*args, **kwargs)
