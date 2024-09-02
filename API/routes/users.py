from fastapi import APIRouter, Depends, Query
from models import *
from fastapi import HTTPException, status
from typing import Annotated

from models.users import User
from config.database import COLLECTIONS
from bson import ObjectId
from models.schema import get_users


__all__: list[str] = ["users_router"]

users_router = APIRouter(prefix="/users", 
                   tags=["users"],
                   responses={404: {"message": "Not found"}})


""" 
class CommonDep:
    def __init__(self, start_date: str, end_date: str) -> None:
        self.start_date = start_date
        self.end_date = end_date
        
        
@users_router.get("/s")
async def get_users_parameters(commons: CommonDep = Depends()):
    return f"Users {commons.start_date} and {commons.end_date}"
 """

#find() retorna un cursor
#model_dump: create dic

#GET Request Method
@users_router.get("/")
async def list_users():
    all_users =  get_users(COLLECTIONS["users"].find())
    return all_users


#POST Request Method
@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(user: User):
    COLLECTIONS["users"].insert_one(dict(user))
    return {"result message": f"User created: {user}"} 