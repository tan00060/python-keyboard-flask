from flask import Flask, request, jsonify
from ..api.switch_api import get_all_switch
from app import app


@app.route('/switch', methods=["GET", "POST"])
def switch():
    if request.method == "GET":
        return get_all_switch()
    else:
        None