import os

class CONFIG_OBJ:
    DEBUG = False
    SECRET_KEY = os.environ.get('WEB_SECRET_KEY')
