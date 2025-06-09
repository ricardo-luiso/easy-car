from pydantic import BaseModel
from typing import Optional
class VentaCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str
    venta_id: int
class AutoCreateRequest(BaseModel):
    nombre: Optional[str] = None
    auto_id: int
class MarcaCreateRequest(BaseModel):
    nombre: str
class ColorCreateRequest(BaseModel):
    nombre: str
class Tipo_combustibleCreateRequest(BaseModel):
    nombre: str
class Estado_vehiculoCreateRequest(BaseModel):
    nombre: str
class ModeloCreateRequest(BaseModel):
    nombre: str
class VendedorCreateRequest(BaseModel):
    nombre: str            
class ClienteCreateRequest(BaseModel):
    nombre: str
class Metodo_pagoCreateRequest(BaseModel):
    nombre: str
class Estado_ventaCreateRequest(BaseModel):
    nombre: str

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
class MarcaResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True   
class ColorResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True
class Tipo_combustibleResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True
class Estado_vehiculoResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True    
class VendedorResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True    
class ClienteResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True 
class Metodo_pagoResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True
class Estado_ventaResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True           