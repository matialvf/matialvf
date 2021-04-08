from flask import render_template
from application import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    return render_template('list.html')
