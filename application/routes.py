from flask import render_template
from application import app

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    return render_template('list.html')

@app.route('/add-item', methods=['POST'])
def add_item():
	return '<h1>item added succesfully</h1>'

@app.route('/delete-item/<id>', methods=['DELETE'])
def delete_item(id):
	pass


# CRUD operations 
# http type of requests and most common return codes

# git common commands
# git status
# git add
# git commit

