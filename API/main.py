from fastapi import FastAPI
from routes import api_router


app = FastAPI()

# routers
app.include_router(api_router)
