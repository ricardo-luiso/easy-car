from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.Tipo_combustibleResponse)
async def crear(combustible: schemas.Tipo_combustibleCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_combustible(db, combustible)
@router.get("/", response_model=list[schemas.Tipo_combustibleResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_combustibles(db)
@router.put("/", response_model=list[schemas.Tipo_combustibleResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_combustible(db)
@router.delete("/", response_model=list[schemas.Tipo_combustibleResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_combustible(db)
