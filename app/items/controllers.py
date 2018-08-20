from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash,redirect
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for,jsonify
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from io import BytesIO
from PIL import Image
from app import db
import os
from flask_mail import Message
from app import mail
from config import ADMINS
from app.users.models import User
from app.items.models import Item
from app.cart.models import Cart
from app.tags.models import Tags
from app.notifications.models import Notif
mod_selleritems = Blueprint('sellertable', __name__, url_prefix = '/sellertable')


@mod_selleritems.route('/additem',methods=['GET','POST'])
def addItem():
	if not g.user.is_authenticated or g.user.buyerseller == 0:
		return "You need to login as a seller for accessing this."
	if request.method=='POST':
		name = request.form['name']
		quantity = request.form['quantity']
		imageurl=""
		price = int(request.form['price'])
		description = request.form['description']
		specifications = request.form['specifications']
		img= request.files['photo']
		shipping = request.form['shipping']
		tags = request.form['tags']
		category=request.form['category']
		sellerid = g.user.id
		s=Item(name,imageurl,quantity,price,description,specifications,sellerid,shipping,category)
		db.session.add(s)
		db.session.commit()
		taglist=tags.split(' ')
		for i in range(len(taglist)):
			t = Tags(tagcontent=taglist[i],itemid=s.id)
			db.session.add(t)
			db.session.commit()


		img = Image.open(img)
		dir=os.getcwd()
		dir1= os.path.join(dir,'app/static/')
		filename = str(s.id)+'.jpg'
		imageurl = dir1+ filename
		print(imageurl)
		img.save(imageurl)
		print("YO")
		item = Item.query.filter(Item.id == s.id).first()
		item.imageurl = filename
		print(item.imageurl)
		print(s.id)
		db.session.commit()
		cartproduct = Cart(itemid=s.id,userid=g.user.id,quantity=quantity)
		db.session.add(cartproduct)
		db.session.commit()
	
		print(s.id)
		return redirect(url_for('.sellertable'))

	else:
		return render_template("itementryform.html")




def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)


@mod_selleritems.route("/update",methods=["POST"])
def updatequantity():
	if request.method=="POST" and g.user.is_authenticated and g.user.buyerseller:
		itemid = request.form['itemid']
		print(itemid)
		quanti= request.form['quantity']
		item = Item.query.filter(Item.id == itemid).first()
		if (item.quantity <= 0):
			users = Notif.query.filter( Notif.itemid == itemid).all()
			for i in users:	
				user = User.query.filter(User.id == i.userid).first()
				print(user.email)
				send_email("The item you wished for is now available" ,ADMINS[0],ADMINS,"YO")

		item.quantity=quanti
		db.session.commit();
		return "Successfully updated items in your cart!"
	else:
		return "Please login to continue"

@mod_selleritems.route("/getitems",methods=["GET"])
def get_all_items():
	if request.method=="GET" and g.user.is_authenticated and g.user.buyerseller:
		it = Item.query.all()
		allitems={ "items" : []}
		for i in it:
	  		print(i.imageurl)
	  		allitems["items"].append(i.itemSerialize())

		return jsonify(allitems)


@mod_selleritems.route("",methods=["GET"])
def sellertable():
	if g.user.is_authenticated and g.user.buyerseller == 1:
		return render_template('sellertable.html')
	else:
		return "Sorry you are not authorized to access this page"
		

@mod_selleritems.route("/categorytable/<typ>",methods=['GET'])
def categorytable(typ):
	if request.method == 'GET':
		print(typ)
		item=Item.query.filter(Item.category == typ).all()
		allcategory=[]
		for i in item:
			allcategory.append(i.itemSerialize())
		print(allcategory)
	return render_template('categorytable.html',allcategory=allcategory)
