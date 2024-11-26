from flask import Blueprint, jsonify, request
from services.create_user_service import create_user

create_user_route = Blueprint('create_user_route', __name__)

@create_user_route.route('/create_user', methods=['POST'])
def create_new_user():
    try:
        data = request.json
        
        return create_user(data)
    
    except Exception as e:
        
        return jsonify({"error": "Error creating user", "message": str(e)}), 400