# Import flask and template operators
from flask import Flask, render_template, session, jsonify
from flask_mail import Mail
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
# Import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from functools import wraps

# Define the WSGI application object
app = Flask(__name__)
Bootstrap(app)
# Configurations
app.config.from_object('config')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'Your mail Id'
app.config['MAIL_PASSWORD'] = 'Your Password'

ADMINS=['shoppingportal4@gmail.com']

mail =Mail(app)
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling

@app.errorhandler(404)
def not_found(error):
   return render_template('index.html'), 200
'''

@app.route('/')
def home():
	return render_template('index.html')
'''

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@app.before_request
def before_request():
	g.user = current_user

# Import a module / component using its blueprint handler variable (mod_auth)
from app.users.controllers import mod_users
from app.items.controllers import mod_selleritems
from app.cart.controllers import mod_carts
from app.tags.controllers import mod_tags
from app.reviews.controllers import mod_reviews
from app.items.controllers2 import mod_buyeritems
from app.notifications.controllers import mod_notif
# Register blueprint(s)
app.register_blueprint(mod_users)
app.register_blueprint(mod_selleritems)
app.register_blueprint(mod_carts)
app.register_blueprint(mod_tags)
app.register_blueprint(mod_reviews)
app.register_blueprint(mod_buyeritems)
app.register_blueprint(mod_notif)
# app.register_blueprint(xyz_module)



# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
