from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash,redirect
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from io import BytesIO
from PIL import Image
from app import db
from sqlalchemy import and_
import os

from app.items.models import Item
from app.cart.models import Cart
from app.tags.models import Tags

mod_buyeritems = Blueprint('buyertable', __name__, url_prefix = '/buyertable')

@mod_buyeritems.route("/additem",methods=["POST"])
def additemtobuyer():
	if request.method=="POST" and g.user.is_authenticated and g.user.buyerseller==0:
		itemid = request.form['itemid']
		if len(Cart.query.filter(and_(Cart.itemid == itemid , Cart.userid == g.user.id)).all()):
			return "Already added item to your cart"
		c = Cart(itemid=itemid,userid = g.user.id,quantity=1)
		db.session.add(c)
		db.session.commit()
		return "Successfully added to cart!"
	else:
		return "Sorry you have to first login as a buyer"

@mod_buyeritems.route("/update",methods=["POST"])
def updatebuyer():
        if request.method=="POST" and g.user.is_authenticated and g.user.buyerseller==0:
                itemid = request.form['itemid']
                print(itemid)
                quanti= request.form['quantity']
                item = Cart.query.filter(and_(Cart.userid == g.user.id , Cart.itemid == itemid)).first()
		
                item.quantity=quanti
                print(item.quantity)
                db.session.commit();
                return "Successfully updated"
        else:
                return "Sorry you are not authorized to access this page"
	


@mod_buyeritems.route("",methods=["GET"])
def buyertable():
	if g.user.is_authenticated and g.user.buyerseller==0:
		return render_template('buyertable.html')
	else:
		return "Sorry you are not authorized to access this page"
