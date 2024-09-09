from pydantic import Field
from pydantic import BaseModel
from typing import Optional
from pydantic_mongo import PydanticObjectId
from enum import Enum

__all__: list[str] = ["Product"] 




class Category(str, Enum):
    Nuevo = "Nuevo"
    Usado = "Usado"
    

class Product(BaseModel):
    id: Optional[str] = None
    name: str
    description: Optional[str] 
    price: float
    quantity: int 
    category: Optional[Category] = None  
    
    class Config:
        from_attributes = True  

    @classmethod
    def product_db(cls, product: dict) -> "Product":
        return cls(
            id = str(product["_id"]),
            name= product["name"],
            description = product.get("description"), 
            price = product["price"],
            quantity = product["quantity"],
            category = product.get("category", None) 
        )