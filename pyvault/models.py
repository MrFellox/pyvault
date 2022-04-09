from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, email, password, first_name, last_name):
        """
        Creates a User object.
        """
        self.id = id
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def from_dict(source):
        return User(
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



class Password():
    def __init__(self, user_id:str, id:str, service_name:str, service_email:str, password:str):
        """
        Creates a Passwords object.
        """
        self.user_id = user_id
        self.id = id
        self.service_name = service_name
        self.service_email = service_email
        self.password = password

    @staticmethod
    def from_dict(source):
        return Password(
            id=source['id'],
            user_id = source['user_id'],
            service_name = source['service_name'],
            service_email=source['service_email'],
            password=source['service_password'],
        )

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'service_name': self.service_name,
            'service_email': self.service_email,
            'service_password': self.password,
        }

    def __repr__(self):
        return f'Password(id={self.id}, user_id={self.user_id}, service_name={self.service_name}, service_email={self.service_email}, password={self.password})'
