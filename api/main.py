from fastapi import FastAPI, Depends
from api.routers.ventas import ventas,vendedor,cliente,metodo,estadoventa
from api.routers.autos import autos,marca,color,modelo, estadov, combustible
import api.routers.usuario as usuario
from api.database import Base, engine
from .dependencies import get_current_user
from fastapi.middleware.cors import CORSMiddleware
api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=[""],
    allow_headers=["*"],
)
api.include_router(ventas.router, prefix="/ventas", tags=["ventas"])
api.include_router(autos.router, prefix="/autos", tags=["autos"])
api.include_router(marca.router, prefix="/marca", tags=["marca"])
api.include_router(color.router, prefix="/color", tags=["color"])
api.include_router(modelo.router, prefix="/modelo", tags=["modelo"])
api.include_router(estadov.router, prefix="/etadovehiculo", tags=["estadov"])
api.include_router(combustible.router, prefix="/combustible", tags=["combustible"])
api.include_router(vendedor.router, prefix="/vendedor", tags=["vendedor"])
api.include_router(cliente.router, prefix="/cliente", tags=["cliente"])
api.include_router(metodo.router, prefix="/metodo", tags=["metodo"])
api.include_router(estadoventa.router, prefix="/estadoventa", tags=["estadoventa"])
api.include_router(usuario.router, prefix="/usuario", tags=["usuario"])

@api.get("/protected")
def protected_route(usuario=Depends(get_current_user)):
    return {"message": f"Hola {usuario.apodo}, estás autenticado"}
