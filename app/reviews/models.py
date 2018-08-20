from flask_sqlalchemy import SQLAlchemy
from app import db


class Review(db.Model):
        id = db.Column(db.Integer,primary_key=True)
        text = db.Column(db.String(400))
        item_id=db.Column(db.Integer)
        user=db.Column(db.String(40))
        def __init__(self,text,item_id,username):
                self.text = text
                self.item_id=item_id
                self.user=username
        def revSerialize(self):
                return { "item_id":self.item_id,"Review": self.text,"user": self.user }
