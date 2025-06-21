from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database
router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/", response_model=schemas.VendedorResponse)
async def crear(vendedor: schemas.VendedorCreateRequest, db:AsyncSession = Depends(get_db)):
    return await dal.crear_vendedor(db, vendedor)
@router.get("/", response_model=list[schemas.VendedorResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_vendedores(db)
@router.put("/", response_model=schemas.VendedorResponse)
async def actualizar(vendedor: schemas.VendedorCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.modificar_vendedor(db,vendedor)
@router.delete("/", response_model="")
async def borrar(db: AsyncSession = Depends(get_db)):
    return await dal.eliminar_vendedor(db)