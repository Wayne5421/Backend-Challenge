from flask import Flask
from dotenv import load_dotenv
from db import init_db

from routes.create_user_route import create_user_route
from routes.get_role_by_user_id_route import get_role_by_user_id_route
from routes.get_user_claims_route import get_user_claims_route

load_dotenv()

app = Flask(__name__)

init_db(app)

app.register_blueprint(create_user_route, url_prefix='/api')
app.register_blueprint(get_role_by_user_id_route, url_prefix='/api')
app.register_blueprint(get_user_claims_route, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
