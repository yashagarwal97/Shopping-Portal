from flask_sqlalchemy import SQLAlchemy
from app import db

class Cart(db.Model):
	id =db.Column(db.Integer,primary_key=True,autoincrement=True)
	itemid = db.Column(db.Integer)
	userid = db.Column(db.Integer)
	quantity = db.Column(db.Integer)
