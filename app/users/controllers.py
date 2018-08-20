from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for
from app import db,login_manager
from flask_cors import CORS
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from flask_login import LoginManager, login_user, logout_user, login_required, current_user,UserMixin
from sqlalchemy import and_
from app.users.models import User
from app.users.forms import RegistrationForm,LoginForm
mod_users = Blueprint('users', __name__, url_prefix='')


@login_manager.user_loader
def load_user(user_id):
	return  User.query.get(int(user_id))



@mod_users.route('/')
def home():
	return render_template('index.html')


@mod_users.route('/signupBuyer', methods=['GET', 'POST'])
def registerBuyer():
	
	form=RegistrationForm()
	if request.method == 'POST':
		if form.validate()==False:
			flash('all fields are required')
			return render_template('register1.html',form=form)
		else:
			name=form.name.data
			email=form.email.data
			password=form.password.data
			try:
				buyer=User(name,email,password,0)
				db.session.add(buyer)
				db.session.commit()
				flash('You have successfully registered! You may now login.')
				return redirect(url_for('.loginBuyer'))
			except:
				error_mesg="User with given email already registered"
				print(error_mesg)
				return render_template('register1.html',form=form,error=error_mesg)
	else :

		return render_template('register1.html',form=form)


@mod_users.route('/signupSeller', methods=['GET', 'POST'])
def registerSeller():
	form=RegistrationForm()
	if request.method == 'POST':
		if form.validate()==False:
			flash('all field are required')
			return render_template('register1.html',form=form)
		else:

			name=form.name.data
			email=form.email.data
			password=form.password.data
			try:
				seller =User(name,email,password,1)
				db.session.add(seller)
				db.session.commit()
				print('gulshan')
				flash('You have successfully registered! You may now login.')
				return redirect(url_for('.loginSeller'))
			except:
				error_mesg="User with given email already registered"
				print(error_mesg)
				return render_template('register1.html',form=form,error=error_mesg)
	else :

		return render_template('register1.html',form=form) 


@mod_users.route('/loginBuyer',methods=['GET','POST'])
def loginBuyer():
	form=LoginForm(request.form)
	remember_me = False
	if form.validate_on_submit():
		if 'remember_me' in form:
			remember_me=True
		buyer = User.query.filter(and_(User.email==form.email.data,User.buyerseller==0)).first()
		if buyer  is not None and buyer.check_password(form.password.data):
			login_user(buyer,remember=remember_me)
			return redirect(url_for('.home'))
			
		else:
			if buyer is None:
				error_mesg="Invalid email . Please register yourself first."
			else:
				error_mesg="Invalid password . Please try again!'"
			return render_template('login.html',form=form,error=error_mesg)
	else:
		return render_template('login.html',form=form)



@mod_users.route('/loginSeller',methods=['GET','POST'])
def loginSeller():
	form=LoginForm(request.form)
	remember_me = False
	if form.validate_on_submit():
		if 'remember_me' in form:
			remember_me=True
		seller = User.query.filter(and_(User.email==form.email.data,User.buyerseller==1)).first()
		if seller  is not None and seller.check_password(form.password.data):
			login_user(seller,remember=remember_me)
			print("Logging user in")
			return redirect(url_for('.home'))
		else:
			if seller is None:
				error_mesg="Invalid email . Please register yourself first."
			else:
				error_mesg="Invalid password . Please try again!"
			return render_template('login.html',form=form,error=error_mesg)
	else:
		return render_template('login.html',form=form)


@mod_users.route('/logout')
def logout():
	if g.user.is_authenticated():
		logout_user()
		print("Reachedlogout")
		flash('You have successfully been logged out.')
		return redirect(url_for('.home'))
	else:
		return redirect(url_for('.home'))

