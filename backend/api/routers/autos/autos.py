from fastapi import APIRouter, Depends, Form, UploadFile, File
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import AsyncSession
import os
import shutil
import uuid
from api import schemas, dal, database

router = APIRouter()

async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
        
@router.post("/", response_model=dict)
async def crear(
    nombre: str = Form(...),
    marca_id: str = Form(...),
    modelo_id: str = Form(...),
    combustible_id: str = Form(...),
    estado_id: str = Form(...),
    color_id: str = Form(...),
    imagen: UploadFile = File(None),
    db: AsyncSession = Depends(get_db),
):
    ruta_imagen = None
    if imagen:
        extension = os.path.splitext(imagen.filename)[1]
        nombre_archivo = f"{uuid.uuid4().hex}{extension}"
        ruta = os.path.join("uploads", nombre_archivo)
        with open(ruta, "wb") as f:
            shutil.copyfileobj(imagen.file, f)
        ruta_imagen = f"/uploads/{nombre_archivo}"

    auto_data = schemas.AutoCreateRequest(
        nombre=nombre,
        marca_id=marca_id,
        modelo_id=modelo_id,
        combustible_id=combustible_id,
        estado_id=estado_id,
        color_id=color_id,
        imagen=ruta_imagen,
    )

    return await dal.crear_auto(db, auto_data)

@router.put("/{auto_id}", response_model=dict)
async def actualizar(
    auto_id: int,
    nombre: str = Form(...),
    marca_id: str = Form(...),
    modelo_id: str = Form(...),
    combustible_id: str = Form(...),
    estado_id: str = Form(...),
    color_id: str = Form(...),
    imagen: UploadFile = File(None),
    db: AsyncSession = Depends(get_db),
):
    ruta_imagen = None
    if imagen:
        extension = os.path.splitext(imagen.filename)[1]
        nombre_archivo = f"{uuid.uuid4().hex}{extension}"
        ruta = os.path.join("uploads", nombre_archivo)
        with open(ruta, "wb") as f:
            shutil.copyfileobj(imagen.file, f)
        ruta_imagen = f"/uploads/{nombre_archivo}"

    auto_data = schemas.AutoCreateRequest(
        nombre=nombre,
        marca_id=marca_id,
        modelo_id=modelo_id,
        combustible_id=combustible_id,
        estado_id=estado_id,
        color_id=color_id,
        imagen=ruta_imagen  # Puede ser None si no se envió una nueva
    )

    return await dal.modificar_auto(db, auto_id, auto_data)

@router.get("/", response_model=list[schemas.AutoResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_autos(db)

@router.get("/{auto_id}", response_model=schemas.AutoResponse)
async def obtener_auto(auto_id: int, db: AsyncSession = Depends(get_db)):
    return await dal.obtener_auto_por_id(db, auto_id)



@router.delete("/", response_model="")
async def borrar(auto: int,db: AsyncSession = Depends(get_db),):
    return await dal.eliminar_auto(db,auto)