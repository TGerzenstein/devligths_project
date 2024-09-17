from fastapi import FastAPI, Request, Form, HTTPException, status, APIRouter, Cookie
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from config.__base import SECRET_KEY
from passlib.context import CryptContext
import jwt
from jwt.exceptions import InvalidTokenError
import logging
from datetime import datetime, timedelta, timezone



app = FastAPI()

templates = Jinja2Templates(directory="templates")


__all__: list[str] = ["app_test"]


app_test = APIRouter(prefix="/test", 
                     tags=["test"],
                     responses={404: {"message": "Not found"}})

db_users = {
    "tatiana": {
        "_id": "1",
        "username": "tatiana", 
        "password": "123#hash", 
    },
    "antonio": {
        "_id": "2",
        "username": "antonio", 
        "password": "321#hash", 
    }
}



oauth2_scheme= OAuth2PasswordBearer("/token")
pwd_context= CryptContext(schemes=["bcrypt"], deprecated="auto")



SECRET = SECRET_KEY
ALGORITHM = "HS256"
TOKEN_MINUT_EXP = 8000




def get_user(username: str, db: list):
    if username in db:
        return db[username]
    return None



def authenticate_user(password: str, password_plane: str):
    password_clean = password.split("#")[0]
    if password_plane == password_clean:
        return True
    return False


def create_token(data: dict):
    data_token = data.copy()
    data_token["exp"] = datetime.now(timezone.utc) + timedelta(minutes=TOKEN_MINUT_EXP)
    
    token_jwt = jwt.encode(data_token, key=SECRET, algorithm=ALGORITHM)
    return token_jwt
     



@app_test.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("/index.html", {"request": request, "title": "Final Project API", "description": "Go to"})




@app_test.get("/dashboard", response_class=HTMLResponse)
async def dashboard(request: Request, access_token: Annotated[str | None, Cookie()] = None):
    if access_token is None:
        return RedirectResponse("/api/test", status_code=302)
    
    try:
        data_user = jwt.decode(access_token, key=SECRET, algorithms=[ALGORITHM])
       # if get_user(data_user["username"], db_users) is None:
        #    return RedirectResponse("/", status_code=302)
        print(data_user)    
        return templates.TemplateResponse("/dashboard.html", {"request": request, "user": data_user})
    except InvalidTokenError:
        return RedirectResponse("/", status_code=302)



@app_test.post("/login")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user_data = get_user(username, db_users)
    
    if user_data is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="User not found")

    if not authenticate_user(user_data["password"], password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Incorrect password")
    
    token = create_token({"username": user_data["username"]})
    
    return RedirectResponse("dashboard", status_code=302, 
                            headers={"set-cookie": f"access_token={token}; Max-Age={TOKEN_MINUT_EXP}"})





logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



@app_test.post("/logout")
async def logout(response = RedirectResponse):
        logger.info("Intentando hacer logout y redireccionar al login...")
        response = RedirectResponse("/api/test", status_code=302)
        response.delete_cookie("access_token")
        logger.info("Cookie 'access_token' eliminada con éxito.")
        return response
        
    #except Exception as e:
    #    logger.error(f"Error en la función logout: {str(e)}")        
    #    raise HTTPException(status_code=500, detail=f"Error en el proceso de logout: {str(e)}")


