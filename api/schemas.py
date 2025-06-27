from pydantic import BaseModel
from typing import Optional

class VentaCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str

class AutoCreateRequest(BaseModel):
    nombre: Optional[str] = None
    marca_id: Optional[int] = None
    modelo_id: Optional[int] = None
    combustible_id: Optional[int] = None
    estado_id: Optional[int] = None
    color_id: Optional[int] = None
    imagen: Optional[str] = None

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
    marca_id: str

class VendedorCreateRequest(BaseModel):
    nombre: str

class ClienteCreateRequest(BaseModel):
    nombre: str

class Metodo_pagoCreateRequest(BaseModel):
    nombre: str

class Estado_ventaCreateRequest(BaseModel):
    nombre: str

class UsuarioCreateRequest(BaseModel):
    apodo: str
    mail: str
    contrasena: str
# RESPONSE
class AutoResponse(BaseModel):
    id: int
    nombre: Optional[str]
    marca_id: Optional[int] 
    modelo_id: Optional[int] 
    combustible_id: Optional[int] 
    estado_id: Optional[int] 
    color_id: Optional[int] 
    imagen: Optional[str] = None
class Config:
    orm_mode = True

class VentaResponse(BaseModel):
    id: int
    nombre: Optional[str]
    Vendedor: Optional[int]
    auto: Optional[AutoResponse]
    metodo:Optional[str]
    estado:Optional[str]
class Config:
    orm_mode = True

class MarcaResponse(BaseModel):
    id: int
    nombre: Optional[str]
class Config:
    orm_mode = True

class ModeloResponse(BaseModel):
    id: int
    nombre: Optional[str]
    marca_id: str
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

class UsuarioResponse(BaseModel):
    id: int
    apodo: Optional[str]
    mail: Optional[str]
class Config:
    orm_mode = True
    from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str
