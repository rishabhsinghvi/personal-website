from flask import Flask,current_app, url_for


app = Flask(__name__, static_url_path='/static')

app.config['SECRET_KEY'] = 
