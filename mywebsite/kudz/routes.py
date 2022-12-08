from flask import render_template
from kudz import app
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo


@app.route('/')
def home():
    #form = ContactForm()

    return render_template("index.html")


@app.route('/projects')
def projects():
    return render_template('projects.html')

"""
class ContactForm(FlaskForm):
    email = StringField(label='Email', validators=[Email(), DataRequired()])
    subject = StringField(label='Subject:', validators=[DataRequired()])
    message = StringField(label='Message', validators=[DataRequired()])
    submit = SubmitField(label='Send Email')
"""