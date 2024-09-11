from bson import ObjectId

from fastapi.routing import APIRouter
from fastapi import HTTPException, status, Depends

from models import *
from models.products import Product, Category
from config.database import product_collection


__all__: list[str] = ["products_router"]


products_router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "Not found this"}})




def get_products(cursor):
    return [Product.product_db(product) for product in cursor]
    

@products_router.get("/")
async def list_products():
    products = get_products(product_collection.find())
    
    if products is not None: 
        return products
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Products not found")


@products_router.get("/category/{category}")
async def filter_by_category(category: Category):
    products = product_collection.find({"category": category.value})
    filtered_products = [Product.product_db(product) for product in products]
    if not filtered_products:
        raise HTTPException(status_code=404, detail="No products found in this category")
    return filtered_products


@products_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_product(product: Product):
    product_collection.insert_one(dict(product))
    return {"result message": f"Product created: {product}"}



@products_router.put("/{id}")
async def update_product(id: str, product: Product):
    
    try:
        object_id = ObjectId(id)
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid product ID")

    update_data = product.model_dump(exclude={"id", "_id"})
    updated_product = product_collection.find_one_and_update(
        {"_id": object_id},  
        {"$set": update_data}, 
        return_document=True  
    )
    
    if updated_product:
        updated_product['_id'] = str(updated_product['_id'])
        return {"message": "Product updated successfully", "product": updated_product}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")



@products_router.delete("/{id}")
async def delete_product(id: str):
    product_collection.find_one_and_delete({"_id": ObjectId(id)})
    return {"Message": "Product deleted"}
    
    