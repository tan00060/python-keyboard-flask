from flask import Blueprint, request, jsonify, session
from ..models.db import db
from ..models.switch_type import SwitchType
from ..models.switch import Switch
from flask_login import current_user, login_user, logout_user, login_required
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
    user_id = session['id']
    data = request.json
    switch = Switch(
        # can also do Switch(**data)
        user_id = user_id,
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


@switch_routes.route('/switch/<switch_id>', methods=["DELETE"])
def delete_by_id_switch(switch_id):
    switch = Switch.query.get(switch_id)
    if switch:
        db.session.delete(switch)
        db.session.commit()
        return {'message': f'switch Id: {switch_id} was successfully deleted'}
    else:
        return {'errors': [f'Switch Id: {switch_id} was not found']}


@switch_routes.route('/switch/<switch_id>', methods=["PUT"])
def update_switch(switch_id):
    try:
        switch = Switch.query.get(switch_id)
        if not switch:
            return jsonify({'error': 'Switch not found'}), 404
        
        data = request.json

        if 'switch_name' in data:
            switch.switch_name = data["switch_name"]

        db.session.commit()
        return {'message': f'switch Id: {switch_id} was successfully updated'}

    except SQLAlchemyError as e:
        error = str(e.__dict__['orig'])
        db.session.rollback()
        return {'errors': ['An error occurred while updating data']}, 500


