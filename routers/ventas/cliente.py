from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.ClienteResponse)
async def crear(cliente: schemas.ClienteCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_cliente(db, cliente)
@router.get("/", response_model=list[schemas.ClienteResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_clientes(db)
@router.put("/", response_model=list[schemas.ClienteResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_cliente(db)
@router.delete("/", response_model=list[schemas.ClienteResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_cliente(db)
