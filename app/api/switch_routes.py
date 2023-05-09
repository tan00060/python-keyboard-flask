from flask import Blueprint, request, jsonify, session
from ..models.db import db
from ..models.switch_type import SwitchType
from ..models.switch import Switch
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError


switch_routes = Blueprint('switch', __name__)


@switch_routes.route('/switch', methods=["GET"])
@login_required
def switch():
    user_id = session['id']
    try:
        switches = db.session.query(Switch, SwitchType).join(SwitchType, Switch.switch_type_id == SwitchType.id).filter(Switch.user_id == user_id).all()
        switch_list = [{"id": switch.Switch.id,"Switch": switch.Switch.switch_name, "SwitchType": switch.SwitchType.switch_type} for switch in switches]
        return switch_list
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

@switch_routes.route('/switch/<int:switch_id>', methods=["GET"])
def get_by_id_switch(switch_id):
    switch = Switch.query.get(switch_id)
    user_id = session['id']
    try:
        if switch:
            if switch.user_id == user_id:
                return switch.to_dict(), 200 
            else:
                return {'errors': [f'switch ID: {switch_id} was not found']}, 404 
        else:
            return {'errors': [f'switch ID: {switch_id} was not found']}, 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

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
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500

@switch_routes.route('/switch/<switch_id>', methods=["DELETE"])
@login_required
def delete_by_id_switch(switch_id):
    user_id = session['id']
    switch = Switch.query.get(switch_id)
    try:
        if switch:
            if user_id == switch.user_id:
                db.session.delete(switch)
                db.session.commit()
                return {'message': f'switch Id: {switch_id} was successfully deleted'}
            else: {'errors': [f'Switch Id: {switch_id} was not found']}, 404
        else:
            return {'errors': [f'Switch Id: {switch_id} was not found']}, 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500


@switch_routes.route('/switch/<switch_id>', methods=["PUT"])
@login_required
def update_switch(switch_id):
    user_id = session['id']
    switch = Switch.query.get(switch_id)
    data = request.json
    try:
        if switch:
            if switch.user_id == user_id:
                if 'switch_name' in data:
                    switch.switch_name = data["switch_name"]
                db.session.add(switch)
                db.session.commit()
                return {'message': f'switch Id: {switch_id} was successfully updated'}
            else:
                return{'errors': [f'Switch Id: {switch_id} was not found']}, 404
        else:
            return {'errors': [f'Switch Id: {switch_id} was not found']}, 404
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500


