from fastapi import *
from database import *
from sqlalchemy import *
from database import engine
from sqlalchemy.orm import *
from services.crud import *
from models import *
from schema import *
from schema import UserResponse

Base.metadata.create_all(bind=engine)



app=FastAPI()

@app.get("/")
def home():
    return 'hello world!'

@app.get("/db-test")
def test_db():
    try:
        with engine.connect() as con:
            result=con.execute(text("SELECT 1"))
            return {"database": "connected",
                    "result":str(result.fetchone())
                    }
        
    except Exception as e :
        return str(e)
    

@app.post("/create-user",response_model=UserResponse)
def create_user_api(user:UserCreate,db:Session=Depends(get_db)):
    return create_user(db,user)

    
