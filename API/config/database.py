__all__: list[str] = ["db", "product_collection"]

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config.__base import *


client = MongoClient(MONGODB_URI, server_api=ServerApi("1"))
DB_NAME = "devlights_eCommerce_app"
db = client[DB_NAME]

#collections in db
""" COLLECTIONS = {
    "products": db["products"],
    "users": db["users"]
} """

product_collection = db["products"]
user_collection = db["users"]


try:
    client.admin.command('ping')
    print("<--- Pinged your deployment. You successfully connected to MongoDB! --->")

except Exception as e:
    print(f"Error conection",e)



