from data.transaction_dao import TransactionDaoDAO
from data.book_dao import BookDaoDAO

class TransactionService:
    """Business logic for issuing, returning, and tracking book transactions."""

    @staticmethod
    def issue_book(member_id, book_id, issue_date, due_date):
        books = BookDaoDAO.get_all_books()
        book = next((b for b in books if b[0] == book_id), None)

        if not book:
            return False

        available = int(book[5])
        if available <= 0:
            return False

        success = TransactionDaoDAO.issue_book(member_id, book_id, issue_date, due_date)
        if success:
            new_available = available - 1
            BookDaoDAO.update_book(book_id, book[1], book[2], book[3], book[4], new_available)
        return success

    @staticmethod
    def return_book(transaction_id, return_date, fine):
        """
        Handles the return of a book:
        - Updates transaction record
        - Increases book availability
        - Returns success/failure
        """
        return TransactionDaoDAO.return_book(transaction_id, return_date, fine)

    @staticmethod
    def get_issued_books():
        return TransactionDaoDAO.get_issued_books()

    @staticmethod
    def get_overdue_books():
        return TransactionDaoDAO.get_overdue_books()

    @staticmethod
    def get_all_transactions():
        return TransactionDaoDAO.get_all_transactions()
