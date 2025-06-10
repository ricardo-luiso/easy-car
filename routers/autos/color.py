from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session: 
        yield session
@router.post("/", response_model=schemas.ColorResponse)
async def crear(color: schemas.ColorCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_color(db, color)
@router.get("/", response_model=list[schemas.ColorResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_color(db)
@router.put("/", response_model=list[schemas.ColorResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_color(db)
@router.delete("/", response_model=list[schemas.ColorResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_color(db)
