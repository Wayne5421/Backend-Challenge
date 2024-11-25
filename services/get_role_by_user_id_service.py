from flask import jsonify
from models.user import User
from models.role import Role
from db import db

def get_role_by_user_id(user_id):
    user = db.session.query(User).filter_by(id=user_id).first()
    
    if user is None:
        return jsonify({"error": f"User with ID {user_id} not found"}), 404

    role = db.session.query(Role).filter_by(id=user.role_id).first()

    if role is None:
        return jsonify({"error": f"Role for user with ID {user_id} not found"}), 404
    
    return jsonify({
        'user_id': user.id,
        'user_name': user.name,
        'role': role.id,
        'role_description': role.description
    })
