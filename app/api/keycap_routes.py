from flask import Blueprint, request, session, jsonify
from ..models.db import db
from ..models.keycap_profile import KeycapProfile
from ..models.keycap import Keycap
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError


keycap_routes = Blueprint('keycap', __name__)

@keycap_routes.route('/keycap', methods=["GET"])
@login_required
def get_keycaps():
    keycaps = db.session.query(Keycap, KeycapProfile).join(KeycapProfile, Keycap.keycap_profile_id == KeycapProfile.id).all();
    keycap_list = [{"id": keycap.Keycap.id, "keycap_name": keycap.Keycap.keycap_name, "keycap_profile_name": keycap.KeycapProfile.keycap_profile_name} for keycap in keycaps]
    return keycap_list

@keycap_routes.route('/keycap', methods=["POST"])
@login_required
def create_keycaps():
    user_id = session['id']
    data = request.json
    new_keycap = Keycap(user_id=user_id, **data)
    try:
        db.session.add(new_keycap)
        db.session.commit()
        new_keycap_json = jsonify({'Keycap': new_keycap.to_dict()})
        return new_keycap_json, 200
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500


