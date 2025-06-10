from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.VentaResponse)
async def crear(venta: schemas.VentaCreateRequest, db:
AsyncSession = Depends(get_db)):
    return await dal.crear_venta(db, venta)
@router.get("/", response_model=list[schemas.VentaResponse]) 
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_ventas(db)
@router.put("/", response_model=list[schemas.VentaResponse]) 
async def actualizar(db: AsyncSession = Depends(get_db)):
    return await dal.modificar_venta(db)
@router.delete("/", response_model=list[schemas.VentaResponse]) 
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_venta(db)