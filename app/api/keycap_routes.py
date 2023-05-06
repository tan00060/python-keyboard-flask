from flask import Blueprint, request
from ..api_calls.keycap_calls import get_all_keycap

keycap_routes = Blueprint('keycap', __name__)

@keycap_routes.route('/keycap', methods=["GET", "POST"])
def keyboard():
    if request.method == "GET":
        return get_all_keycap()
    else:
        None