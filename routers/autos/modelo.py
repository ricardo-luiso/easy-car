from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session: 
        yield session
@router.post("/", response_model=schemas.MarcaResponse)
async def crear(modelo: schemas.MarcaCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_modelo(db, modelo)
@router.get("/", response_model=list[schemas.MarcaResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_modelo(db)
@router.put("/", response_model=list[schemas.ModeloResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_modelo(db)
@router.delete("/", response_model=list[schemas.ModeloResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_modelo(db)
