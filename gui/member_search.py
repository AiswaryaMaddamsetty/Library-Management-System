import tkinter as tk
from tkinter import messagebox
from business.member_service import MemberService      
from gui.member_add import launch_member_form

def launch_member_search():
    def refresh_table():
        # Clear previous data
        for row in member_list.get_children():
            member_list.delete(row)

        keyword = search_entry.get().strip()
        members = MemberService.search_members(keyword) if keyword else MemberService.get_all_members()  # ✅ Business layer
        for mem in members:
            member_list.insert("", "end", values=mem)

    def delete_selected():
        selected = member_list.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Select a member to delete.")
            return

        mem = member_list.item(selected[0])["values"]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete member '{mem[1]}'?")
        if confirm:
            try:
                MemberService.delete_member(mem[0])   # ✅ Business layer
                refresh_table()
                messagebox.showinfo("Deleted", f"Member '{mem[1]}' deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to delete member: {str(e)}")

    def update_selected():
        selected = member_list.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Select a member to update.")
            return

        mem = member_list.item(selected[0])["values"]
        launch_member_form("update", mem, refresh_table)

    # --- GUI Window ---
    window = tk.Toplevel()
    window.title("Search / Manage Members")
    window.geometry("700x400")

    # --- Search Bar ---
    search_frame = tk.Frame(window)
    search_frame.pack(pady=10)
    tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Search", command=refresh_table).pack(side=tk.LEFT)
    tk.Button(search_frame, text="Add New Member", 
              command=lambda: launch_member_form("add", None, refresh_table)).pack(side=tk.LEFT, padx=10)

    # --- Member List Table ---
    import tkinter.ttk as ttk
    member_list = ttk.Treeview(window, columns=("ID", "Name", "Email", "Phone"), show="headings")
    for col in member_list["columns"]:
        member_list.heading(col, text=col)
        member_list.column(col, width=150)
    member_list.pack(pady=10, fill=tk.BOTH, expand=True)

    # --- Action Buttons ---
    action_frame = tk.Frame(window)
    action_frame.pack(pady=5)
    tk.Button(action_frame, text="Update Selected", command=update_selected).pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Delete Selected", command=delete_selected).pack(side=tk.LEFT, padx=10)

    # Load initial data
    refresh_table()


class MemberSearchGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_member_search(*args, **kwargs):
        """Wrapper to module-level function launch_member_search"""
        return launch_member_search(*args, **kwargs)
