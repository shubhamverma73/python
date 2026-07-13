from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


'''
This page is used for:
    Objects for all Flask extensions are created in a single place.

Benifit of this page:
    Single Source of Truth:
        All extensions in a single file.

    Circular import avoid:
        This is a very common problem with flasks.

    Easy maintenance:
        Easy to maintain and update extensions in a single place.

So:
    Remember this in a nutshell:
        Role of `extensions.py`: To create shared instances of Flask extensions (db, bcrypt, jwt, mail, etc.) in one place.
        Role of `app.py`: To initialize those instances with the Flask application using `init_app(app)`.
        Role of the rest of the project: Simply use those same shared instances by importing them (e.g., `from extensions import db` or `bcrypt`).
'''