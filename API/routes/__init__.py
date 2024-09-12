from fastapi import APIRouter
from routes.products import products_router
from routes.users import users_router
from routes.auth_users import auth_users
from routes.test import app_test


#variable
#solo api_router será exportado
__all__: list[str] = ["api_router"]

api_router = APIRouter(prefix="/api")
api_router.include_router(products_router)
api_router.include_router(users_router)
api_router.include_router(auth_users)
api_router.include_router(app_test)
