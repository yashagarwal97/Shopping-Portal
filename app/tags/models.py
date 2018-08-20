from flask_sqlalchemy import SQLAlchemy
from app import db


class Tags(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	tagcontent = db.Column(db.String(20))
	itemid = db.Column(db.Integer)
