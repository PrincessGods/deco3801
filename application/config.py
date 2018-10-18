import os

class Config:
    SECRET_KEY = '3204436496843db0b799220bd0c151b2'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/deco3801'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')