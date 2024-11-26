from flask import jsonify
from models.user import User
from models.role import Role
from models.claim import Claim
from models.user_claim import UserClaim
from db import db

def get_user_claims():
    try:
        
        try:
            result = db.session.query(
                User.name.label('user_name'),
                User.email.label('user_email'),
                Role.description.label('role_description'),
                Claim.description.label('claim_description')
            ).join(Role, Role.id == User.role_id) \
             .join(UserClaim, UserClaim.user_id == User.id) \
             .join(Claim, Claim.id == UserClaim.claim_id) \
             .all()
        except Exception as e:
            return jsonify({"error": "Error while fetching user claims.", "details": str(e)}), 500

        
        response = []
        for row in result:
            response.append({
                'user_name': row.user_name,
                'user_email': row.user_email,
                'role_description': row.role_description,
                'claim_description': row.claim_description
            })

        return jsonify(response)

    except Exception as e:
        
        return jsonify({"error": "An unexpected error occurred while processing user claims.", "details": str(e)}), 500
