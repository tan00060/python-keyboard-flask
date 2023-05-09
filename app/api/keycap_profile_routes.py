from flask import Blueprint, request
from ..models.db import db
from ..models.keycap_profile import KeycapProfile
from sqlalchemy.exc import SQLAlchemyError

keycap_profile_routes = Blueprint('keycap_profile', __name__)

@keycap_profile_routes.route('/keycap-profile', methods=["GET"])
def get_keycap_type():
    try:
        profiles = KeycapProfile.query.all();
        keycap_profile_list = [{"id": profile.id, "keycap_profile_name": profile.keycap_profile_name} for profile in profiles]
        return keycap_profile_list
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500