from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv
import os
import firebase_admin
from firebase_admin import firestore

# Get data from .env file
load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pyvault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.templates_auto_reload = True
app.secret_key = os.getenv('SECRET_KEY')

firebase_app = firebase_admin.initialize_app()
db = firestore.client(app = firebase_app)

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"

from pyvault.routes import *
