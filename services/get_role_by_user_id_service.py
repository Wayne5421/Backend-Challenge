from flask import jsonify
from models.user import User
from models.role import Role
from db import db

def get_role_by_user_id(user_id):
    try:
        
        try:
            user = db.session.query(User).filter_by(id=user_id).first()
        except Exception as e:
            return jsonify({"error": f"Something went wrong while trying to find the user with ID {user_id}.", "details": str(e)}), 500

        if user is None:
            return jsonify({"error": f"Sorry, couldn't find a user with ID {user_id}."}), 404


        try:
            role = db.session.query(Role).filter_by(id=user.role_id).first()
        except Exception as e:
            return jsonify({"error": f"An error occurred while looking up the role for user with ID {user_id}.", "details": str(e)}), 500

        if role is None:
            return jsonify({"error": f"No role found for the user with ID {user_id}."}), 404
        
        return jsonify({
            'user_id': user.id,
            'user_name': user.name,
            'role': role.id,
            'role_description': role.description
        })

    except Exception as e:
        
        return jsonify({"error": "An unexpected error occurred while processing the request.", "details": str(e)}), 500
