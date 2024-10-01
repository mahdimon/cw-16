from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
import datetime
from sqlalchemy.orm import Session
from app.migrations import engine
from bcrypt import hashpw, gensalt
from werkzeug.security import check_password_hash
from sqlalchemy.exc import IntegrityError

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    last_login = Column(DateTime, default=datetime.datetime.now())

    post = relationship("Post", back_populates="author", cascade="all, delete-orphan")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, autoincrement=True)
    author_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    create_at = Column(DateTime, default=datetime.datetime.now())
    title = Column(String(100), nullable=False)
    body = Column(String, nullable=False)

    author = relationship("User", back_populates="post")

class Session(Base):
    __tablename__ = 'sessions'
    
    session_id = Column(String(100), primary_key=True)
    session_data = Column(String, nullable=False)
    expire_date = Column(Date, nullable=False)


def custom_register(data):
    if data["password1"] != data["password2"] or len(data["password1"]) < 6:
        return False
    
    hashed_password = hashpw(data["password1"].encode('utf-8'), gensalt())

    user = User(
        username=data["username"],
        password=hashed_password,
        email=data["email"]
    )

    with Session(engine) as session:
        session.add(user)
        try:
            session.commit()
            return True
        except IntegrityError:
            session.rollback()
            return False