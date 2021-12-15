from flask import Blueprint, render_template, request

Auth = Blueprint('Auth', __name__)

@Auth.route('/login', methods=['GET'])
def render_login() -> str:
    return render_template('user_input_tmp.html', type="Login")


@Auth.route('/login', methods=['POST'])
def login():
    pass

@Auth.route('/logout')
def logout() -> str:
    content: str = """
Could not find the page you were looking for.
Please make sure your link is valid, and it was typed correctly.
    """
    return render_template('error.html', error_code="404", error_content=content)


@Auth.route('/sign-up', methods=['GET'])
def render_sign_up() -> str:
    return render_template('user_input_tmp.html', type="Sign Up")


@Auth.route('/sign-up', methods=['POST'])
def sign_up() -> str:
    pass

