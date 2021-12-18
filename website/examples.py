from flask import Blueprint, render_template


Examples = Blueprint('Examples', __name__)


@Examples.route('/block-example')
def block_example() -> str:
    return render_template('block-example.html')


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
