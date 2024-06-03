from flask import Blueprint, request, jsonify, g
from app.models.user import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/profile', methods=['GET', 'PUT'])
def user_profile():
    user = g.user  # Assuming you have a middleware that sets the authenticated user in the g object

    if request.method == 'GET':
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })
    elif request.method == 'PUT':
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({
            'id': user.id,
            'username': user.username,
            'email': user.email
        })

