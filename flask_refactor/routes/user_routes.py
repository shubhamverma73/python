from flask import Blueprint
from controllers.user_controller import UserController

user_bp = Blueprint("users", __name__, url_prefix="/api/v1") #GET /api/v1/users

controller = UserController()

# ------------------------
# User APIs
# ------------------------

controller = UserController()
user_bp.get("/users")(controller.get_users)
user_bp.post("/users")(controller.create_user)
user_bp.put("/users/<int:user_id>")(controller.update_user)
user_bp.patch("/users/<int:user_id>")(controller.patch_user)
user_bp.delete("/users/<int:user_id>")(controller.delete_user)
user_bp.post("/upload/<int:user_id>")(controller.upload_image)
