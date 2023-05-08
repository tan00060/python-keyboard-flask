from flask import Blueprint, jsonify, session, request
from ..models.user import User
from ..models.db import db
from ..form.signup_form import SignupForm
from flask_login import current_user, login_user, logout_user, login_required

signup_routes = Blueprint('signup', __name__)

@signup_routes.route('/signup', methods=['POST'])
def signup():
    data = request.json
    form = SignupForm(**data)
    form['csrf_token'].data = request.cookies['csrf_token']

    if form.validate_on_submit():
        user = User.query.filter(User.email == form.data['email']).first()
        if not user:
            new_user = User(**data)
            db.session.add(new_user)
            db.session.commit()
            user_dict = {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email
            }
            print(new_user)
            return {'message': 'User created successfully', 'user': user_dict}
        else:
            return {'errors': ['User already exists']}
    else:
        print(form.errors)
        return {'errors': form.errors}, 401

