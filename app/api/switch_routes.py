from flask import Blueprint, request, jsonify
from ..api_calls.switch_calls import get_all_switch, create_switch, delete_switch, get_switch_by_id, update_by_id_switch
from ..models.db import db
from ..models.switch_type import SwitchType
from ..models.switch import Switch
from sqlalchemy.exc import SQLAlchemyError

switch_routes = Blueprint('switch', __name__)

@switch_routes.route('/switch', methods=["GET"])
def switch():
    switches = db.session.query(Switch, SwitchType).join(SwitchType, Switch.switch_type_id == SwitchType.id).all()
    switch_list = [{"id": switch.Switch.id,"Switch": switch.Switch.switch_name, "SwitchType": switch.SwitchType.switch_type} for switch in switches]
    return switch_list

@switch_routes.route('/switch/<int:switch_id>', methods=["GET"])
def get_by_id_switch(switch_id):
        switch = Switch.query.get(switch_id)
        return switch.to_dict()

@switch_routes.route('/switch', methods=["POST"])
def create_new_switch():
    data = request.json
    switch = Switch(
        switch_name = data["switch_name"],
        switch_type_id = data["switch_type_id"]
    )
    try:
        db.session.add(switch)
        db.session.commit()
        switch_json = jsonify({'switch': switch.to_dict()})
        return switch_json
    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while creating data']}, 500

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

