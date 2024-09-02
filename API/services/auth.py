
    
"""
app = FastAPI()

access_security= JwtAccesBearer(secret_key=SECRET_KEY)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)



       

    user_db = users_db.get(form.username)
    if not user_db:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}



def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    

async def user_current(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
       raise HTTPException(
          status_code=status.HTTP_401_UNAUTHORIZED, 
          detail="Credencial invalida")
    

 
@app.post("/login")
async def login_user(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user(form.username)
    if not form.password == user.password:
       raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    return {"access_token": user.username, "token_type": "bearer"}



@app.get("/users/myuser")
async def myuser(user: User = Depends(user_current)):
    return user
   """ 