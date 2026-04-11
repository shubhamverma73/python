from flask import Flask, jsonify, request
from resources.item import blp as ItemBlueprint
from flask_smorest import Api

# Create Flask app
app = Flask(__name__)
app.config["API_TITLE"] = "Items API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.2"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
api = Api(app)
api.register_blueprint(ItemBlueprint)

# Run the Flask app
if __name__ == "__main__":
    app.run(port=5000, debug=True)
