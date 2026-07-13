from extensions import db


class Role(db.Model):

    __tablename__ = "roles"

    role_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    users_data = db.relationship("User", back_populates="user_role") # ye reverse relationship hai, Role se saare users nikalne ke liye (optional)
