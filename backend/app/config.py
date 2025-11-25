from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///umbook.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'super-secret'

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = int(os.getenv('MAIL_PORT'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')  # Aquí se usa tu correo
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')  # Aquí se usa tu clave
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER')  # Configura el remitente predeterminado