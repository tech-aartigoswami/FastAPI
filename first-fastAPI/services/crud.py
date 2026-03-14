from sqlalchemy.orm import *
from models import *
from services.crud import *
from schema import UserCreate
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