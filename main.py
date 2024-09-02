""" from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


#Models
class User(BaseModel):
    id: int
    name: str
    email: str
        

list_users = [User(id=1,name="Superman", email="super@gmail.com"),
              User(id=2, name="Batman", email="batman@gmail.com")]



# class Product(BaseModel):
#     id: int
#     name: str
#     description: str
#     price: float


#fastapi dev run the server

#Routes
@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path
@app.get("/user/{id}")
async def search_user(id: int):
    
    users = filter(lambda user: user.id == id, list_users)
    
    try: 
        return list(users)[0]
    except:
        return {"error": "No se encontró el usuario"}
 


@app.post("/user/")

async def create_user(user: User):
    
    if search_user(user.id) == User:
       return ("El usuario ya existe")
    else: 
       list_users.append(user)    
    
     """
    
    
    
    
    
 
