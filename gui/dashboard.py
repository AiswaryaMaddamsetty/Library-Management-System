import tkinter as tk
from tkinter import messagebox
from gui.book_search import launch_book_search
from gui.member_search import launch_member_search
from gui.issue_book import launch_issue_book
from gui.return_book import launch_return_book
from gui.register_user import launch_register_window
from gui.view_reports import launch_view_reports

def launch_dashboard(user_id, role):
    def logout_action():
        dashboard.destroy()
        from gui.login import launch_login
        launch_login(launch_dashboard)

    def not_implemented():
        messagebox.showinfo("Coming Soon", "This feature is not implemented yet.")

    # --- Window Setup ---
    dashboard = tk.Tk()
    dashboard.title("Library Management System - Dashboard")
    dashboard.state("zoomed")
    dashboard.configure(bg="#f0f4f7")
    dashboard.resizable(True, True)

    # --- Header ---
    header = tk.Frame(dashboard, bg="#1e88e5", height=80)
    header.pack(fill="x")
    tk.Label(header, text="📚 Library Management System", font=("Segoe UI", 18, "bold"), bg="#1e88e5", fg="white").pack(pady=20)

    # --- Welcome Info ---
    tk.Label(dashboard, text=f"Welcome to the LMS!", font=("Segoe UI", 14, "bold"), bg="#f0f4f7", fg="#263238").pack(pady=(30, 5))
    tk.Label(dashboard, text=f"Logged in as: {role.capitalize()}", font=("Segoe UI", 11), bg="#f0f4f7", fg="#555555").pack(pady=(0, 20))

    # --- Button Styling Helpers ---
    def create_button(text, command):
        btn = tk.Button(
            dashboard, text=text, width=30, height=2, bg="#1e88e5", fg="white",
            font=("Segoe UI", 11, "bold"), bd=0, relief="flat", command=command
        )
        btn.pack(pady=8)
        btn.bind("<Enter>", lambda e: btn.config(bg="#1565c0"))
        btn.bind("<Leave>", lambda e: btn.config(bg="#1e88e5"))
        return btn

    # --- Buttons Section ---
    create_button("📚 Add / Search Books", launch_book_search)
    create_button("👥 Register / Search Members", launch_member_search)
    create_button("🔄 Issue Book", launch_issue_book)
    create_button("✅ Return Book", launch_return_book)
    create_button("📊 View Reports / Overdue", launch_view_reports)

    # Librarian Only
    if role == "librarian":
        create_button("🧑‍💼 Register New User", launch_register_window)

    # --- Logout Button ---
    tk.Button(
        dashboard, text="🚪 Logout", width=30, height=2,
        bg="#ef5350", fg="white", font=("Segoe UI", 11, "bold"),
        bd=0, relief="flat", command=logout_action
    ).pack(pady=30)

    dashboard.mainloop()


class DashboardGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_dashboard(*args, **kwargs):
        """Wrapper to module-level function launch_dashboard"""
        return launch_dashboard(*args, **kwargs)
