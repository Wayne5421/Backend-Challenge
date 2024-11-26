from flask import jsonify
from models.user import User
from models.role import Role
from models.claim import Claim
from models.user_claim import UserClaim
from db import db
from services.generate_password_service import generate_password

def create_user(data):
    try:
        
        if 'name' not in data or 'email' not in data or 'role_id' not in data:
            return jsonify({"error": "Oops! Looks like you're missing some fields: name, email, or role_id."}), 400

        name = data['name']
        email = data['email']
        role_id = data['role_id']

        
        try:
            role = db.session.query(Role).filter_by(id=role_id).first()
        except Exception as e:
            return jsonify({"error": "Hmm, something went wrong while looking up the role.", "details": str(e)}), 500

        if not role:
            return jsonify({"error": f"Sorry, we couldn't find a role with ID {role_id}."}), 404

        password = data.get('password', generate_password())

        new_user = User(
            name=name,
            email=email,
            password=password,
            role_id=role_id,
            created_at=db.func.current_date()
        )
        
        try:
            db.session.add(new_user)
            db.session.flush()  
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "We hit a snag while saving the new user to the database.", "details": str(e)}), 500
        
        try:
            claim = db.session.query(Claim).filter_by(id=role_id).first()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Something went wrong while fetching the correct claim.", "details": str(e)}), 500

        if claim:
            
            try:
                user_claim = UserClaim(user_id=new_user.id, claim_id=claim.id)
                db.session.add(user_claim)
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": "Couldn't link the claim to the user. Let's check what went wrong.", "details": str(e)}), 500

        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": "Couldn't save changes to the database. Something's off.", "details": str(e)}), 500

        
        return jsonify({
            "message": "User created successfully!",
            "user_id": new_user.id,
            "user_name": new_user.name,
            "user_email": new_user.email,
            "role_description": role.description
        }), 201

    except Exception as e:
        return jsonify({"error": "Sorry, something unexpected happened. Let's take a closer look.", "details": str(e)}), 500
