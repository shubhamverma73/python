from flask import request

from utils.response import success_response, error_response
from services.auth_service import login_user, get_current_user, logout_user

def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return error_response("Email and password are required", 400)
    
    result, status_code = login_user(email, password)
    if status_code != 200:
        return error_response(message=result["message"], status_code=status_code)

    return success_response( message= "Login successful", data= result, status_code= status_code )
    

def profile():
    result, status_code = get_current_user()

    if status_code != 200:
        return error_response(message=result["message"], status_code=status_code)
    
    return success_response(message="Profile retrieved successfully", data=result, status_code=status_code)

def logout():
    logout_user()
    return success_response(message="Logout successful", status_code=200)