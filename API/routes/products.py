from fastapi.routing import APIRouter
from fastapi import HTTPException, status, Depends
from fastapi.responses import JSONResponse

from models import *
from pydantic_mongo import PydanticObjectId
from models.products import Product
from config.database import COLLECTIONS
from bson import ObjectId
from models.schema import get_all


__all__: list[str] = ["products_router"]



products_router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "Not found this"}})



""" #model_dump: create dic
#GET Request Method
@products_router.get("/")
async def list_products():
    products = get_all(ProductService((COLLECTIONS)["products"]))
   # products =  get_all(COLLECTIONS["products"].find(limit=2))
    return products
    
"""


#POST Request Method
@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    COLLECTIONS["products"].insert_one(dict(product))
    return {"result message": f"Product created: {product}"}


#POST Request Method
@products_router.put("/{id}")
async def update_product(id: str, product: Product):
    COLLECTIONS["products"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(product)})
    
    
#DELETE Request Method
@products_router.delete("/{id}")
async def delete_product(id: str):
    COLLECTIONS["products"].find_one_and_delete({"_id": ObjectId(id)})
    return {"Message": "Product deleted"}
    

