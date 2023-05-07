from .db import db

class SwitchType(db.Model):
    __tablename__ = "switch_type"

    id = db.Column(db.Integer, primary_key=True)
    switch_type = db.Column(db.String(50), nullable=False, unique=False)

    def to_dict(self):
        return {
            'id': self.id,
            'switch_type': self.switch_type,
        }