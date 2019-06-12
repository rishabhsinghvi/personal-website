from website import app, db
from flask import render_template, redirect, url_for, request
from website.forms import MessageForm
from website.models import Message


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def index():
    form = MessageForm()
    if form.validate_on_submit():

        msg = Message(m_name=form.m_name.data, m_email=form.m_email.data, m_msg = form.m_msg.data)
        db.session.add(msg)
        db.session.commit()

        return redirect(url_for('msg_sent'))
    
    return render_template('index.html', form=form, css=url_for('static', filename='css/index.css'), jsfile=url_for('static', filename='js/home.js')) 


@app.route('/msgsent')
def msg_sent():
    return render_template('msgsent.html', css=url_for('static', filename='css/msgsent.css'), jsfile=url_for('static', filename="js/msgsent.js"))

