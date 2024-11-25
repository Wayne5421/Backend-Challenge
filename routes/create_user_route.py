from flask import Blueprint, request
from services.create_user_service import create_user

create_user_route = Blueprint('create_user_route', __name__)

@create_user_route.route('/create_user', methods=['POST'])
def create_new_user():
    data = request.json
    return create_user(data)
