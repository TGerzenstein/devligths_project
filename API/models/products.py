from pydantic import Field
from pydantic import BaseModel
from typing import Optional
from pydantic_mongo import PydanticObjectId


__all__: list[str] = ["Product"] 


class Product(BaseModel):
    id: PydanticObjectId = Field(default=None, alias="_id")   
    name: str
    description: Optional[str] 
    price: float
    quantity: int