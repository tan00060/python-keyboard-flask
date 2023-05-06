from flask import Flask, request, jsonify
from ..api.keyboard import get_all_keyboard
from app import app


@app.route('/keyboard', methods=["GET", "POST"])
def keyboard():
    if request.method == "GET":
        return get_all_keyboard()
    else:
        None