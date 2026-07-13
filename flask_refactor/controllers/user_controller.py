from flask import request

from services.user_service import UserService
from utils.response import success_response, error_response


class UserController:
    def __init__(self):
        self.user_service = UserService()

    # ----------------------------------
    # GET USERS
    # ----------------------------------

    def get_users(self):
        page = request.args.get("page", 1, type=int)
        per_page = request.args.get("per_page", 10, type=int)
        
        result, status = self.user_service.get_users(page, per_page)

        return success_response(
            message="Users fetched successfully",
            data=result["users"],
            pagination=result["pagination"],
            status_code=status,
        )

    # ----------------------------------
    # CREATE USER
    # ----------------------------------

    def create_user(self):
        result, status = self.user_service.create_user(request.get_json())

        if status != 201:
            return error_response(result["message"], status)
        return success_response( message="User created successfully", data=result, status_code=status )

    # ----------------------------------
    # UPDATE USER
    # ----------------------------------

    def update_user(self, user_id):
        result, status = self.user_service.update_user(user_id, request.get_json())

        if status != 200:
            return error_response(result["message"], status)
        return success_response(message="User updated successfully", data=result)

    # ----------------------------------
    # PATCH USER
    # ----------------------------------

    def patch_user(self, user_id):
        result, status = self.user_service.patch_user(user_id, request.get_json())

        if status != 200:
            return error_response(result["message"], status)
        return success_response(message="User updated successfully", data=result)

    # ----------------------------------
    # DELETE USER
    # ----------------------------------

    def delete_user(self, user_id):
        result, status = self.user_service.delete_user(user_id)

        if status != 200:
            return error_response(result["message"], status)
        return success_response(message=result["message"], status_code=status)

    # ----------------------------------
    # IMAGE UPLOAD
    # ----------------------------------

    def upload_image(self, user_id):
        if "image" not in request.files:
            return error_response("No image selected", 400)
        
        result, status = self.user_service.upload_image(user_id, request.files["image"])

        if status != 200:
            return error_response(result["message"], status)
        return success_response(message="Image uploaded successfully", data=result)
