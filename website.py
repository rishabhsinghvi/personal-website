from flask import Flask,current_app, url_for

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return current_app.send_static_file('index.html')

