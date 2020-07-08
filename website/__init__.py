from flask import Flask
from flask_mail import Mail
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

import os

from website.config import CONFIG_OBJ

mail = Mail()
login_manager = LoginManager()
db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(CONFIG_OBJ)

mail.init_app(app)
login_manager.init_app(app)
db.init_app(app)

from website import routes
from website import models