from flask import Blueprint, request
from ..api_calls.switch_calls import get_all_switch

switch_routes = Blueprint('switch', __name__)

@switch_routes.route('/switch', methods=["GET", "POST"])
def switch():
    if request.method == "GET":
        return get_all_switch()
    else:
        None