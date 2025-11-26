import os
from dotenv import load_dotenv
from flask_login import LoginManager
from database import init_database
from models.usuario import Usuario


def config_app(app):
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')
    if SECRET_KEY is None or SECRET_KEY == '':
        raise RuntimeError('SECRET_KEY não foi definida')

    app.secret_key = SECRET_KEY

    login_manager = LoginManager(app)
    login_manager.login_view = '/login' # type: ignore

    init_database()

    @login_manager.user_loader
    def load_user(user_id: int):
        return Usuario.get(user_id)
