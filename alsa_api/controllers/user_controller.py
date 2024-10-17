# alsa_api/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from ..models.user import db, User, Profile  # Use relative import to access db, User, Profile

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/v1/signin', methods=['POST'])
def sign_in():
    data = request.get_json()

    # Validate input data
    if not data or not all(k in data for k in ('name', 'email', 'country', 'age', 'contact')):
        return jsonify({'message': 'Missing data'}), 400

    # Create a new user instance
    new_user = User(
        name=data['name'],
        email=data['email'],
        country=data['country'],
        age=data['age'],
        contact=data['contact']
    )

    # Add the user to the database
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        'message': 'User signed in successfully!',
        'user': {
            'id': new_user.id,
            'name': new_user.name,
            'email': new_user.email,
            'country': new_user.country,
            'age': new_user.age,
            'contact': new_user.contact
        }
    }), 201
