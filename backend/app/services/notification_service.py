import threading
from flask_mail import Message
from flask import current_app
from .. import mail

class NotificationService:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def send_invitation(self, recipient_email, inviter_name):
        subject = "You're Invited to UMBook!"
        body = f"Hi, you've been invited to join UMBook by {inviter_name}."
        with current_app.app_context():  # Asegúrate de estar en el contexto de la aplicación
            msg = Message(
                subject=subject,
                recipients=[recipient_email],
                body=body,
                sender=current_app.config['MAIL_DEFAULT_SENDER']  # Usa current_app para acceder a la configuración
            )
            try:
                mail.send(msg)
                print(f"[NotificationService] Email sent to {recipient_email}")
            except Exception as e:
                print(f"[NotificationService] Failed to send email: {e}")
                raise
