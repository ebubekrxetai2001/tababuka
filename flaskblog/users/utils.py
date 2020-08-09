import os
import secrets
from PIL import Image
from flask import url_for,current_app
import smtplib
from flask_mail import Message
from flaskblog import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
    EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)




        subject = 'Verification link'
        body = f'''To reset your password, visit the following link:
{url_for('users.reset_token',token=token,_external=True)}

If you did not make this request then simply ignore this email and no changing
'''

        


        msg = f'Subject: {subject}\n\n{body}'
    
        smtp.sendmail(EMAIL_ADDRESS, user.email, msg)    