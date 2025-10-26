import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from business.transaction_service import TransactionService   

def launch_return_book():
    window = tk.Toplevel()
    window.title("Return Book")
    window.geometry("700x400")

    # --- Listbox for active transactions ---
    trans_listbox = tk.Listbox(window, width=100)
    trans_listbox.pack(pady=10)

    # --- Fetch issued (not returned) transactions via business layer ---
    transactions = TransactionService.get_issued_books()
    for trans in transactions:
        trans_listbox.insert(
            tk.END, f"{trans[0]} - {trans[1]} - {trans[2]} - Issued: {trans[3]} - Due: {trans[4]}"
        )

    # --- Return Book Handler ---
    def return_selected():
        selected = trans_listbox.curselection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a transaction to return.")
            return

        selected_index = selected[0]
        transaction_id = transactions[selected_index][0]
        return_date = datetime.now().strftime("%Y-%m-%d")

        # --- Fine Calculation ---
        due_date = datetime.strptime(transactions[selected_index][4], "%Y-%m-%d")
        days_late = (datetime.now() - due_date).days
        fine = max(0, days_late * 5)

        # ✅ Call business layer for return operation
        success = TransactionService.return_book(transaction_id, return_date, fine)
        if success:
            messagebox.showinfo("Success", f"Book returned successfully.\nFine: ₹{fine}")
            trans_listbox.delete(selected_index)
        else:
            messagebox.showerror("Error", "Failed to return book.")

    # --- Button ---
    tk.Button(window, text="Return Book", command=return_selected).pack(pady=10)


class ReturnBookGUI:
    """Auto-generated wrapper class exposing module functions as static methods."""
    @staticmethod
    def launch_return_book(*args, **kwargs):
        """Wrapper to module-level function launch_return_book"""
        return launch_return_book(*args, **kwargs)
