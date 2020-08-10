import os
import smtplib
import secrets
from flask import url_for
import json
with open('/Users/gunes/tababuka/flaskblog/config.json') as config_file:
	config = json.load(config_file)

class Config:
	SECRET_KEY =config.get('SECRET_KEY')
	SQLALCHEMY_DATABASE_URI =config.get('SQLALCHEMY_DATABASE_URI')
	SQLALCHEMY_TRACK_MODIFICATIONS=False
def send_reset_email(user):
	token = user.get_reset_token()
	EMAIL_ADDRESS = config.get('EMAIL_USER')
	EMAIL_PASSWORD = config.get('EMAIL_PASS')

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()

		smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
		



		subject = 'Verification link'
		body = f'''To reset your password, visit the following link:
	{url_for('users.reset_token',token=token,_external=True)}If you did not make this request then simply ignore this email and no changing'''

    


		msg = f'Subject: {subject}\n\n{body}'
	    
		smtp.sendmail(EMAIL_ADDRESS, user.email, msg)    
