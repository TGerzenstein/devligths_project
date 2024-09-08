import logging
import os
from logging import Logger  # Import Logger

from dotenv import load_dotenv

__all__: list[str] = ["MONGODB_URI", "logger", "SECRET_KEY"]

#variables
load_dotenv()

MONGODB_URI: str | None = os.getenv("MONGODB_CONNECTION_STRING")
if not MONGODB_URI:
    raise Exception("MongoDB connection string not found")


SECRET_KEY=os.getenv("SECRET_KEY")
if not SECRET_KEY:
    raise Exception("Secret key not found")



#logger: Logger = logging.getLogger("uvicorn")
#logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("passlib").setLevel(logging.ERROR)
