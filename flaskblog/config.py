import os
import smtplib
import secrets
from flask import url_for

class Config:
	SECRET_KEY ="421070be4c6a0c41ab002c357a836532"
	SQLALCHEMY_DATABASE_URI ="sqlite:///site.db"
	SQLALCHEMY_TRACK_MODIFICATIONS=False
def send_reset_email(user):
	token = user.get_reset_token()
	EMAIL_ADDRESS = "EMAIL_USER"
	EMAIL_PASSWORD = "EMAIL_PASS"

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
