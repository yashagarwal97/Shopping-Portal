from app import db
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash,redirect
from flask_cors import CORS
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from flask_wtf import FlaskForm

from app.items.models import Item
from app.tags.models import Tags

mod_tags= Blueprint('tags', __name__, url_prefix = '/tags')


@mod_tags.route("/displayproducts",methods=['POST'])
def displayproducts():
	if request.method == 'POST':

		inp = request.form['tagstring']
		taglist = inp.split(' ')
		itemlist=[]
		items = Item.query.all()
		
		mp={}
		for i in taglist:
			items=Tags.query.filter(Tags.tagcontent == i).all()
			print(i)
			for j in items:
				if  not j.itemid in mp:
					mp[j.itemid]=1
					it = Item.query.filter(Item.id == j.itemid).first()
					itemlist.append(it.itemSerialize())
		
		return render_template('displaypage.html',itemlist=itemlist)

@mod_tags.route("/<itemid>",methods=["GET"])
def itemwithid(itemid):
  item = Item.query.filter(Item.id == itemid).first()
  return render_template('description.html',item = item)

