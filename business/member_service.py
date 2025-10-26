from data.member_dao import MemberDaoDAO

class MemberService:
    """Business logic for managing members."""

    @staticmethod
    def add_member(name, email, phone, join_date):
        if not name or not email or not phone:
            raise ValueError("All member details are required.")
        if len(phone) < 10 or not phone.isdigit():
            raise ValueError("Phone number must contain at least 10 digits.")
        MemberDaoDAO.add_member(name, email, phone, join_date)

    @staticmethod
    def get_all_members():
        return MemberDaoDAO.get_all_members()

    @staticmethod
    def search_members(keyword):
        return MemberDaoDAO.search_members(keyword)

    @staticmethod
    def update_member(member_id, name, email, phone, join_date):
        if not name or not email or not phone:
            raise ValueError("All member details are required.")
        if len(phone) < 10 or not phone.isdigit():
            raise ValueError("Phone number must contain at least 10 digits.")
        MemberDaoDAO.update_member(member_id, name, email, phone, join_date)

    @staticmethod
    def delete_member(member_id):
        if not member_id:
            raise ValueError("Member ID is required for deletion.")
        MemberDaoDAO.delete_member(member_id)
