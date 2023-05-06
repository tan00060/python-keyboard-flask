from flask import Flask, request, jsonify

# from app.config import Config
from routes.keyboard import get_all_keyboard

app = Flask(__name__)
# app.config.from_object(Config)

@app.route('/keyboard', methods=["GET", "POST"])
def keyboard():
    if request.method == "GET":
        return get_all_keyboard()
    else:
        None




