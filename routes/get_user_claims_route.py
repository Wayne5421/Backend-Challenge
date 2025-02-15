from flask import Blueprint, jsonify
from services.get_user_claims_service import get_user_claims

get_user_claims_route = Blueprint('get_user_claims_route', __name__)

@get_user_claims_route.route('/user_claims', methods=['GET'])
def user_claims():
    
    try:
        
        return get_user_claims()
    
    except Exception as e:
        
        return jsonify({"error": "Error getting user claims", "message": str(e)}), 400
