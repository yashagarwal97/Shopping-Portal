from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin

class User(db.Model):
	__tablename__ = 'user'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(255))
	email = db.Column(db.String(255), unique=True)
	password = db.Column(db.String(255))
	buyerseller = db.Column(db.Integer)


	def __init__(self, name, email, password,buyerseller):
		self.name = name
		self.email = email
		self.password = generate_password_hash(password)
		self.buyerseller = buyerseller

	def check_password(self, password):
		return check_password_hash(self.password, password)

	def is_active(self):
		return True

	def is_anonymous(self):
		return False

	def is_authenticated(self):
		return True
		
	def get_id(self):
		print(self.id)
		return self.id
	
	def serialize(self):
		return { 'id' : self.id, 'name': self.name, 'email': self.email , 'buyerseller': self.buyerseller }

	def __repr__(self):
		return "< id %d name %s email %s>" % (self.id, self.name,self.email)

