import os
from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask_cors import CORS
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect, generate_csrf


from .models.db import db
from .api.keyboard_routes import keyboard_routes
from .api.keyboard_type_routes import keyboard_type_routes
from .api.keycap_routes import keycap_routes
from .api.keycap_profile_routes import keycap_profile_routes
from .api.switch_routes import switch_routes
from .api.switch_type_routes import switch_type_routes
from .api.auth_routes import auth_routes
from .api.signup_routes import signup_routes

from .models.user import User

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

login = LoginManager(app)
login.login_view = "session.login"

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


app.register_blueprint(keyboard_routes, url_prefix="/api")
app.register_blueprint(keyboard_type_routes, url_prefix="/api")
app.register_blueprint(keycap_routes, url_prefix="/api")
app.register_blueprint(keycap_profile_routes, url_prefix="/api")
app.register_blueprint(switch_routes, url_prefix="/api")
app.register_blueprint(switch_type_routes, url_prefix="/api")
app.register_blueprint(auth_routes, url_prefix="/api")
app.register_blueprint(signup_routes, url_prefix="/api")

db.init_app(app)
Migrate(app, db)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie('csrf_token',
                        generate_csrf(),
                        secure=True if os.environ.get(
                            'FLASK_ENV') == 'production' else False,
                        samesite='Strict' if os.environ.get(
                            'FLASK_ENV') == 'production' else None,
                        httponly=True)
    return response