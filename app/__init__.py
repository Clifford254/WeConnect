from flask import Flask
from app.useraccounts import UserClass
from app.business import BusinessClass
from config import app_config


""" Initialize the app """
app = Flask(__name__, instance_relative_config=True)

# app.secret_key = 'tonystarktheironman'
app.config.from_object(app_config['development'])

user_object = UserClass()
business_object = BusinessClass()

from app import views


""" Load the config file """
app.config.from_object('config')