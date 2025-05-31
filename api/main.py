from fastapi import FastAPI
from api.routers.ventas import ventas
from api.routers.autos import autos,marca
from api.database import Base, engine
api = FastAPI()
api.include_router(ventas.router, prefix="/ventas", tags=["ventas"])
api.include_router(autos.router, prefix="/autos", tags=["autos"])
api.include_router(marca.router, prefix="/marca", tags=["marca"])
