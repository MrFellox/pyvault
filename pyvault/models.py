import email
from pyvault import db
from flask_login import UserMixin


class Users(UserMixin):
    def __init__(self, id, email, password, first_name, last_name):
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def from_dict(source):
        return Users(
            id=source['id'],
            email=source['email'],
            password=source['password'],
            first_name=source['first_name'],
            last_name=source['last_name']
        )

    def to_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name
        }

    def __repr__(self):
        return f'User(id={self.id}, email={self.email}, first_name={self.first_name}, last_name={self.last_name})'



class Passwords(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), primary_key=True)
    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(120))
    service_username = db.Column(db.String(120))
    service_email = db.Column(db.String(120))
    password = db.Column(db.String(120))
    notes = db.Column(db.String(150))
