from .db import db

class Keycap(db.Model):
    __tablename__ = "keycap"

    id = db.Column(db.Integer, primary_key=True)
    keycap_name = db.Column(db.String(50), nullable=False, unique=False)
    keycap_profile_id = db.Column(db.Integer, db.ForeignKey("keycap_profile.id"), nullable=False)

    keycap_profile = db.relationship("KeycapProfile")

    def to_dict(self):
        return {
            'id': self.id,
            'keycap_profile_name': self.keycap_profile_name,
            'keycap_profile': self.keycap_profile_id
        }