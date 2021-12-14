from flask import Blueprint, render_template


Views = Blueprint('views', __name__)


@Views.route('/')
def home() -> str:
    return render_template("base.html", title="Homepage", inAuth=False)


@Views.route('/user-page')
def user_page(user_name:str=None) -> str:
    if user_name:
        return render_template("user_home_page.html", user_name=user_name)

    error_content: str = """
As a non-user, you are trying to accese some user content.
Please return to your designated area.
    """

    return render_template("error.html", error_code="505", error_content=error_content)
