from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from ..persistence.daos.user_dao import UserDAO

def token_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            identity = int(get_jwt_identity())
        except Exception as e:
            return jsonify({'msg': 'Missing or invalid token', 'error': str(e)}), 401

        user = UserDAO.get_by_id(identity)
        if not user:
            return jsonify({'msg': 'User not found'}), 401

        kwargs['current_user'] = user
        return fn(*args, **kwargs)
    return wrapper
