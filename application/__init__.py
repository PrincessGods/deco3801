import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

application = Flask(__name__)
application.config['SECRET_KEY'] = '3204436496843db0b799220bd0c151b2'
application.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('MySQL')
db = SQLAlchemy(application)
bcrypt = Bcrypt(application)
login_manager = LoginManager(application)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
application.config['MAIL_SERVER'] = 'smtp.googlemail.com'
application.config['MAIL_PORT'] = 587
application.config['MAIL_USE_TLS'] = True
application.config['MAIL_USERNAME'] = os.environ.get('MAIL_USER')
application.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASS')
mail = Mail(application)

from application import routes