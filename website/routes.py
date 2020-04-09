from website import app
from flask import render_template, redirect, url_for, request

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def index():
    return render_template('index.html')

