from flask import Blueprint
from controllers.user_controller import UserController
from flask_jwt_extended import jwt_required

user_bp = Blueprint("users", __name__, url_prefix="/api/v1") #GET /api/v1/users Blueprint is used to group related routes together. In this case, it groups all user-related routes under the "/api/v1" prefix. This helps in organizing the code and makes it easier to manage routes for different parts of the application.

controller = UserController()

# ------------------------
# User APIs
# ------------------------

user_bp.get("/users")(jwt_required()(controller.get_users))
user_bp.post("/users")(controller.create_user)
user_bp.put("/users/<int:user_id>")(controller.update_user)
user_bp.patch("/users/<int:user_id>")(controller.patch_user)
user_bp.delete("/users/<int:user_id>")(controller.delete_user)
user_bp.post("/upload/<int:user_id>")(controller.upload_image)
