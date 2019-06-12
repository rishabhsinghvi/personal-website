from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import utils
from flask_mail import Mail
import os
from website.config import CONFIG_OBJ

db = SQLAlchemy()
mail = Mail()

app = Flask(__name__)
app.config.from_object(CONFIG_OBJ)

db.init_app(app)
mail.init_app(app)

from website import routes

