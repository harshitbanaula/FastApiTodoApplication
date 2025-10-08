# # app/models.py
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
# from sqlalchemy.orm import relationship
# from .database import Base
# import datetime

# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(50), unique=True, index=True, nullable=False)
#     email = Column(String(255), unique=True, index=True, nullable=False)
#     hashed_password = Column(String(255), nullable=False)

#     todos = relationship("ToDo", back_populates="owner", cascade="all, delete-orphan")
#     refresh_tokens = relationship("RefreshToken", back_populates="user", cascade="all, delete-orphan")

# class ToDo(Base):
#     __tablename__ = "todos"
#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String(200), nullable=False)
#     description = Column(String, nullable=True)
#     completed = Column(Boolean, default=False)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="todos")

# class RefreshToken(Base):
#     __tablename__ = "refresh_tokens"
#     id = Column(Integer, primary_key=True, index=True)
#     token = Column(String(255), unique=True, index=True, nullable=False)
#     user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     expires_at = Column(DateTime, nullable=False)
#     revoked = Column(Boolean, default=False)

#     user = relationship("User", back_populates="refresh_tokens")

# app/models.py



from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from .database import Base
import datetime

# Users table
class User(Base):
    __tablename__ = "users"  # must match your DB table name exactly

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    todos = relationship("ToDo", back_populates="owner")
    refresh_tokens = relationship("RefreshToken", back_populates="user")

# ToDos table
class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="todos")

# Refresh tokens table
class RefreshToken(Base):
    __tablename__ = "refresh_tokens"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String, nullable=False, unique=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    revoked = Column(Boolean, default=False)
    expires_at = Column(DateTime, default=lambda: datetime.datetime.utcnow() + datetime.timedelta(days=7))

    user = relationship("User", back_populates="refresh_tokens")
