from flask import Blueprint, render_template, request
from .python.priv_types import Dict

Examples = Blueprint('Examples', __name__)

###############################
### Used to show the block and the extends for the html parts.
### They are in the templates/examples/block-example.html
###############################

@Examples.route('/block-example')
def block_example() -> str:
	return render_template('examples/block-example.html')

###############################


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


@Examples.route('/search-line-example')
def search_line_example() -> str:
	content: dict = request.args
	print(content.get('username', None))
	return render_template('examples/search-line-example.html', content=str(content))

