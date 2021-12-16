from flask import Blueprint, render_template, request


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


@Views.route('/handling-data')
def handling_data():
    return render_template('testing.html')

###############################
### This part is important to understand
### the post system in flask. Even when
### we delete the testing.html page, this
### must stay!!!
###############################
"""
@Views.route('/handling_data', methods=['GET'])
def render_handling_data() -> str:
    return render_template('testing.html')


@Views.route('/handling_data', methods=['POST'])
def handling_data() -> str:
    projectPath = request.form['Username']
    return render_template('testing.html', inpt=projectPath)
"""
###############################