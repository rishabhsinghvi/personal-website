from website import app
from flask import render_template, redirect, url_for, request

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
@app.route('/about.html', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/skills', methods=['GET'])
@app.route('/skills.html', methods=['GET'])
def skills():
    return render_template('skills.html')


@app.route('/contact', methods=['GET'])
@app.route('/contact.html', methods=['GET'])
def contact():
    return render_template('contact.html')