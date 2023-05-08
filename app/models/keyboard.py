from .db import db

class Keyboard(db.Model):
    __tablename__ = "keyboard"

    id = db.Column(db.Integer, primary_key=True)
    keyboard_name = db.Column(db.String(50), nullable=False, unique=False)
    keyboard_type_id = db.Column(db.Integer, db.ForeignKey("keyboard_type.id"), nullable=False, unique=False)
    switch_id = db.Column(db.Integer, db.ForeignKey("switch.id"), nullable=False, unique=False)
    keycap_id = db.Column(db.Integer, db.ForeignKey("keycap.id"), nullable=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, unique=False)

    switch = db.relationship("Switch")
    keycap = db.relationship("Keycap")
    keyboard_type = db.relationship("KeyboardType")
    user = db.relationship("User", backref="keyboards")

    def to_dict(self):
        return {
            'id': self.id,
            'keyboard_name': self.keyboard_name,
            'keyboard_type_id': self.keyboard_type_id,
            'switch_id': self.switch_id,
            'keycap_id': self.keycap_id,
            'user_id': self.user_id
        }