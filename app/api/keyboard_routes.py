from flask import Blueprint, request, jsonify
from ..models.db import db
from ..models.keycap import Keycap
from ..models.switch import Switch
from ..models.keyboard_type import KeyboardType
from ..models.keyboard import Keyboard
from sqlalchemy.exc import SQLAlchemyError

keyboard_routes = Blueprint('keyboard', __name__)

@keyboard_routes.route('/keyboard', methods=["GET"])
def keyboard():
    try:
        keyboards = db.session.query(Keyboard, Keycap, Switch, KeyboardType).join(KeyboardType, Keyboard.keyboard_type_id == KeyboardType.id).join(Switch, Keyboard.switch_id == Switch.id).join(Keycap, Keyboard.keycap_id == Keycap.id).all()
        keyboard_list = [{"id": keyboard.Keyboard.id, "keyboard_name": keyboard.Keyboard.keyboard_name,"keycap": keyboard.Keycap.keycap_name, "switch_name": keyboard.Switch.switch_name, "keyboard_type": keyboard.KeyboardType.keyboard_type} for keyboard in keyboards]
        return keyboard_list
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["GET"])
def get_keyboard_by_id(keyboard_id):
    keyboard = Keyboard.query.get(keyboard_id)
    return keyboard.to_dict()

@keyboard_routes.route('/keyboard', methods=["POST"])
def create_keyboard():
    data = request.json
    new_keyboard = Keyboard(**data)
    try:
        db.session.add(new_keyboard)
        db.session.commit()
        switch_json = jsonify({'Keyboard': new_keyboard.to_dict()})
        return switch_json
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["DELETE"])
def delete_keyboard_by_id(keyboard_id):
    keyboard = Keyboard.query.get(keyboard_id)
    if keyboard:
        db.session.delete(keyboard)
        db.session.commit()
        return {'message': f'keyboard Id: {keyboard_id} was successfully deleted'}
    else:
        return {'errors': [f'keyboard Id: {keyboard_id} was not found']}

@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["PUT"])
def update_keyboard(keyboard_id):
    try:
        keyboard = Keyboard.query.get(keyboard_id)
        if not keyboard:
            return jsonify({'error': 'keyboard not found'}), 404
        
        data = request.json

        if 'keyboard_name' in data:
            keyboard.keyboard_name = data["keyboard_name"]
        if 'keyboard_type_id' in data:
            keyboard.keyboard_type_id = data["keyboard_type_id"]
        if 'switch_id' in data:
            keyboard.switch_id = data["switch_id"]
        if 'keycap_id' in data:
            keyboard.keycap_id = data["keycap_id"]

        db.session.commit()
        return {'message': f'Keyboard Id: {keyboard_id} was successfully updated'}

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500


