from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash,redirect,jsonify
from flask_cors import CORS
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from functools import wraps
from sqlalchemy import and_
from app.items.models import Item
from app.cart.models import Cart

from app import db
mod_carts = Blueprint('cart', __name__, url_prefix = '/cart')

@mod_carts.route("/cartitems",methods=["GET"])
def getitem():
	cartitems = Cart.query.filter(Cart.userid==g.user.id).all()
	itemlist={ 'items' : []}
	for i in cartitems:

  		item = Item.query.filter(Item.id == i.itemid).first()
  		itemlist['items'].append(item.itemSerialize())
	return jsonify(itemlist)


@mod_carts.route("/cartitemsofbuyer",methods=["GET"])
def getitemsofbuyer():
	cartitems = Cart.query.filter(Cart.userid==g.user.id).all()
	itemlist={ 'items' : [] , 'qnty' : []}
	for i in cartitems:

  		item = Item.query.filter(Item.id == i.itemid).first()
  		print(i.quantity)
  		itemlist['items'].append(item.itemSerialize())
  		itemlist['qnty'].append(i.quantity)
	return jsonify(itemlist)

@mod_carts.route("/buy",methods=["POST"])
def buyitemsincart():
	if request.method=="POST":
		cartitems = Cart.query.filter(Cart.userid == g.user.id).all()
		flag=0
		for i in cartitems:
			item = Item.query.filter(Item.id == i.itemid).first()
			if (i.quantity > item.quantity):
				flag=1
				i.quantity = item.quantity
				db.session.commit()
		if (flag):
			return "We have a shortage of some items.The available quantities have been updated.Click buy again to place your order."
		for i in cartitems:
			item = Item.query.filter(Item.id == i.itemid).first()
			item.quantity = item.quantity - i.quantity;
			i.quantity=0
			db.session.commit()
		return "Thank you for purchasing!"

@mod_carts.route("/delete",methods=["POST"])
def deleteitemsincart():
	if request.method=="POST":
		itemid = request.form['itemid']
		cartitem = Cart.query.filter(and_(Cart.userid == g.user.id , Cart.itemid == itemid )).first()
		db.session.delete(cartitem)
		db.session.commit()
		return "Successfully deleted item"		 
