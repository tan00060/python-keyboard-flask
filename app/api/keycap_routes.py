from flask import Blueprint, request
from ..models.db import db
from ..models.keycap_profile import KeycapProfile
from ..models.keycap import Keycap

keycap_routes = Blueprint('keycap', __name__)

@keycap_routes.route('/keycap', methods=["GET"])
def get_keycaps():
    keycaps = db.session.query(Keycap, KeycapProfile).join(KeycapProfile, Keycap.keycap_profile_id == KeycapProfile.id).all();
    keycap_list = [{"id": keycap.Keycap.id, "keycap_name": keycap.Keycap.keycap_name, "keycap_profile_name": keycap.KeycapProfile.keycap_profile_name} for keycap in keycaps]
    return keycap_list


