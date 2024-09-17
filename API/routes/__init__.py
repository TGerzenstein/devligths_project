__all__: list[str] = ["api_router"]

from fastapi import APIRouter
from routes.products import products_router
from routes.users import users_router
from routes.auth_users import auth_user
from routes.test import app_test


api_router = APIRouter(prefix="/api")
api_router.include_router(products_router)
api_router.include_router(users_router)
api_router.include_router(auth_user)
api_router.include_router(app_test)
