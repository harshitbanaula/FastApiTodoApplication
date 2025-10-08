# app/routers/auth_router.py
import datetime
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, crud, database, auth

router = APIRouter(prefix="/auth", tags=["auth"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if crud.get_user_by_username(db, user.username) or crud.get_user_by_email(db, user.email):
        raise HTTPException(status_code=400, detail="Username or email already registered")
    db_user = crud.create_user(db, user)
    return db_user

@router.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = auth.create_access_token(subject=str(user.id))
    refresh_row = crud.create_refresh_token(db, user.id)
    return {"access_token": access_token, "refresh_token": refresh_row.token, "token_type": "bearer"}

@router.post("/refresh", response_model=schemas.Token)
def refresh_token(payload: schemas.TokenRefreshIn, db: Session = Depends(get_db)):
    token_row = crud.get_refresh_token(db, payload.refresh_token)
    if not token_row or token_row.revoked or token_row.expires_at < datetime.datetime.utcnow():
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or expired refresh token")
    crud.revoke_refresh_token(db, token_row)
    new_refresh = crud.create_refresh_token(db, token_row.user_id)
    access_token = auth.create_access_token(subject=str(token_row.user_id))
    return {"access_token": access_token, "refresh_token": new_refresh.token, "token_type": "bearer"}

@router.post("/logout")
def logout(payload: schemas.TokenRefreshIn, db: Session = Depends(get_db)):
    token_row = crud.get_refresh_token(db, payload.refresh_token)
    if token_row:
        crud.revoke_refresh_token(db, token_row)
    return {"ok": True, "message": "Logged out"}
