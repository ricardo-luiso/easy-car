from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from api import schemas, dal, database

router = APIRouter()
async def get_db():
    async with database.AsyncSessionLocal() as session:
        yield session
@router.post("/registro", response_model=schemas.UsuarioResponse)
async def registro(usuario: schemas.UsuarioCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.crear_usuario(db, usuario)
@router.post("/login", response_model=schemas.Token)
async def login(usuario: schemas.UsuarioCreateRequest, db: AsyncSession = Depends(get_db)):
    return await dal.inicio_usuario(db, usuario)
@router.get("/", response_model=list[schemas.UsuarioResponse])
async def listar(db: AsyncSession = Depends(get_db)):
    return await dal.obtener_usuarios(db)