from flask import Blueprint, request, jsonify, session
from ..models.db import db
from ..models.keycap import Keycap
from ..models.switch import Switch
from ..models.keyboard_type import KeyboardType
from ..models.keyboard import Keyboard
from ..models.user import User
from sqlalchemy.exc import SQLAlchemyError
from flask_login import current_user, login_user, logout_user, login_required

keyboard_routes = Blueprint('keyboard', __name__)

@keyboard_routes.route('/keyboard', methods=["GET"])
@login_required
def keyboard():
    user_id = session['id']  # Get the user_id from the session
    try:
        keyboards = db.session.query(Keyboard, Keycap, Switch, KeyboardType).join(KeyboardType, Keyboard.keyboard_type_id == KeyboardType.id).join(Switch, Keyboard.switch_id == Switch.id).join(Keycap, Keyboard.keycap_id == Keycap.id).filter(Keyboard.user_id == user_id).all()
        keyboard_list = [{"id": keyboard.Keyboard.id, "keyboard_name": keyboard.Keyboard.keyboard_name,"keycap": keyboard.Keycap.keycap_name, "switch_name": keyboard.Switch.switch_name, "keyboard_type": keyboard.KeyboardType.keyboard_type} for keyboard in keyboards]
        return keyboard_list
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["GET"])
@login_required
def get_keyboard_by_id(keyboard_id):
    user_id = session['id']
    keyboard = Keyboard.query.get(keyboard_id)

    if keyboard:
        if keyboard.user_id == user_id:
            return keyboard.to_dict(), 200 
        else:
            return {'errors': [f'Keyboard ID: {keyboard_id} was not found']}, 404 
    else:
        return {'errors': [f'Keyboard ID: {keyboard_id} was not found']}, 404

@keyboard_routes.route('/keyboard', methods=["POST"])
@login_required
def create_keyboard():
    data = request.json
    user_id = session['id']
    new_keyboard = Keyboard(user_id=user_id, **data)
    try:
        db.session.add(new_keyboard)
        db.session.commit()
        keyboard_json = jsonify({'Keyboard': new_keyboard.to_dict()})
        return keyboard_json, 200
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["DELETE"])
@login_required
def delete_keyboard_by_id(keyboard_id):
    user_id = session['id']  # Get the user_id from the session
    keyboard = Keyboard.query.get(keyboard_id)

    if keyboard:
        if keyboard.user_id == user_id:  # Check if the keyboard belongs to the logged-in user
            db.session.delete(keyboard)
            db.session.commit()
            return jsonify({'message': f'Keyboard ID: {keyboard_id} was successfully deleted'}), 200
        else:
            return jsonify({'error': 'Keyboard not found'}), 404
    else:
        return jsonify({'errors': [f'Keyboard ID: {keyboard_id} was not found']}), 404

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["PUT"])
@login_required
def update_keyboard(keyboard_id):
    user_id = session['id']

    keyboard = Keyboard.query.get(keyboard_id)
    if not keyboard:
        return jsonify({'error': 'Keyboard not found'}), 404

    if keyboard.user_id != user_id:
        return jsonify({'error': 'Keyboard not found'}), 404

    data = request.json

    if 'keyboard_name' in data:
        keyboard.keyboard_name = data["keyboard_name"]
    if 'keyboard_type_id' in data:
        keyboard.keyboard_type_id = data["keyboard_type_id"]
    if 'switch_id' in data:
        keyboard.switch_id = data["switch_id"]
    if 'keycap_id' in data:
        keyboard.keycap_id = data["keycap_id"]

    try:
        db.session.commit()
        return keyboard.to_dict(), 200

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500


