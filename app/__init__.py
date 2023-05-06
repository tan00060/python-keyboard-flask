from flask import Flask
from app.config import Config
from .api.keyboard_routes import keyboard_routes
from .api.switch_routes import switch_routes
from .api.keycap_routes import keycap_routes


app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(keyboard_routes, url_prefix="/api")
app.register_blueprint(switch_routes, url_prefix="/api")
app.register_blueprint(keycap_routes, url_prefix="/api")


