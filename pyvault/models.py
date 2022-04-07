from pyvault import db
from flask_login import UserMixin


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(120))
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))


class Passwords(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(120))
    service_username = db.Column(db.String(120))
    service_email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    notes = db.Column(db.String(150))
