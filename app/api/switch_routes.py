from flask import Blueprint, request
from ..api_calls.switch_calls import get_all_switch, create_switch

switch_routes = Blueprint('switch', __name__)

@switch_routes.route('/switch', methods=["GET"])
def switch():
    if request.method == "GET":
        return get_all_switch()
    else:
        None


@switch_routes.route('/switch', methods=["POST"])
def create_new_switch():
    if request.method == "POST":
        print(request.json)
        create_switch(request.json)
        return "ctreate"
    else:
        None