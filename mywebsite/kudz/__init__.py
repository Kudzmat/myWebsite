from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '169d3c991557feaa996ccbbf'
mail = Mail(app)

from kudz import routes
