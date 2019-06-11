from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from website import utils

app = Flask(__name__)
app.config['SECRET_KEY'] = utils.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = utils.SQL_DB_PATH
db = SQLAlchemy(app)

class Message(db.Model):
    m_id = db.Column(db.Integer, primary_key = True)
    m_name = db.Column(db.String(20), nullable = False)
    m_email = db.Column(db.String(100), nullable = False)
    m_msg = db.Column(db.Text, nullable = False)
    m_msg_time = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def __repr__(self):
        return f"Message({self.m_name}, {self.m_email}, {self.m_msg})"

from website import routes