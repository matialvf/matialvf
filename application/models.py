from datetime import datetime
from application import db

class Item(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	time = db.Column(db.DateTime, default=datetime.utcnow)
	event = db.Column(db.String(50))
	description = db.Column(db.String(255))

	def __repr__(self):
		return '<Hello, this is Item #{}>'.format(self.id)

	def woop(self):
		print('woop woop, thats the sound of the police')

class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(50))
	last_name = db.Column(db.String(50))
	username = db.Column(db.String(50))
	password = db.Column(db.String(50))

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def my_name(self):
		print("Hi, my name is %s %s" % (self.first_name, self.last_name))
