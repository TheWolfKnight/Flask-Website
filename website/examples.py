from flask import Blueprint, render_template, request


Examples = Blueprint('Examples', __name__)


@Examples.route('/block-example')
def block_example() -> str:
    return render_template('examples/block-example.html')


###############################
### This part is important to understand
### the post system in flask. Even when
### we delete the testing.html page, this
### must stay!!!
###############################

@Examples.route('/form-example', methods=['GET'])
def render_form_example() -> str:
    return render_template('examples/form-example.html', inpt="")


@Examples.route('/form-example', methods=['POST'])
def form_example() -> str:
    projectPath: str = request.form['Username']
    print(projectPath)
    return render_template('examples/form-example.html', inpt=projectPath)

###############################
