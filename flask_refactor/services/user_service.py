import os
import time
from flask import current_app
from werkzeug.utils import secure_filename
from extensions import bcrypt

from extensions import db
from models.user import User


class UserService:
    # ----------------------------------
    # GET USERS
    # ----------------------------------

    def get_users(self, page, per_page):
        pagination = User.query.paginate(page=page, per_page=per_page, error_out=False)
        users = [user.to_dict() for user in pagination.items]

        return {
            "users": users,
            "pagination": {
                "page": pagination.page,
                "per_page": pagination.per_page,
                "total_records": pagination.total,
                "total_pages": pagination.pages,
                "has_next": pagination.has_next,
                "has_prev": pagination.has_prev
            },
        }, 200

    # ----------------------------------
    # CREATE USER
    # ----------------------------------

    def create_user(self, data):
        try:
            name = data.get("name")
            email = data.get("email")
            password = data.get("password")
            role_id = data.get("role_id")

            if not name or not email or not password or not role_id:
                return {"message": "All fields are required"}, 400

            existing_user = User.query.filter_by(email=email).first()

            if existing_user:
                return {"message": "Email already exists"}, 409

            user = User(name=name, email=email, password=bcrypt.generate_password_hash(password).decode("utf-8"), role_id=role_id)

            db.session.add(user)
            db.session.commit()
            return user.to_dict(), 201

        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    # ----------------------------------
    # UPDATE USER
    # ----------------------------------

    def update_user(self, user_id, data):
        try:
            user = db.session.get(User, user_id)

            if not user:
                return {"message": "User not found"}, 404

            user.name = data.get("name")
            user.email = data.get("email")
            user.password = bcrypt.generate_password_hash(data.get("password")).decode("utf-8")
            user.role_id = data.get("role_id")

            db.session.commit()
            return user.to_dict(), 200

        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    # ----------------------------------
    # PATCH USER
    # ----------------------------------

    def patch_user(self, user_id, data):
        try:
            user = db.session.get(User, user_id)

            if not user:
                return {"message": "User not found"}, 404

            if "name" in data:
                user.name = data["name"]

            if "email" in data:
                user.email = data["email"]

            if "password" in data:
                user.password = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

            if "role_id" in data:
                user.role_id = data["role_id"]

            db.session.commit()
            return user.to_dict(), 200

        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    # ----------------------------------
    # DELETE USER
    # ----------------------------------

    def delete_user(self, user_id):
        try:
            user = db.session.get(User, user_id)

            if not user:
                return {"message": "User not found"}, 404

            db.session.delete(user)
            db.session.commit()
            return {"message": "User deleted successfully"}, 200

        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500

    # ----------------------------------
    # IMAGE UPLOAD
    # ----------------------------------

    def upload_image(self, user_id, file):
        try:
            user = db.session.get(User, user_id)

            if not user:
                return {"message": "User not found"}, 404

            filename = secure_filename(file.filename)
            extension = os.path.splitext(filename)[1]
            new_filename = f"user_{user_id}_{int(time.time())}{extension}"            
            upload_folder = current_app.config["UPLOAD_FOLDER"]
            os.makedirs(upload_folder, exist_ok=True)
            filepath = os.path.join(upload_folder, new_filename)
            file.save(filepath)
            user.profile_image = filepath

            db.session.commit()
            return user.to_dict(), 200

        except Exception as e:
            db.session.rollback()
            return {"message": str(e)}, 500
