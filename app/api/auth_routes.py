from flask import Blueprint, jsonify, session, request
from ..models.user import User
from ..models.db import db
from ..form.login_form import LoginForm
from flask_login import current_user, login_user, logout_user, login_required

#maybe add jwt token??

auth_routes = Blueprint('auth', __name__)

@auth_routes.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()
        session['id'] = user.id
        login_user(user)
        return user.to_dict()
    else:
        print(form.errors)
        return {'errors': "unauthorzed"}, 401


# log the user ou of the session
@auth_routes.route('/logout', methods=["POST"])
def logout():
    session.clear()
    logout_user()
    return "logout"