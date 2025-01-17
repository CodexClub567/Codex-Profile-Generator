from flask import Blueprint, request, jsonify
from .models import db, User, Profile
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('routes', __name__)

@bp.route('/register', methods=['POST'])
def register_user():
    data = request.json
    email = data['email']
    password = data['password']
    user = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.json
    email = data['email']
    password = data['password']
    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        # Generate a session token (for simplicity, returning a dummy token here)
        return jsonify({"token": "dummy-session-token"}), 200
    return jsonify({"message": "Invalid credentials"}), 401

@bp.route('/logout', methods=['POST'])
def logout_user():
    token = request.json.get('token')
    # Invalidate the token (for simplicity, returning success here)
    return jsonify({"message": "User logged out"}), 200