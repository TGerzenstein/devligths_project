from fastapi import APIRouter
from routes.products import products_router
from routes.users import users_router


#variable
#solo api_router será exportado
__all__: list[str] = ["api_router"]

api_router = APIRouter(prefix="/api")
api_router.include_router(products_router)
api_router.include_router(users_router)
