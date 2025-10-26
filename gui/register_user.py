import tkinter as tk
from tkinter import messagebox
from business.user_service import UserService  

def launch_register_window():
    def register_action():
        username = username_entry.get().strip()
        password = password_entry.get().strip()
        role = role_var.get()

        try:
            UserService.register_user(username, password, role)
            messagebox.showinfo("Success", f"User '{username}' registered as {role}.")
            register_window.destroy()
        except ValueError as e:
            messagebox.showwarning("Validation Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")

    # --- Main window setup ---
    register_window = tk.Toplevel()
    register_window.title("Register New User")
    register_window.state("zoomed")               # Start maximized
    register_window.configure(bg="#f0f4f7")
    register_window.resizable(True, True)

    # --- Center form frame ---
    frame = tk.Frame(register_window, bg="white", bd=2, relief="ridge")
    frame.place(relx=0.5, rely=0.5, anchor="center", width=400, height=400)

    tk.Label(frame, text="📚 Library Management System", font=("Segoe UI", 16, "bold"), bg="white", fg="#1e88e5").pack(pady=20)
    tk.Label(frame, text="User Registration", font=("Segoe UI", 12, "bold"), bg="white", fg="#263238").pack(pady=5)

    # --- Username field ---
    tk.Label(frame, text="Username", font=("Segoe UI", 10), bg="white", fg="#263238").pack(pady=5)
    username_entry = tk.Entry(frame, font=("Segoe UI", 10), width=30, bd=1, relief="solid")
    username_entry.pack(pady=5, ipady=4)

    # --- Password field ---
    tk.Label(frame, text="Password", font=("Segoe UI", 10), bg="white", fg="#263238").pack(pady=5)
    password_entry = tk.Entry(frame, show="*", font=("Segoe UI", 10), width=30, bd=1, relief="solid")
    password_entry.pack(pady=5, ipady=4)

    # --- Role dropdown ---
    tk.Label(frame, text="Role", font=("Segoe UI", 10), bg="white", fg="#263238").pack(pady=5)
    role_var = tk.StringVar()
    role_var.set("staff")  # default role
    role_menu = tk.OptionMenu(frame, role_var, "librarian", "staff")
    role_menu.config(font=("Segoe UI", 10), bg="white", fg="#1e88e5", width=20)
    role_menu.pack(pady=5)

    # --- Button styling helpers ---
    def on_enter(e): e.widget.config(bg="#1565c0")
    def on_leave(e): e.widget.config(bg="#1e88e5")

    # --- Register button ---
    register_btn = tk.Button(frame, text="Register", font=("Segoe UI", 11, "bold"), bg="#1e88e5", fg="white",
                             width=25, bd=0, relief="flat", command=register_action)
    register_btn.pack(pady=20, ipady=5)
    register_btn.bind("<Enter>", on_enter)
    register_btn.bind("<Leave>", on_leave)

    # --- Footer note ---
    tk.Label(frame, text="Already have an account? Please login.", font=("Segoe UI", 9), bg="white", fg="#777777").pack(pady=5)

    register_window.mainloop()


class RegisterUserGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_register_window(*args, **kwargs):
        """Wrapper to module-level function launch_register_window"""
        return launch_register_window(*args, **kwargs)
