from flask import Blueprint, render_template

Auth = Blueprint('Auth', __name__)

@Auth.route('/login')
def login():
    return render_template('user_input_tmp.html', type="Login")


@Auth.route('/logout')
def logout():
    content: str = """
Could not find the page you were looking for.
Please make sure your link is valid, and it was typed correctly.
    """
    return render_template('error.html', error_code="404", error_content=content)


@Auth.route('/sign-up')
def sign_up():
    return render_template('user_input_tmp.html', type="Sign Up")
