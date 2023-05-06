from flask import Blueprint, request, jsonify
from ..api_calls.switch_calls import get_all_switch, create_switch, delete_switch, get_switch_by_id, update_by_id_switch
from ..models.switch import SwitchType

switch_routes = Blueprint('switch', __name__)

@switch_routes.route('/switch', methods=["GET"])
def switch():
    switches = SwitchType.query.all()
    return {"switches": [switch.to_dict() for switch in switches]}

@switch_routes.route('/switch/<int:switch_id>', methods=["GET"])
def get_by_id_switch(switch_id):
        switch = SwitchType.query.get(switch_id)
        return switch.to_dict()

# @switch_routes.route('/switch', methods=["POST"])
# def create_new_switch():
#     if request.method == "POST":
#         res = create_switch(request.json)
#         print(res)
#         return res
#     else:
#         None


# @switch_routes.route('/switch/<switch_id>', methods=["DELETE"])
# def delete_by_id_switch(switch_id):
#     if request.method == "DELETE":
#         res = delete_switch(switch_id)
#         print(res)
#         return res
#     else:
#         None

# @switch_routes.route('/switch/<switch_id>', methods=["PUT"])
# def update_switch(switch_id):
#     if request.method == "PUT":
#         res = update_by_id_switch(switch_id, request.json)
#         print(res)
#         return res
#     else:
#         None

