from flask import render_template, redirect, url_for, request, current_app
from flask_mail import Message
from flask_login import login_user, current_user, logout_user, login_required

from website import app, mail, db
from website.forms import ContactForm, LoginForm, PostForm
from website.utils import validate_password
from website.models import User

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        msg = Message()
        
        msg.subject = 'You have a new message!'
        msg.sender = form.email.data
        msg.add_recipient(current_app.config['RECIPIENT_EMAIL'])
        msg.body = f"""
        Sender: {form.name.data}
        Sender Email: {form.email.data}
        Subject: {form.subject.data}
        Body: {form.message.data}
        """

        mail.send(msg)
        return redirect(url_for('index'))
        
    return render_template('index.html', form=form)

# Login for admin
@app.route('/login', methods=['POST', 'GET'])
@app.route('/login.html', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    if current_user.is_authenticated:
        print('Authenticated user attempting to login. Redirecting to index.html...')
        return redirect(url_for('index'))
    
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None:
            return redirect(url_for('login'))
        
        if validate_password(form.password.data, user.hash_pw) == False:
            # TODO: Flash
            return redirect(url_for('login'))
        
        print('Succesfully logged in!')
        login_user(user)
        return redirect(url_for('index'))


    return render_template('login.html', form=form)


@app.route('/logout', methods=['POST', 'GET'])
@login_required
def logout():
    logout_user()
    print('Succesfully logged out!')
    return redirect(url_for('index'))


@app.errorhandler(404)
def not_found(e):
    return render_template('not_found.html'), 404


@app.route('/new_post', methods=['POST', 'GET'])
@login_required
def new_post():
    form = PostForm()
    if request.method == "POST":
        if form.validate_on_submit():
            print('\n\n\n\n\n\n')
            print('Form Content:\n')
            print(form.html.data)
            print('\n\n\n\n')

    return render_template('new_post.html', form = form)
