# app/main.py
from fastapi import FastAPI, Depends
from .routers import auth_router, todo_router  
from fastapi.security import OAuth2PasswordBearer

# import all routers

app = FastAPI(title="ToDo API", version="0.1.0")

# Include routers
app.include_router(auth_router.router)
app.include_router(todo_router.router)  # <-- include ToDo routes



# This defines Bearer token usage for Swagger
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

