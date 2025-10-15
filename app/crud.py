# app/crud.py
import datetime
import secrets
from sqlalchemy.orm import Session
from . import models, schemas, auth

# Users
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, email=user.email, hashed_password=hashed)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Todos
def create_todo(db: Session, todo: schemas.ToDoCreate, user_id: int):
    db_todo = models.ToDo(**todo.dict(), owner_id=user_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo








def get_todos_for_user(db: Session, user_id: int):
    return db.query(models.ToDo).filter(models.ToDo.owner_id == user_id).all()

def get_todo_for_user(db: Session, todo_id: int, user_id: int):
    return db.query(models.ToDo).filter(models.ToDo.id == todo_id, models.ToDo.owner_id == user_id).first()

def update_todo(db: Session, todo_obj, data: dict):
    for k, v in data.items():
        setattr(todo_obj, k, v)
    db.add(todo_obj)
    db.commit()
    db.refresh(todo_obj)
    return todo_obj

def delete_todo(db: Session, todo_obj):
    db.delete(todo_obj)
    db.commit()
    return True

# Refresh tokens
def create_refresh_token(db: Session, user_id: int):
    token = secrets.token_urlsafe(48)
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(days=auth.REFRESH_TOKEN_EXPIRE_DAYS)
    db_token = models.RefreshToken(token=token, user_id=user_id, expires_at=expires_at)
    db.add(db_token)
    db.commit()
    db.refresh(db_token)
    return db_token

def get_refresh_token(db: Session, token: str):
    return db.query(models.RefreshToken).filter(models.RefreshToken.token == token).first()

def revoke_refresh_token(db: Session, token_obj):
    token_obj.revoked = True
    db.add(token_obj)
    db.commit()
    db.refresh(token_obj)
    return token_obj
