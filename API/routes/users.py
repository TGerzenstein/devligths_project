from fastapi import APIRouter, Depends, Query
from models import *
from fastapi import HTTPException, status
from typing import Annotated

from models.users import User
from config.database import COLLECTIONS
from bson import ObjectId
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


__all__: list[str] = ["users_router"]

users_router = APIRouter(prefix="/users", 
                   tags=["users"],
                   responses={404: {"message": "Not found"}})



def get_users(cursor):
    return [User.from_mongo(user) for user in cursor]

# GET Request Method
@users_router.get("/")
async def list_users():
    cursor = COLLECTIONS["users"].find()
    all_users = get_users(cursor)
    return all_users


def hash_password(password: str) -> str:
    return pwd_context.hash(password)



# POST Request Method
@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):

    hashed_user = user.model_copy(update={"password": hash_password(user.password)})

    COLLECTIONS["users"].insert_one(dict(hashed_user))
    return {"result_message": f"User created: {user.name}"}

