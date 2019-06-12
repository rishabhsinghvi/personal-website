import os
from website.utils import MAIL_PORT, MAIL_SERVER, MAIL_TLS

class CONFIG_OBJ:
    DEBUG = False
    SECRET_KEY = os.environ.get('WEB_SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('WEB_SQL_DB_PATH')
    MAIL_SERVER = MAIL_SERVER
    MAIL_PORT = MAIL_PORT
    MAIL_USE_TLS = MAIL_TLS
    MAIL_USERNAME = os.environ.get('WEB_MAIL_USER')
    MAIL_PASSWORD = os.environ.get('WEB_MAIL_PASS')
