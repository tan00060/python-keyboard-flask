from .db import db

class Switch(db.Model):
    __tablename__ = "switch"

    id = db.Column(db.Integer, primary_key=True)
    switch_name = db.Column(db.String(50), nullable=False, unique=False)
    switch_type_id = db.Column(db.Integer, db.ForeignKey("switch_type.id"), nullable=False)

    switch_type = db.relationship("SwitchType")


    def to_dict(self):
        return {
            'id': self.id,
            'switch_name': self.switch_name,
            'switch_type_id': self.switch_type_id
        }