from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, flash,redirect,jsonify
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from app.items.models import Item
from app.users.models import User
from app.notifications.models import Notif
from config import ADMINS
from app import db
mod_notif = Blueprint('notif', __name__, url_prefix = '/notif')

from flask_mail import Message
from app import mail

def send_email(subject, sender, recipients, text_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    mail.send(msg)

@mod_notif.route('/receive',methods=["POST"])
def receive():
	print("YO")
	userid = request.form['userid']
	itemid = request.form['itemid']
	print(userid,itemid)
	notif = Notif(userid = userid , itemid = itemid)
	db.session.add(notif)
	db.session.commit()
	return "JOB DONE"

