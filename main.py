from gui.login import launch_login
from gui.dashboard import launch_dashboard
from data.db_connector import create_tables
create_tables()
# This function will be triggered after successful login
def launch_main_app(user_id, role):
    # For now, just show a message — later you’ll load full GUI
    import tkinter as tk
    from tkinter import messagebox

    app = tk.Tk()
    app.title("Library Management System")
    app.geometry("400x200")
    messagebox.showinfo("Main App", f"Main Dashboard Placeholder\nLogged in as User ID: {user_id} | Role: {role}")
    app.mainloop()

if __name__ == "__main__":
    launch_login(launch_dashboard)
