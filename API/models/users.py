from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum # Supports for enumerations


__all__: list[str] = ["User"]

""" # enum : clases que listan todos los valores posibles que puede tomar una instancia
class SetupRole(str, Enum):
    customer = "customer"
    seller = "seller"

# enum for role
class Role(str, Enum):
    admin = "admin"
    customer = "customer"
    seller = "seller"
     """

class User(BaseModel):
    id: Optional[str]
    name: str 
    email: str 
    password: str 
    
