from data.user_dao import UserDaoDAO

class UserService:
    """Business logic for managing user registration and authentication."""

    @staticmethod
    def register_user(username, password, role):
        """
        Handles user registration.
        Includes validation and delegates database insertion to the DAO.
        """
        if not username or not password or not role:
            raise ValueError("All fields (username, password, role) are required.")
        if len(password) < 4:
            raise ValueError("Password must be at least 4 characters long.")
        UserDaoDAO.add_user(username, password, role)

    @staticmethod
    def login_user(username, password):
        """
        Authenticates a user by verifying their credentials.
        Returns (user_id, role) if successful, or None if invalid.
        """
        if not username or not password:
            raise ValueError("Username and password cannot be empty.")
        result = UserDaoDAO.authenticate_user(username, password)
        return result  # (user_id, role) or None

    @staticmethod
    def get_user_by_id(user_id):
        """Fetches user details by ID."""
        if not user_id:
            raise ValueError("User ID is required.")
        return UserDaoDAO.get_user_by_id(user_id)
