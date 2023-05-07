from .db import db

class KeycapProfile(db.Model):
    __tablename__ = "keycap_profile"

    id = db.Column(db.Integer, primary_key=True)
    keycap_profile_name = db.Column(db.String(50), nullable=False, unique=False)

    def to_dict(self):
        return {
            'id': self.id,
            'keycap_profile_name': self.keycap_profile_name,
        }