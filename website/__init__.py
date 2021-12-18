from flask import Flask
from sys import exit

from website.examples import Examples

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'ALKJHSFEGONEPNoingboajnfd65487'

    from .views import Views
    from .auth import Auth
    from .examples import Examples

    app.register_blueprint(Views, url_prefix="/")
    app.register_blueprint(Auth, url_prefix='/auth')
    app.register_blueprint(Examples, url_prefix='/examples')

    return app


if __name__ == "__main__":
    exit()
