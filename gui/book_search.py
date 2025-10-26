import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from business.book_service import BookService       
from gui.book_add import launch_book_form           

def launch_book_search():
    def refresh_table():
        for row in book_list.get_children():
            book_list.delete(row)

        keyword = search_entry.get().strip()
        books = BookService.search_books(keyword) if keyword else BookService.get_all_books()  # ✅ through business layer

        for book in books:
            book_list.insert("", "end", values=book)

    def delete_selected():
        selected = book_list.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Select a book to delete.")
            return
        book = book_list.item(selected[0])["values"]
        confirm = messagebox.askyesno("Confirm Delete", f"Delete book '{book[1]}'?")
        if confirm:
            BookService.delete_book(book[0])       # ✅ through business layer
            refresh_table()

    def update_selected():
        selected = book_list.selection()
        if not selected:
            messagebox.showwarning("No Selection", "Select a book to update.")
            return
        book = book_list.item(selected[0])["values"]
        launch_book_form("update", book, refresh_table)  # ✅ GUI function remains same

    window = tk.Toplevel()
    window.title("Search / Manage Books")
    window.geometry("700x400")

    # --- Search bar ---
    search_frame = tk.Frame(window)
    search_frame.pack(pady=10)
    tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=5)
    tk.Button(search_frame, text="Search", command=refresh_table).pack(side=tk.LEFT)
    tk.Button(search_frame, text="Add New Book", command=lambda: launch_book_form("add", None, refresh_table)).pack(side=tk.LEFT, padx=10)

    # --- Book table ---
    book_list = ttk.Treeview(window, columns=("ID", "Title", "Author", "ISBN", "Total Copies", "Available"), show="headings")
    for col in book_list["columns"]:
        book_list.heading(col, text=col)
        book_list.column(col, width=120)
    book_list.pack(pady=10, fill=tk.BOTH, expand=True)

    # --- Action buttons ---
    action_frame = tk.Frame(window)
    action_frame.pack(pady=5)
    tk.Button(action_frame, text="Update Selected", command=update_selected).pack(side=tk.LEFT, padx=10)
    tk.Button(action_frame, text="Delete Selected", command=delete_selected).pack(side=tk.LEFT, padx=10)

    refresh_table()   # ✅ populate table initially


class BookSearchGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_book_search(*args, **kwargs):
        """Wrapper to module-level function launch_book_search"""
        return launch_book_search(*args, **kwargs)
