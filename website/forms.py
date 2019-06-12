from flask_wtf import FlaskForm
from wtforms.validators import Length, DataRequired, Email
from wtforms.widgets import TextArea
from wtforms import StringField, SubmitField
 

class MessageForm(FlaskForm):
    m_name = StringField(u'Name', validators=[DataRequired(), Length(min=1, max=30)])
    m_email = StringField(u'Email', validators=[DataRequired(), Email()])
    m_msg = StringField(u'Message', widget=TextArea(), validators=[DataRequired(), Length(max=500)])
    m_sub = SubmitField(u'Send message!')

    

