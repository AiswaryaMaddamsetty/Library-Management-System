import tkinter as tk
from tkinter import messagebox
from business.book_service import BookService   

def launch_book_form(mode="add", book_data=None, refresh_callback=None):
    def save_action():
        title = title_entry.get().strip()
        author = author_entry.get().strip()
        isbn = isbn_entry.get().strip()
        total = total_entry.get().strip()

        if not title or not author or not isbn or not total.isdigit():
            messagebox.showerror("Invalid Input", "Please fill all fields correctly.")
            return

        total_copies = int(total)

        if mode == "add":
            # ✅ Call through business layer
            BookService.add_new_book(title, author, isbn, total_copies)
            messagebox.showinfo("Success", "Book added successfully.")
        else:
            book_id = book_data[0]
            available = int(book_data[5]) + (total_copies - int(book_data[4]))  # adjust available
            # ✅ Call through business layer
            BookService.update_existing_book(book_id, title, author, isbn, total_copies, available)
            messagebox.showinfo("Success", "Book updated successfully.")

        form.destroy()
        if refresh_callback:
            refresh_callback()

    form = tk.Toplevel()
    form.title("Add Book" if mode == "add" else "Update Book")
    form.geometry("350x300")

    tk.Label(form, text="Title").pack(pady=5)
    title_entry = tk.Entry(form)
    title_entry.pack(pady=5)

    tk.Label(form, text="Author").pack(pady=5)
    author_entry = tk.Entry(form)
    author_entry.pack(pady=5)

    tk.Label(form, text="ISBN").pack(pady=5)
    isbn_entry = tk.Entry(form)
    isbn_entry.pack(pady=5)

    tk.Label(form, text="Total Copies").pack(pady=5)
    total_entry = tk.Entry(form)
    total_entry.pack(pady=5)

    if mode == "update" and book_data:
        title_entry.insert(0, book_data[1])
        author_entry.insert(0, book_data[2])
        isbn_entry.insert(0, book_data[3])
        total_entry.insert(0, str(book_data[4]))

    tk.Button(form, text="Save", command=save_action).pack(pady=20)


class BookAddGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_book_form(*args, **kwargs):
        """Wrapper to module-level function launch_book_form"""
        return launch_book_form(*args, **kwargs)
