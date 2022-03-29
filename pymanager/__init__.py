from flask import Flask

app = Flask(__name__)
app.templates_auto_reload = True
app.secret_key = '23595366b265957cdebfd34a57b253a3'

from pymanager.routes import *
