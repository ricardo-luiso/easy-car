from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.MarcaResponse)
async def crear(marca: schemas.MarcaCreateRequest, db:AsyncSession = Depends(get_db)):
    return await dal.crear_marca(db, marca)
@router.get("/", response_model=list[schemas.MarcaResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_marca(db)
@router.put("/", response_model=schemas.MarcaResponse)
async def actualizar(marca: schemas.MarcaResponse, db: AsyncSession = Depends(get_db)):
    return await dal.modificar_marca(db, marca)
@router.delete("/", response_model="")
async def borrar(marca: int,db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_marca(db,marca)
