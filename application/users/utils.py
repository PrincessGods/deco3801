import secrets
import os
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from application import mail

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 
                                'static/imgs', picture_fn)

    output_size = (300, 300)
    thumbnail_picture = Image.open(form_picture)
    thumbnail_picture.thumbnail(output_size)
    thumbnail_picture.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', 
                    sender='noreply@deco3801mars.com', 
                    recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no change will be made.
'''
    mail.send(msg)