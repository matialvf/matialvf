from flask import render_template, flash, redirect, request
from application import app, db
from application.forms import LoginForm, SignupForm
from application.models import Item
from datetime import datetime

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    items = Item.query.all()
    return render_template('list.html', items=items)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.username.data, form.email.data, form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}. remember_me={}'.format(form.username.data, form.remember_me.data))
		return redirect('/index')
	return render_template('login.html', title='Sign In', form=form)

@app.route('/add-item', methods=['POST'])
def add_item():
    submitted_time = request.form.get('date') + ' ' + request.form.get('time')
    dt = datetime.strptime(submitted_time, '%Y-%m-%d %H:%M')
    item = Item(time=dt, event=request.form.get("event"), description=request.form.get("description"))
    db.session.add(item)
    db.session.commit()

    return redirect('/list')

@app.route('/delete-item/<id>', methods=['DELETE'])
def delete_item(id):
	pass



# CRUD operations 
# http type of requests and most common return codes

# git common commands
# git status
# git add
# git commit

