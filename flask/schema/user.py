from extensions import db


class User(db.Model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey("roles.role_id"))
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    profile_image = db.Column(db.String(255), nullable=True)
    user_role = db.relationship("Role", back_populates="users_data") # yahi relationship hai jo aapko manual join se bachayega