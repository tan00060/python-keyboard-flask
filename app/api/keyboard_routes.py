from flask import Blueprint, request
from ..api_calls.keyboard_calls import get_all_keyboard, get_by_id_keyboard

keyboard_routes = Blueprint('keyboard', __name__)

@keyboard_routes.route('/keyboard', methods=["GET", "POST"])
def keyboard():
    if request.method == "GET":
        return get_all_keyboard()
    else:
        None


@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["GET"])
def keyboard_by_id(keyboard_id):
    if request.method == "GET":
        return get_by_id_keyboard(keyboard_id)
    else:
        None
