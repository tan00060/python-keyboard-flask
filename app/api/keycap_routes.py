from flask import Blueprint, request
from ..models.db import db
from ..models.keycap_type import KeycapProfile
from ..models.keycap import Keycap

keycap_routes = Blueprint('keycap', __name__)

@keycap_routes.route('/keycap-type', methods=["GET"])
def get_keycap_type():
    profiles = KeycapProfile.query.all();
    keycap_profile_list = [{"id": profile.id, "keycap_profile_name": profile.keycap_profile_name} for profile in profiles]
    return keycap_profile_list

@keycap_routes.route('/keycap', methods=["GET"])
def get_keycaps():
    keycaps = db.session.query(Keycap, KeycapProfile).join(KeycapProfile, Keycap.keycap_profile_id == KeycapProfile.id).all();
    keycap_list = [{"id": keycap.Keycap.id, "keycap_name": keycap.Keycap.keycap_name, "keycap_profile_name": keycap.KeycapProfile.keycap_profile_name} for keycap in keycaps]
    return keycap_list


