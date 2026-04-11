from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user_schema import UserCreate
from app.crud import user_crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users")
def create(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

@router.get("/users")
def read_all(db: Session = Depends(get_db)):
    return user_crud.get_users(db)

@router.get("/users/{user_id}")
def read_one(user_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user(db, user_id)

@router.put("/users/{user_id}")
def update(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.update_user(db, user_id, user)

@router.delete("/users/{user_id}")
def delete(user_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user(db, user_id)