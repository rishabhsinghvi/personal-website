from website import app, db, mail
from flask import render_template, redirect, url_for, request
from website.forms import MessageForm
from website.models import DB_Message
from flask_mail import Message
from website.utils import MsgTo, MsgFrom, MsgSubject
import datetime

@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
@app.route('/index.html', methods=['POST', 'GET'])
def index():
    form = MessageForm()
    if form.validate_on_submit():
        try:
            db_msg = DB_Message(m_name=form.m_name.data, m_email=form.m_email.data, m_msg = form.m_msg.data)
            db.session.add(db_msg)
            db.session.commit()

            msg = Message(MsgSubject, sender=MsgFrom, recipients=[MsgTo])

            msg.body = '''
            Name: {}
            Email: {}
            Message: {}
            Time: {}
            '''.format(form.m_name.data, form.m_email.data, form.m_msg.data, datetime.datetime.now())

            mail.send(msg)
        except:
            return redirect(url_for('index'))

        return redirect(url_for('msg_sent'))
    
    return render_template('index.html', form=form, css=url_for('static', filename='css/index.css'), jsfile=url_for('static', filename='js/home.js')) 


@app.route('/msgsent')
def msg_sent():
    return render_template('msgsent.html', css=url_for('static', filename='css/msgsent.css'), jsfile=url_for('static', filename="js/msgsent.js"))

