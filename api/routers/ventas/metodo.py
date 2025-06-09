from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.Metodo_pagoResponse)
async def crear(metodo: schemas.Metodo_pagoCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_metodo(db, metodo)
@router.get("/", response_model=list[schemas.Metodo_pagoResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_metodos(db)