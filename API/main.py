from fastapi import FastAPI, Depends, HTTPException, status, Form
from fastapi.responses import HTMLResponse
from fastapi.security import APIKeyHeader, OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from routes import api_router

from typing import Union

#from config.database import COLLECTIONS
from config.__base import SECRET_KEY
from passlib.context import CryptContext


app = FastAPI()

# routers
app.include_router(api_router)


""" 
API_KEY_TOKEN =  SECRET_KEY
api_key_token = APIKeyHeader(name="Token")

@app.get("/protected-route")
def protected_route(token: str = Depends(api_key_token)):
    if token != API_KEY_TOKEN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)
    return {"hello": "FASTAPI"}    
    

 """



fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_pass": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",        
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_pass": "fakehashedsecret2",
        "disabled": True,
    },
}


oauth2_scheme= OAuth2PasswordBearer("/token")
pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")



class NewUser(BaseModel):
    username: str
    full_name: Union[str, None ] = None
    email: Union[str, None ] = None
    disabled: bool | None = None    

class UserInDB(NewUser):
    hashed_pass: str



def get_user(db, username):
    if username in db:
        user_data= db[username]
        return UserInDB(**user_data)
    return []

def verify_password(plane_password, hashed_pass):
    return pwd_context.verify(plane_password, hashed_pass)


def authenticate_user(db, username, password):
    user = get_user(db, username)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    if not verify_password(password, user.hashed_pass): #true or false
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return user
    

@app.get("/users/me")
def user(token: str = Depends(oauth2_scheme)):
    return "I am user"


@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    print(user)
    return "I am loggin"
