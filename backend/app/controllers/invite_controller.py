from flask import Blueprint, request, jsonify
from marshmallow import Schema, fields, ValidationError
from ..utils.decorators import token_required
from ..services.notification_service import NotificationService

invite_bp = Blueprint('invite', __name__)
notif_service = NotificationService()

class InviteSchema(Schema):
    email = fields.Email(required=True)

@invite_bp.route('', methods=['POST'])
@token_required
def invite(current_user):
    schema = InviteSchema()
    try:
        data = schema.load(request.get_json())
    except ValidationError as err:
        return jsonify(err.messages), 400

    try:
        notif_service.send_invitation(recipient_email=data['email'], inviter_name=current_user.name)
        return jsonify({'msg': 'Invitation queued'}), 202
    except Exception as e:
        print(e)
        return jsonify({'msg': 'Failed to send invitation', 'error': str(e)}), 500
