from flask import Blueprint, request

keyboard_routes = Blueprint('keyboard', __name__)

@keyboard_routes.route('/keyboard', methods=["GET", "POST"])
def keyboard():
    pass


@keyboard_routes.route('/keyboard/<keyboard_id>', methods=["GET"])
def keyboard_by_id(keyboard_id):
    pass
