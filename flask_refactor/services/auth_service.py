from flask_jwt_extended import create_access_token, get_jwt_identity
from flask_jwt_extended import get_jwt
from utils.token_blocklist import BLOCKLIST

from extensions import bcrypt
from models.user import User
from extensions import db

def login_user(email, password):
    user = User.query.filter_by(email=email).first()
    
    if not user:
        return {"message": "Invalid email or password"}, 401

    if not bcrypt.check_password_hash(user.password, password):
        return {"message": "Invalid email or password"}, 401
    
    # if not user or not bcrypt.check_password_hash(user.password, password):
    #     return {"message": "Invalid email or password"}, 401

    access_token = create_access_token(identity=str(user.user_id))
    return {"access_token": access_token}, 200


def get_current_user():
    user_id = get_jwt_identity()
    user = db.session.get(User, int(user_id))

    if not user:
        return {"message": "User not found"}, 404

    #return user.to_dict(), 200 # later will enable this line and remove the below line to return only specific fields
    return {
        "user_id": user.user_id,
        "name": user.name,
        "email": user.email,
        "profile_image": user.profile_image
    }, 200


def logout_user():
    jti = get_jwt()["jti"]

    BLOCKLIST.add(jti)

    return {"message": "Logout successful"}, 200