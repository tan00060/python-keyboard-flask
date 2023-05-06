from flask import Flask, request, jsonify
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from .routes.keyboard_route import keyboard
from .routes.switch_route import switch


