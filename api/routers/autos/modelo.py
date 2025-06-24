from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.ModeloResponse)
async def crear(modelo: schemas.ModeloCreateRequest, db:AsyncSession = Depends(get_db)):
    return await dal.crear_modelo(db, modelo)
@router.get("/", response_model=list[schemas.ModeloResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_modelo(db)
@router.put("/", response_model=schemas.ModeloResponse)
async def actualizar(modelo: schemas.ModeloResponse, db: AsyncSession = Depends(get_db)):
    return await dal.modificar_modelo(db,modelo)
@router.delete("/", response_model="")
async def borrar(modelo: int,db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_modelo(db,modelo)
