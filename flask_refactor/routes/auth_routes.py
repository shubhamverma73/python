from flask import Blueprint
from controllers.auth_controller import login, logout, profile
from flask_jwt_extended import jwt_required

auth_bp = Blueprint("auth", __name__, url_prefix="/api/v1") #GET /api/v1/auth

# ------------------------
# Auth APIs
# ------------------------

auth_bp.post("/login")(login)
auth_bp.get("/profile")(jwt_required()(profile))
auth_bp.post("/logout")(jwt_required()(logout))