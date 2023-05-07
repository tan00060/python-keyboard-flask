from flask import Flask
from app.config import Config
from flask_migrate import Migrate
from flask_cors import CORS

from .models.db import db
from .api.keyboard_routes import keyboard_routes
from .api.keyboard_type_routes import keyboard_type_routes
from .api.keycap_routes import keycap_routes
from .api.keycap_profile_routes import keycap_profile_routes
from .api.switch_routes import switch_routes
from .api.switch_type_routes import switch_type_routes


app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

app.register_blueprint(keyboard_routes, url_prefix="/api")
app.register_blueprint(keyboard_type_routes, url_prefix="/api")
app.register_blueprint(keycap_routes, url_prefix="/api")
app.register_blueprint(keycap_profile_routes, url_prefix="/api")
app.register_blueprint(switch_routes, url_prefix="/api")
app.register_blueprint(switch_type_routes, url_prefix="/api")

db.init_app(app)
Migrate(app, db)
