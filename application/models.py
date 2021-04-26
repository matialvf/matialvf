from datetime import datetime
from application import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from application import login

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.DateTime, default=datetime.utcnow)
	event = db.Column(db.String(50))
	description = db.Column(db.String(255))
	user = db.Column(db.Integer, db.ForeignKey('user.id'))
	# add user relationship

	def __repr__(self):
		return '<Hello, this is Item #{}>'.format(self.id)

	def woop(self):
		print('woop woop, thats the sound of the police')

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	username = db.Column(db.String(50))
	email = db.Column(db.String(120), index=True, unique=True)
	password = db.Column(db.String(255))
	items = db.relationship("Item")

	def __init__(self, fn, last_name, username, email, password):
		self.first_name = fn
		self.last_name = last_name
		self.username = username
		self.email = email
		self.password = self.set_password(password)

	def my_name(self):
		print("Hi, my name is %s %s" % (self.first_name, self.last_name))

	def set_password(self, password):
		return generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password, password)

@login.user_loader
def load_user(id):
	return User.query.get(int(id))