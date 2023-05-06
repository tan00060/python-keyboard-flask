from flask import Blueprint, request
from ..api_calls.keyboard_calls import get_all_keyboard

keyboard_routes = Blueprint('keyboard', __name__)

@keyboard_routes.route('/keyboard', methods=["GET", "POST"])
def keyboard():
    if request.method == "GET":
        return get_all_keyboard()
    else:
        None