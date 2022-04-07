from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pyvault.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.templates_auto_reload = True
app.secret_key = '23595366b265957cdebfd34a57b253a3'

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)



from pyvault.routes import *
