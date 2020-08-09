from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField,PasswordField,SubmitField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo,ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
	username =StringField('Ləqəbin nədi sənin onu de bi mənə?',validators=[DataRequired(),Length(min=2,max=20)])

	email=StringField('Email-in nədi sənin bi de görüm',validators=[DataRequired(),Email()])


	password=PasswordField('Parolun nədi sən onu de bi görüm?',validators=[DataRequired()])
	confrim_password=PasswordField('Bir də yaz görüm əmin olum',validators=[DataRequired(),EqualTo('password')])

	submit=SubmitField('Bir dənə bura baş bir şey yoxlayıram')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Qaqa bu adı götürüblər sorry. Başqa bir dene tap')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Qaqa bu email uje var. Başqa bir dene tap')

class LoginForm(FlaskForm):
	email=StringField('Belə pis çıxmasın email-in nə idi?',validators=[DataRequired(),Email()])

	password=PasswordField('Parolun yadındadır?',validators=[DataRequired()])
	remember= BooleanField('Kef elə unutmaram səni')
	submit=SubmitField('Gəl daxil ol utanma öz saytın kimi fırlan')	

class UpdateAccountForm(FlaskForm):
	username =StringField('Ləqəbin nədi sənin onu de bi mənə?',validators=[DataRequired(),Length(min=2,max=20)])

	email=StringField('Email-in nədi sənin bi de görüm',validators=[DataRequired(),Email()])

	picture =FileField("Şəklini dəyiş fasonlu görsən", validators=[FileAllowed(['jpg','png','jpeg'])])
	submit=SubmitField('Qaqa əminsen? Dəqiq?')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Qaqa bu adı götürüblər sorry. Başqa bir dene tap')

	
	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Qaqa bu email uje var. Başqa bir dene tap')


class RequestResetForm(FlaskForm):
	email=StringField('Email-in nədi sənin bi de görüm',validators=[DataRequired(),Email()])		
	submit = SubmitField('Request Password Reset')



	def validate_email(self, email):
			user = User.query.filter_by(email=email.data).first()
			if user is None:
				raise ValidationError('Qaqa belə email yoxdu.Hələ  bir qeydiyyatdan keç.')



class ResetPasswordForm(FlaskForm):
	password=PasswordField('Parolun nədi sən onu de bi görüm?',validators=[DataRequired()])
	confirm_password=PasswordField('Bir də yaz görüm əmin olum',validators=[DataRequired(),EqualTo('password')])
	submit = SubmitField(' Password Reset')
