import tkinter as tk
from tkinter import messagebox
from business.user_service import UserService
from gui.register_user import launch_register_window

def launch_login(app_callback):
    def login_action():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        try:
            user = UserService.login_user(username, password)
            if user:
                user_id, role = user
                messagebox.showinfo("Login Successful", f"Welcome {username} ({role})!")
                root.destroy()
                app_callback(user_id, role)
            else:
                messagebox.showerror("Login Failed", "Invalid username or password.")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    # --- Window setup ---
    root = tk.Tk()
    root.title("Library Login")
    root.state("zoomed")
    root.configure(bg="#f0f4f7")
    root.resizable(True, True)

    # --- Center Frame ---
    frame = tk.Frame(root, bg="white", bd=2, relief="ridge")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=350)

    tk.Label(frame, text="📚 Library Management System", font=("Segoe UI", 16, "bold"), bg="white", fg="#1e88e5").pack(pady=20)
    tk.Label(frame, text="User Login", font=("Segoe UI", 12, "bold"), bg="white", fg="#263238").pack(pady=5)

    tk.Label(frame, text="Username", font=("Segoe UI", 10), bg="white", fg="#263238").pack(pady=5)
    username_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bd=1, relief="solid")
    username_entry.pack(pady=5, ipady=4)

    tk.Label(frame, text="Password", font=("Segoe UI", 10), bg="white", fg="#263238").pack(pady=5)
    password_entry = tk.Entry(frame, show="*", font=("Segoe UI", 10), width=30, bd=1, relief="solid")
    password_entry.pack(pady=5, ipady=4)

    # --- Buttons ---
    def on_enter(e): e.widget.config(bg="#1565c0")
    def on_leave(e): e.widget.config(bg="#1e88e5")

    login_btn = tk.Button(frame, text="Login", font=("Segoe UI", 11, "bold"), bg="#1e88e5", fg="white", width=25, command=login_action, bd=0, relief="flat")
    login_btn.pack(pady=15, ipady=5)
    login_btn.bind("<Enter>", on_enter)
    login_btn.bind("<Leave>", on_leave)

    register_btn = tk.Button(frame, text="Register", font=("Segoe UI", 10, "bold"), bg="white", fg="#1e88e5", bd=0, command=launch_register_window)
    register_btn.pack()

    root.mainloop()


class LoginGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_login(*args, **kwargs):
        """Wrapper to module-level function launch_login"""
        return launch_login(*args, **kwargs)
