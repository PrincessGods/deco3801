import os

class Config:
    SECRET_KEY = '3204436496843db0b799220bd0c151b2'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://DECO3801Mars:DECO3801mars@deco3801rdstesting.c18plumnhyns.ap-southeast-2.rds.amazonaws.com/test'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')