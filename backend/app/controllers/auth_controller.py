from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, validate, ValidationError
from flask_jwt_extended import create_access_token
from ..services.auth_service import AuthService

auth_bp = Blueprint('auth', __name__)

class RegisterSchema(Schema):
    name = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Email(required=True)
    password = fields.Str(required=True, validate=validate.Length(min=8))

class LoginSchema(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)

@auth_bp.route('/register', methods=['POST'])
def register():
    schema = RegisterSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    user, err_msg = AuthService.register_user(data['name'], data['email'], data['password'])
    if err_msg:
        return jsonify({'msg': err_msg}), 400

    return jsonify({'id': user.id, 'email': user.email}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    schema = LoginSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    user = AuthService.authenticate(data['email'], data['password'])
    if not user:
        return jsonify({'msg': 'Bad credentials'}), 401

    access_token = create_access_token(identity=str(user.id))
    return jsonify({'access_token': access_token, 'user': {'id': user.id, 'email': user.email}}), 200
