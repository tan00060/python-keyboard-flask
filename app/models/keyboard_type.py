from .db import db

class KeyboardType(db.Model):
    __tablename__ = "keyboard_type"

    id = db.Column(db.Integer, primary_key=True)
    keyboard_type = db.Column(db.String(50), nullable=False, unique=False)
