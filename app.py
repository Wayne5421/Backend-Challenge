from flask import Flask, jsonify, request
from dotenv import load_dotenv
from db import init_db
from services.create_user_service import create_user
from services.get_role_by_user_id_service import get_role_by_user_id
from services.get_user_claims_service import get_user_claims


load_dotenv()

app = Flask(__name__)

init_db(app)

@app.route('/user_claims', methods=['GET'])
def user_claims():
    return get_user_claims()

@app.route('/role_by_user_id/<int:user_id>', methods=['GET'])
def role_by_user_id(user_id):
    return get_role_by_user_id(user_id)

@app.route('/create_user', methods=['POST'])
def create_new_user():
    data = request.json
    return create_user(data)

if __name__ == '__main__':
    app.run(debug=True)
