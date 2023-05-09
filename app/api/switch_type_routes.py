from flask import Blueprint
from ..models.db import db
from ..models.switch_type import SwitchType
from sqlalchemy.exc import SQLAlchemyError


switch_type_routes = Blueprint('switch_type', __name__)

@switch_type_routes.route('/switch-type', methods=["GET"])
def get_switch_type():
    try:
        switch_types = SwitchType.query.all();
        switch_type_list = [{"id": type.id, "switch_type": type.switch_type} for type in switch_types]
        return switch_type_list
    except SQLAlchemyError as e:
        db.session.rollback()
        return {'errors': ['An error occurred']}, 500
