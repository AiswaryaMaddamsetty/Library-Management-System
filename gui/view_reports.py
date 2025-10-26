import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import csv
from data.transaction_dao import get_overdue_books
from datetime import datetime
FINE_PER_DAY = 5  # Fine amount per overdue day

def calculate_fine(due_date):
    try:
        due = datetime.strptime(due_date, "%Y-%m-%d")
        today = datetime.today()
        days_overdue = (today - due).days
        return FINE_PER_DAY * days_overdue if days_overdue > 0 else 0
    except:
        return 0

def generate_csv():
    overdue_books = get_overdue_books()
    if not overdue_books:
        messagebox.showinfo("No Overdue Books", "No overdue books to export.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[("CSV files", "*.csv")],
        title="Save Overdue Report As"
    )
    if not file_path:
        return  # User canceled

    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            fieldnames = ["Transaction ID", "Member Name", "Book Title", "Issue Date", "Due Date", "Fine to be Paid"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for book in overdue_books:
                fine = calculate_fine(book[4])
                writer.writerow({
                    "Transaction ID": book[0],
                    "Member Name": book[1],
                    "Book Title": book[2],
                    "Issue Date": book[3],
                    "Due Date": book[4],
                    "Fine to be Paid": f"{fine}"
                })

        messagebox.showinfo("CSV Export", f"Overdue books exported successfully to this path:\n{file_path}")

    except Exception as e:
        messagebox.showerror("Export Failed", f"An error occurred:\n{str(e)}")


def launch_view_reports():
    window = tk.Toplevel()
    window.title("View Overdue Books")
    window.geometry("700x400")
    tk.Label(window, text="Overdue Report", font=("Helvetica", 16, "bold")).pack(pady=10)

    # Frame to hold the Treeview and Scrollbar
    tree_frame = tk.Frame(window)
    tree_frame.pack(pady=20, fill="both", expand=True)

    # Scrollbar
    tree_scrollbar = ttk.Scrollbar(tree_frame, orient="vertical")
    tree_scrollbar.pack(side="right", fill="y")

    # Treeview for overdue books
    columns = ("Transaction ID", "Member Name", "Book Title", "Issue Date", "Due Date", "Fine to be Paid")
    tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scrollbar.set)
    
    # Configure scrollbar to Treeview
    tree_scrollbar.config(command=tree.yview)

    # Define column headings
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor="center",width=120)  # optional: center align

    # Populate the treeview
    overdue_books = get_overdue_books()
    for book in overdue_books:
        fine = calculate_fine(book[4])
        tree.insert("", tk.END, values=book + (f"{fine}",))
    
    tree.pack(side="left", fill="both", expand=True)

    # Button to generate CSV
    tk.Button(window, text="Export to CSV", command=generate_csv).pack(pady=10)



class ViewReportsGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def calculate_fine(*args, **kwargs):
        """Wrapper to module-level function calculate_fine"""
        return calculate_fine(*args, **kwargs)

    @staticmethod
    def generate_csv(*args, **kwargs):
        """Wrapper to module-level function generate_csv"""
        return generate_csv(*args, **kwargs)

    @staticmethod
    def launch_view_reports(*args, **kwargs):
        """Wrapper to module-level function launch_view_reports"""
        return launch_view_reports(*args, **kwargs)
