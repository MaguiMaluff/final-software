from werkzeug.security import generate_password_hash, check_password_hash
from ..persistence.daos.user_dao import UserDAO

class AuthService:
    @staticmethod
    def register_user(name, email, password):
        existing = UserDAO.get_by_email(email)
        if existing:
            return None, 'Email already registered'
        pw_hash = generate_password_hash(password)
        user = UserDAO.create(name=name, email=email, password_hash=pw_hash)
        return user, None

    @staticmethod
    def authenticate(email, password):
        user = UserDAO.get_by_email(email)
        if not user or not check_password_hash(user.password_hash, password):
            return None
        return user
