from sqlalchemy.orm import Session
from app.models.user_model import User

def create_user(db: Session, user):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.user_id == user_id).first()

def update_user(db: Session, user_id: int, user):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.user_id == user_id).first()
    db.delete(db_user)
    db.commit()