from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session: 
        yield session
@router.post("/", response_model=schemas.AutoResponse)
async def crear(auto: schemas.AutoCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_auto(db, auto)
@router.get("/", response_model=list[schemas.AutoResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_autos(db)
@router.put("/", response_model=list[schemas.AutoResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_auto(db)
@router.delete("/", response_model=list[schemas.AutoResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_auto(db)