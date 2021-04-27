from flask import render_template, flash, redirect, request, url_for
from application import app, db
from application.forms import LoginForm, SignupForm
from application.models import Item
from application.models import User
from datetime import datetime
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html')

@app.route('/list', methods=['GET'])
def list():
    items = []
    if current_user.is_authenticated: 
        items = current_user.items
    return render_template('list.html', items=items)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = SignupForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        user = User(form.first_name.data, form.last_name.data, form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        # Before redirect, LOG IN the user after creation above.
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('signup'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Login requested for user {}. remember_me={}'.format(form.username.data, form.remember_me.data))
            return redirect('/signup')
        login_user(user, remember=form.remember_me.data)
    return render_template('login.html', title='Sign In', form=form)
  # Retrieve the user from database, check credentials...
        # check username and password...
        # user = User.query.filter_by()....

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add-item', methods=['POST'])
def add_item():
    if current_user.is_authenticated:
        submitted_time = request.form.get('date') + ' ' + request.form.get('time')
        dt = datetime.strptime(submitted_time, '%Y-%m-%d %H:%M')
        item = Item(time=dt, event=request.form.get("event"), description=request.form.get("description"), user=current_user.id)
        db.session.add(item)
        db.session.commit()
    return redirect('/list')

@app.route('/delete-item/<item_id>', methods=['GET', 'DELETE']) # UPDATE TO DELETE
def delete_item(item_id):
    item = Item.query.filter_by(id=item_id).delete()
    db.session.commit()
    return redirect('/list')


# CRUD operations 
# http type of requests and most common return codes

# git common commands
# git status
# git add
# git commit

