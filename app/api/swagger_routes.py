from flask import Blueprint, request, session, jsonify
from ..models.db import db
from flask_login import current_user, login_user, logout_user, login_required
from sqlalchemy.exc import SQLAlchemyError
from flask_swagger_ui import get_swaggerui_blueprint

swagger_routes = Blueprint('swagger', __name__)


SWAGGER_URL = '/api/swagger'  # URL for exposing Swagger UI (without trailing '/')
API_URL = 'http://petstore.swagger.io/v2/swagger.json'  # Our API url (can of course be a local resource)

# Call factory function to create our blueprint
def swagger():
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL,  # Swagger UI static files will be mapped to '{SWAGGER_URL}/dist/'
        API_URL,
        config={  # Swagger UI config overrides
            'app_name': "Test application"
    })
    return swaggerui_blueprint