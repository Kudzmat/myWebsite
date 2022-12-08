from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


class ContactForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    subject = StringField(label='Subject:', validators=[DataRequired()])
    message = StringField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send Email')

