from flask import Blueprint, request
from ..api_calls.switch_calls import get_all_switch, create_switch, delete_switch, get_switch_by_id

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
        res = create_switch(request.json)
        print(res)
        return res
    else:
        None

@switch_routes.route('/switch/<switch_id>', methods=["GET"])
def get_by_id_switch(switch_id):
    if request.method == "GET":
        res = get_switch_by_id(switch_id)
        print(res)
        return res
    else:
        None
        
@switch_routes.route('/switch/<switch_id>', methods=["DELETE"])
def delete_by_id_switch(switch_id):
    if request.method == "DELETE":
        res = delete_switch(switch_id)
        print(res)
        return res
    else:
        None
