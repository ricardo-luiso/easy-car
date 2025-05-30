from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from api import models, schemas
async def crear_venta(db: AsyncSession, venta:
schemas.VentaCreateRequest):
    nuevo_venta = models.Venta(**venta.dict())
    db.add(nuevo_venta)
    await db.commit()
    await db.refresh(nuevo_venta)
    return nuevo_venta
async def crear_auto(db: AsyncSession, auto:
schemas.AutoCreateRequest):
    nuevo_auto = models.Auto(**auto.dict())
    db.add(nuevo_auto)
    await db.commit()
    await db.refresh(nuevo_auto)
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Auto.venta)).where(models.Auto.id == nuevo_auto.id)
)
    auto_con_relacion = result.scalar_one()
    return auto_con_relacion
async def obtener_ventas(db: AsyncSession): 
    result = await db.execute(select(models.Venta))
    return result.scalars().all()
async def obtener_autos(db: AsyncSession):
    result = await db.execute(
select(models.Auto).options(selectinload(models.Auto.venta)) )
    return result.scalars().all()