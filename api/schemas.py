from pydantic import BaseModel
from typing import Optional
class VentaCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str
    venta_id: int
class AutoCreateRequest(BaseModel):
    nombre: Optional[str] = None
    auto_id: int
# RESPONSE
class AutoResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True
class VentaResponse(BaseModel):
    id: int
    nombre: Optional[str]
    Vendedor: str
    auto: AutoResponse
class Config:
    orm_mode = True
