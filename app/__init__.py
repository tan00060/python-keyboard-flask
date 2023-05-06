from flask import Flask, request, jsonify

app = Flask(__name__)

from .routes.keyboard_route import keyboard


