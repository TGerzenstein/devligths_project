from fastapi import APIRouter, Depends, Query
from models import *
from fastapi import HTTPException, status
from typing import Annotated

from models.users import User
from config.database import user_collection
from bson import ObjectId
from passlib.context import CryptContext


__all__: list[str] = ["users_router"]

users_router = APIRouter(prefix="/users", 
                   tags=["users"],
                   responses={404: {"message": "Not found"}})


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def get_users(cursor):
    return [User.from_database(user) for user in cursor]

# GET Request Method
@users_router.get("/")
async def list_users():
    cursor = user_collection.find()
    all_users = get_users(cursor)
    return all_users 


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# GET Request Method
@users_router.get("/{id}", response_model=User)
async def find_user_by_id(id: str):
    user_data = user_collection.find_one({"_id": ObjectId(id)})
    
    if user_data:
        return User.from_database(user_data)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")



# POST Request Method
@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    hashed_user = user.model_copy(update={"password": hash_password(user.password)})

    user_collection.insert_one(dict(hashed_user))
    return {"result_message": f"User created: {user.name}"}


