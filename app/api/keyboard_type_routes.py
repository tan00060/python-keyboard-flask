from flask import Blueprint, request
from ..models.db import db
from ..models.keyboard_type import KeyboardType

keyboard_type_routes = Blueprint('keyboard_type', __name__)

@keyboard_type_routes.route('/keyboard-type', methods=["GET"])
def get_keycap_type():
    keyboard_types = KeyboardType.query.all();
    keyboard_type_list = [{"id": type.id, "keyboard_type": type.keyboard_type} for type in keyboard_types]
    return keyboard_type_list
