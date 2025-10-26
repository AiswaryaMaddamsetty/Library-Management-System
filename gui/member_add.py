import tkinter as tk
from tkinter import messagebox
import datetime
from business.member_service import MemberService   

def launch_member_form(mode="add", member_data=None, refresh_callback=None):
    def save_member():
        name = name_entry.get().strip()
        email = email_entry.get().strip()
        phone = phone_entry.get().strip()

        if not name or not email or not phone:
            messagebox.showerror("Invalid Input", "Please fill all fields.")
            return

        join_date = datetime.date.today().isoformat()

        try:
            if mode == "add":
                # ✅ Call business layer instead of DAO
                MemberService.add_member(name, email, phone, join_date)
                messagebox.showinfo("Success", "Member added successfully.")
            else:
                member_id = member_data[0]
                # ✅ Call business layer for update
                MemberService.update_member(member_id, name, email, phone, join_date)
                messagebox.showinfo("Success", "Member updated successfully.")

            form.destroy()
            if refresh_callback:
                refresh_callback()

        except ValueError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Database Error", f"An error occurred: {str(e)}")

    # --- GUI Form ---
    form = tk.Toplevel()
    form.title("Add Member" if mode == "add" else "Update Member")
    form.geometry("350x250")

    tk.Label(form, text="Name").pack(pady=5)
    name_entry = tk.Entry(form)
    name_entry.pack(pady=5)

    tk.Label(form, text="Email").pack(pady=5)
    email_entry = tk.Entry(form)
    email_entry.pack(pady=5)

    tk.Label(form, text="Phone").pack(pady=5)
    phone_entry = tk.Entry(form)
    phone_entry.pack(pady=5)

    if mode == "update" and member_data:
        name_entry.insert(0, member_data[1])
        email_entry.insert(0, member_data[2])
        phone_entry.insert(0, member_data[3])

    tk.Button(form, text="Save", command=save_member).pack(pady=20)


class MemberAddGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_member_form(*args, **kwargs):
        """Wrapper to module-level function launch_member_form"""
        return launch_member_form(*args, **kwargs)
