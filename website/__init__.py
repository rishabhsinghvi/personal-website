from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = utils.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = utils.SQL_DB_PATH
db = SQLAlchemy(app)

from website import routes