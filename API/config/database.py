from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.__base import *


__all__: list[str] = ["db", "COLLECTIONS"]


client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))

DB_NAME = "devlights_eCommerce_app"
#create database
db = client[DB_NAME]

#collections in db
COLLECTIONS = {
    "products": db["products"],
    "users": db["users"]
}


try:
    client.admin.command("ping")
    logger.info("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)




