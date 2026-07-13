from flask import Flask
from flask_cors import CORS

from config import Config
from extensions import db, bcrypt, jwt

from routes import register_routes
from middleware.error_handler import register_error_handlers

from utils.logger import setup_logger
import logging

from routes.auth_routes import auth_bp
from utils.response import error_response
from utils.token_blocklist import BLOCKLIST

setup_logger()
logger = logging.getLogger(__name__)
logger.info("Flask application started.")

def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    app.register_blueprint(auth_bp)

    CORS(app)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # ----------------------------------
    # Blocklist Check before call Route
    # ----------------------------------
    @jwt.token_in_blocklist_loader
    def check_if_token_revoked(jwt_header, jwt_payload):
        jti = jwt_payload["jti"]
        print(f"Checking if token is revoked: {jti} in BLOCKLIST: {BLOCKLIST}")
        return jti in BLOCKLIST

    register_routes(app)

    register_error_handlers(app)

    with app.app_context():
        db.create_all()        

    # ------------------------
    # Handle JWT Errors
    # ------------------------
    @jwt.unauthorized_loader
    def unauthorized_callback(error):
        return error_response(message="Authorization token is missing", status_code=401)


    @jwt.invalid_token_loader
    def invalid_token_callback(error):
        return error_response(message="Invalid authentication token", status_code=401)


    @jwt.expired_token_loader
    def expired_token_callback(jwt_header, jwt_payload):
        return error_response(message="Token has expired", status_code=401)

    # This decorator registers a callback function that will be called when a revoked token is used to access a protected route. The callback function will return an error response indicating that the token has been revoked. That will execute after check "token_in_blocklist_loader" function.
    @jwt.revoked_token_loader
    def revoked_token_callback(jwt_header, jwt_payload):
        return error_response(message="Token has been revoked", status_code=401)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
