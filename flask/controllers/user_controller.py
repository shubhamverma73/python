from extensions import app
from flask import request
from werkzeug.utils import secure_filename
from models.user_model import user_model # here user_model is imported from models/user_model.py

@app.get('/users')
def get_users():
    page = request.args.get('page', default=1, type=int)
    per_page = request.args.get('per_page', default=10, type=int)
    result, pagination, status_code = user_model().get_users_data(page, per_page) # here user_model_function is called to get the user data
    return {'status': 'success', 'message': 'Users data fetched successfully', 'data': result, 'pagination': pagination}, status_code # here user_model_function is called to return the user data

@app.post('/users')
def create_user():
    data = request.get_json()
    result, status_code = user_model().create_users_data(data) # here user_model_function is called to create the user data
    return {'status': 'success', 'message': 'User created successfully', 'data': result}, status_code # here user_model_function is called to return the user data


@app.put('/users/<int:user_id>')
def update_user(user_id):
    data = request.get_json()
    result, status_code = user_model().update_user(user_id, data)
    return {'status': 'success', 'message': 'User updated successfully', 'data': result}, status_code


@app.patch('/users/<int:user_id>')
def patch_user(user_id):
    data = request.get_json()
    result, status_code = user_model().patch_user(user_id, data)
    return {'status': 'success', 'message': 'User updated successfully', 'data': result}, status_code

@app.delete('/users/<int:user_id>')
def delete_user(user_id):
    result, status_code = user_model().delete_user(user_id)
    return {'status': 'success', 'message': 'User deleted successfully', 'data': result}, status_code

@app.post("/upload/<int:user_id>")
def upload_image(user_id):

    if "image" not in request.files:
        return { "status": "error", "message": "No file selected" }, 400

    file = request.files["image"]
    result, status_code = user_model().upload_image(user_id, file)
    return { "status": "success" if status_code == 200 else "error", "data": result }, status_code