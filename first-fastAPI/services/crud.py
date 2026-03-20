from sqlalchemy.orm import *
from models import *
from services.crud import *
from schema import UserCreate
from schema import UserUpdate
import models
import schema


def create_user(db:session,user:schema.UserCreate):
    db_user=User(
        name=user.name,
        age= user.age
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_users(db:Session):
    users=db.query(User).all()# select + from user
    return users

def get_user_by_id(db:Session,user_id:int):
    user=db.query(User).filter(User.id==user_id).first()
    return user


def get_user_by_id(db:Session,user_id:int):
    user=db.query(User).filter(User.id==user_id).first()
    return user

def update_user (db: Session, user_id: int, user: UserUpdate):

    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        return None

    db_user.name = user.name
    db_user.email = user.email

    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user_by_id(db:Session,user_id:int):
    user=db.query(User).filter(User.id==user_id).first()
    
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user