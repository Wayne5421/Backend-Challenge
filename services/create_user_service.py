from flask import jsonify
from models.user import User
from models.role import Role
from models.claim import Claim
from models.user_claim import UserClaim
from db import db
from services.generate_password_service import generate_password


# Função para criar um usuário
def create_user(data):
    if 'name' not in data or 'email' not in data or 'role_id' not in data:
        return jsonify({"error": "Missing required fields: name, email, role_id"}), 400

    name = data['name']
    email = data['email']
    role_id = data['role_id']
    
    # Verificação se o papel (role) existe
    role = db.session.query(Role).filter_by(id=role_id).first()
    if not role:
        return jsonify({"error": f"Role with ID {role_id} not found"}), 404
    
    password = data.get('password', generate_password())
    
    # Criar o novo usuário
    new_user = User(
        name=name,
        email=email,
        password=password,
        role_id=role_id,
        created_at=db.func.current_date()
    )
    
    try:
        db.session.add(new_user)
        db.session.flush()  # Garante que o ID do usuário será gerado antes de associá-lo a uma claim
        
        claim = db.session.query(Claim).first()  # Selecione a primeira claim disponível
        
        if claim:
            user_claim = UserClaim(user_id=new_user.id, claim_id=claim.id)
            db.session.add(user_claim)
        
        db.session.commit()
        
        return jsonify({
            "message": "User created successfully",
            "user_id": new_user.id,
            "user_name": new_user.name,
            "user_email": new_user.email,
            "role_description": role.description
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": "Error creating user", "error": str(e)}), 500
