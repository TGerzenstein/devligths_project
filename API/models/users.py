from typing import Optional, List
from pydantic import BaseModel, Field
from enum import Enum # Supports for enumerations

__all__: list[str] = ["User"]


class User(BaseModel):
    name: str
    email: str
    password: str
    disabled: bool 

    class Config:
        from_attributes = True  

    @classmethod
    def from_mongo(cls, data: dict):

        return cls(
            id = str(data["_id"]),
            name = data["name"],
            email = data["email"],
            password = data["password"],
            disabled = data.get("disabled", False) 
        )