import os

class CONFIG_OBJ:
    DEBUG = False
    SECRET_KEY = os.environ.get('WEB_SECRET_KEY')
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('WEB_MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('WEB_MAIL_PASSWORD')
    RECIPIENT_EMAIL = os.environ.get('WEB_RECIPIENT_EMAIL')
    SQLALCHEMY_DATABASE_URI = os.environ.get('WEB_SQL_DB_PATH')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
