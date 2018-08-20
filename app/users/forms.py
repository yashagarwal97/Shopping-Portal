from flask_wtf import FlaskForm
from wtforms import TextField,RadioField, SelectField,IntegerField,TextAreaField,SubmitField,PasswordField,BooleanField,ValidationError
from wtforms import validators, ValidationError
from wtforms.validators import DataRequired,Email,EqualTo

class RegistrationForm(FlaskForm):
	name = TextField("Name:",validators=[DataRequired()])
	email = TextField("Email",validators=[DataRequired(), Email()])
	password=PasswordField('Password:',validators=[DataRequired(),EqualTo('confirm_password')])
	confirm_password = PasswordField('Confirm_Password')
	submit = SubmitField("Signup")
	

class LoginForm(FlaskForm):
	email = TextField("Email",[validators.Required("Please enter your emailaddress.")])
	password=PasswordField('Password',[validators.Required('Please enter your password')])
	# remember_me = BooleanField('Remember_me', default=False)
	submit = SubmitField("Login")
