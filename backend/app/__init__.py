from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_mail import Mail
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()

def create_app():
    app = Flask(__name__)

    # Cargar variables de entorno
    load_dotenv()

    # Configuración de la aplicación
    app.config.update(
        SQLALCHEMY_DATABASE_URI='sqlite:///umbook.db',
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY='super-secret',
        MAIL_SERVER=os.getenv('MAIL_SERVER'),
        MAIL_PORT=int(os.getenv('MAIL_PORT')),
        MAIL_USE_TLS=os.getenv('MAIL_USE_TLS') == 'True',
        MAIL_USERNAME=os.getenv('MAIL_USERNAME'),
        MAIL_PASSWORD=os.getenv('MAIL_PASSWORD'),
        MAIL_DEFAULT_SENDER=os.getenv('MAIL_USERNAME')
    )

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)  # Asegúrate de que esto esté presente y correctamente ejecutado

    # Configurar CORS
    CORS(app, resources={r"/*": {"origins": "http://localhost:4200"}})

    # Importar modelos para migraciones
    from .persistence import models

    # Registrar blueprints
    from .controllers.auth_controller import auth_bp
    from .controllers.invite_controller import invite_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(invite_bp, url_prefix='/invite')

    return app