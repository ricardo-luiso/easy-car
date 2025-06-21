from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.Estado_vehiculoResponse)
async def crear(estadov: schemas.Estado_vehiculoCreateRequest, db:AsyncSession = Depends(get_db)):
    return await dal.crear_estadovehiculo(db, estadov)
@router.get("/", response_model=list[schemas.Estado_vehiculoResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_estadovehiculo(db)
@router.put("/", response_model=schemas.Estado_vehiculoResponse)
async def actualizar(estadov: schemas.Estado_vehiculoCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.modificar_estadovehiculo(db,estadov)
@router.delete("/", response_model="")
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_estadovehiculo(db)
