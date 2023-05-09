from .db import db
from flask_login import UserMixin 
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password_hashed = db.Column(db.String(255), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "keyboards": [keyboard.id for keyboard in self.keyboards],
            "keycaps": [keycap.id for keycap in self.keycaps],
            "switches": [{"id": switch.id, "name": switch.switch_name} for switch in self.switches]
        }
    
    @property
    def password(self):
        return self.password_hashed

    @password.setter
    def password(self, password):
        self.password_hashed = generate_password_hash(password)

# find better way to check hash so i dont get erros
    def check_password(self, password):
        return check_password_hash(self.password, password)