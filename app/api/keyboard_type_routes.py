from flask import Blueprint, request
from ..models.db import db
from ..models.keyboard_type import KeyboardType
from sqlalchemy.exc import SQLAlchemyError

keyboard_type_routes = Blueprint('keyboard_type', __name__)

@keyboard_type_routes.route('/keyboard-type', methods=["GET"])
def get_keycap_type():
    try:
        keyboard_types = KeyboardType.query.all();
        keyboard_type_list = [{"id": type.id, "keyboard_type": type.keyboard_type} for type in keyboard_types]
        return keyboard_type_list
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500
