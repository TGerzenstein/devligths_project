from fastapi import FastAPI, Request
from routes import api_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.include_router(api_router)


# dominios que pueden acceder a la API
allowed_origins = [
    "http://localhost:3000",  # Ejemplo: tu aplicación frontend en React o Vue
    "https://myfrontendapp.com",  # Un dominio público
]

# middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins = allowed_origins,  # Permitir estos orígenes
    allow_credentials = True,         # Permitir cookies y credenciales
    allow_methods = ["*"],            # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers = ["*"],            # Permitir todos los headers
)


@app.get("/route", summary="middleware")
async def route():
    return {"message": "This route is an example"}