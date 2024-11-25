from flask import Blueprint
from services.get_role_by_user_id_service import get_role_by_user_id

get_role_by_user_id_route = Blueprint('get_role_by_user_id_route', __name__)

@get_role_by_user_id_route.route('/role_by_user_id/<int:user_id>', methods=['GET'])
def role_by_user_id(user_id):
    return get_role_by_user_id(user_id)
