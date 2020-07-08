from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, FileField, HiddenField
from wtforms.validators import InputRequired, Email

class ContactForm(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired()], render_kw={"placeholder": "Your Name", "class": "form-control"})
    email = StringField('Your Email', validators=[InputRequired(), Email()], render_kw={"placeholder": "Your Email", "class": "form-control"})
    subject = StringField('Subject', validators=[InputRequired()], render_kw={"placeholder": "Subject", "class": "form-control"})
    message = StringField('Message', validators=[InputRequired()], render_kw={"placeholder": "Message", "class": "form-control"})
    submit = SubmitField('Send message', render_kw={"class": "btn btn-default btn-send"})


class LoginForm(FlaskForm):
    username = StringField('Name', validators=[InputRequired()], render_kw={"placeholder": "Username", "class": "form-control"})
    password = PasswordField('Password', validators=[InputRequired()], render_kw={"placeholder": "Password", "class": "form-control"})
    submit = SubmitField('Login', render_kw={"class": "btn btn-outline-primary btn-send"})


class PostForm(FlaskForm):
    delta = HiddenField('Delta')
    html = HiddenField('HTML')
    title = StringField('Name', validators=[InputRequired()], render_kw={"placeholder": 'Title', "class": "form-control"})
    tags = StringField('Tags', validators=[InputRequired()], render_kw={"placeholder": 'Tags', "class": "form-control"})
    submit = SubmitField('Create Post', render_kw={"class": "btn btn-outline-primary"})

    
