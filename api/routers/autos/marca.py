from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session: 
        yield session
@router.post("/", response_model=schemas.MarcaResponse)
async def crear(auto: schemas.MarcareateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_marca(db, auto)
@router.get("/", response_model=list[schemas.MarcaResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_marcas(db)
