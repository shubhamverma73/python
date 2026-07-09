import os
from werkzeug.utils import secure_filename
from flask import current_app

from sqlalchemy.exc import SQLAlchemyError
from extensions import db
from schema.user import User
from schema.role import Role


class user_model:

    def get_users_data(self, page, per_page):
        try:
            pagination = User.query.options(db.joinedload(User.user_role)).paginate(page=page, per_page=per_page, error_out=False)
            if not pagination.items:
                return "No users found", 404

            users = pagination.items

            if not users:
                return { "status": "error", "message": "No users found" }, 404

            data = []

            for user in users:
                data.append({
                    "user_id": user.user_id,
                    "name": user.name,
                    "email": user.email,
                    "password": user.password,
                    "profile_image": user.profile_image,
                    "role_id": user.role_id,
                    "role_name": user.user_role.name if user.user_role else None
                })

            pagination = {
                    "current_page": pagination.page,
                    "per_page": pagination.per_page,
                    "total_records": pagination.total,
                    "total_pages": pagination.pages,
                    "has_next": pagination.has_next,
                    "has_prev": pagination.has_prev
                }
            return data, pagination, 200

        except SQLAlchemyError:
            return "Database error", 500


    def create_users_data(self, data):
        try:
            user = User(
                name=data["name"],
                email=data["email"],
                password=data["password"]
            )

            db.session.add(user)
            db.session.commit()

            return "User created successfully", 201

        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 500


    def update_user(self, user_id, data):
        try:
            user = User.query.get(user_id)

            if user is None:
                return "User not found", 404

            user.name = data["name"]
            user.email = data["email"]
            user.password = data["password"]

            db.session.commit()

            return "User updated successfully", 200

        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 500


    def patch_user(self, user_id, data):
        try:
            user = User.query.get(user_id)

            if user is None:
                return "User not found", 404

            if "name" in data:
                user.name = data["name"]

            if "email" in data:
                user.email = data["email"]

            if "password" in data:
                user.password = data["password"]

            db.session.commit()

            return "User updated successfully", 200

        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 500


    def delete_user(self, user_id):
        try:
            user = User.query.get(user_id)

            if user is None:
                return "User not found", 404

            db.session.delete(user)
            db.session.commit()

            return "User deleted successfully", 200

        except SQLAlchemyError as e:
            db.session.rollback()
            return str(e), 500
        

    def upload_image(self, user_id, file):
        try:
            user = User.query.get(user_id)

            if user is None:
                return "User not found", 404

            filename = secure_filename(file.filename)
            extension = filename.rsplit(".", 1)[1].lower()
            filename = f"user_{user_id}.{extension}"

            filepath = os.path.join(
                current_app.config["UPLOAD_FOLDER"],
                filename
            )
            file.save(filepath)
            user.profile_image = filepath
            db.session.commit()

            return { "message": "Image uploaded successfully", "image": filepath }, 200

        except Exception as e:
            db.session.rollback()
            return str(e), 500
