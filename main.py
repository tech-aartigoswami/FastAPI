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


@app.get("/get-all-users",response_model=list[UserResponse])
def get_users_api(db:Session=Depends(get_db)):
    return get_users(db)


@app.get("/get-users-by-id/{user_id}",response_model=list[UserResponse])
def get_users_by_id_api(user_id:int,db:Session=Depends(get_db)):
    return get_user_by_id(db)




@app.delete("/delete-users-by-id/{user_id}")
def get_users_by_id_api(user_id:int,db:Session=Depends(get_db)):
    user=delete_user_by_id(db,user_id)

    if not user:
        raise HTTPException(status_code=404,detail="User Not Found")
    
    return {"message":"User Deleted Successfully"}



