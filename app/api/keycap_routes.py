from flask import Blueprint, request, session, jsonify
from ..models.db import db
from ..models.keycap_profile import KeycapProfile
from ..models.keycap import Keycap
from flask_login import login_required
from sqlalchemy.exc import SQLAlchemyError


keycap_routes = Blueprint('keycap', __name__)

@keycap_routes.route('/keycap', methods=["GET"])
@login_required
def get_keycaps():
    user_id = session['id']
    try:
        keycaps = db.session.query(Keycap, KeycapProfile).join(KeycapProfile, Keycap.keycap_profile_id == KeycapProfile.id).filter(Keycap.user_id == user_id).all()
        keycap_list = [{"id": keycap.Keycap.id, "keycap_name": keycap.Keycap.keycap_name, "keycap_profile_name": keycap.KeycapProfile.keycap_profile_name} for keycap in keycaps]
        return keycap_list
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

@keycap_routes.route('/keycap/<int:keycap_id>', methods=["GET"])
@login_required
def get_by_id_keycaps(keycap_id):
    user_id = session['id']
    try:
        keycap = Keycap.query.get(keycap_id)
        if keycap:
            if keycap.user_id == user_id:
                return keycap.to_dict(), 200 
            else:
                return {'errors': [f'keycaps ID: {keycap_id} was not found']}, 404 
        else:
            return {'errors': [f'keycaps ID: {keycap_id} was not found']}, 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

@keycap_routes.route('/keycap', methods=["POST"])
@login_required
def create_keycaps():
    user_id = session['id']
    try:
        data = request.json
        new_keycap = Keycap(user_id=user_id, **data)
        db.session.add(new_keycap)
        db.session.commit()
        new_keycap_json = jsonify({'Keycap': new_keycap.to_dict()})
        return new_keycap_json, 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

@keycap_routes.route('/keycap/<int:keycap_id>', methods=["PUT"])
@login_required
def update_keycaps(keycap_id):
    user_id = session['id']
    try:
        data = request.json
        keycap = Keycap.query.get(keycap_id)
        if not keycap:
            return jsonify({'error': 'Keyboard not found'}), 404
        if keycap.user_id != user_id:
            return jsonify({'error': 'Keyboard not found'}), 404
        if 'keycap_name' in data:
            keycap.keycap_name = data["keycap_name"]
        if 'keycap_profile_id' in data:
            keycap.keycap_profile_id = data["keycap_profile_id"]

        db.session.add(keycap)
        db.session.commit()
        return keycap.to_dict(), 200
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500

@keycap_routes.route('/keycap/<int:keycap_id>', methods=["DELETE"])
@login_required
def delete_keycaps(keycap_id):
    user_id = session['id']
    keycap = Keycap.query.get(keycap_id)
    try:
        if keycap:
            if keycap.user_id == user_id:
                db.session.delete(keycap)
                db.session.commit()
                return jsonify({'message': f'keycap ID: {keycap_id} was successfully deleted'}), 200
            else:
                return jsonify({'error': 'keycap not found'}), 404
        else:
            return jsonify({'errors': [f'keycap ID: {keycap_id} was not found']}), 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500


