from flask_sqlalchemy import SQLAlchemy
from app import db

class Item(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name = db.Column(db.String(40))
	imageurl = db.Column(db.String(40))
	quantity = db.Column(db.Integer)
	price = db.Column(db.Integer)
	description = db.Column(db.String(100))
	specifications = db.Column(db.String(50))
	userid = db.Column(db.Integer)
	shipping = db.Column(db.String(40))
	category=db.Column(db.String(30))
    

	def __init__(self,name,imageurl,quantity,price,description,specifications,userid,shipping,category):
		self.name = name
		self.imageurl = imageurl
		self.quantity = quantity
		self.price = price
		self.description = description
		self.specifications = specifications
		self.userid = userid
		self.shipping = shipping
		self.category=category

	def itemSerialize(self): 
		return { "id": self.id ,"user_id": self.userid ,"shipping":self.shipping, "price": self.price, "specifications": self.specifications,"name": self.name, "category": self.category ,"imageurl": self.imageurl, "quantity": self.quantity , "description": self.description}
		
