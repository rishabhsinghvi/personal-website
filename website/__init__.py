from flask import Flask,current_app, url_for


app = Flask(__name__)


from website import routes