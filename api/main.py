from fastapi import FastAPI
from api.routers.ventas import ventas
from api.routers.autos import autos,marca,color,modelo, estadov, combustible
from api.database import Base, engine
api = FastAPI()
api.include_router(ventas.router, prefix="/ventas", tags=["ventas"])
api.include_router(autos.router, prefix="/autos", tags=["autos"])
api.include_router(marca.router, prefix="/marca", tags=["marca"])
api.include_router(color.router, prefix="/color", tags=["color"])
api.include_router(modelo.router, prefix="/modelo", tags=["modelo"])
api.include_router(estadov.router, prefix="/etadov", tags=["estadov"])
api.include_router(combustible.router, prefix="/combustible", tags=["combustible"])