from pydantic import BaseModel
from typing import Optional

class VentaCreateRequest(BaseModel):
    nombre: Optional[str] = None
    email: str

class AutoCreateRequest(BaseModel):
    nombre: Optional[str] = None
    marca: Optional[str] = None
    modelo: Optional[str] = None
    combustible: Optional[str] = None
    color: Optional[str] = None
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
    imagen: Optional[str]
    combustible: Optional[str]
    estado:Optional[str]
    modelo:Optional[str]
    color:Optional[str]
    marca:Optional[str]
class Config:
    orm_mode = True

class VentaResponse(BaseModel):
    id: int
    nombre: Optional[str]
    Vendedor: str
    auto: AutoResponse
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
    marca: MarcaResponse
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
