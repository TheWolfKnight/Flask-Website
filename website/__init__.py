from flask import Flask
from sys import exit

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ALKJHSFEGONEPNoingboajnfd65487'

    from .views import Views
    from .auth import Auth

    app.register_blueprint(Views, url_prefix="/")
    app.register_blueprint(Auth, url_prefix='/auth')

    return app


if __name__ == "__main__":
    exit()
