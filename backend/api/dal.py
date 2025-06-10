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
    select(models.Auto).options(selectinload(models.Auto.venta)).where(models.Auto.id == nuevo_auto.id)#mirar si añadir
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
async def crear_marca(db: AsyncSession, marca:
schemas.MarcaCreateRequest):
    nuevo_marca = models.Marca(**marca.dict())
    db.add(nuevo_marca)
    await db.commit()
    await db.refresh(nuevo_marca)
    return nuevo_marca
async def obtener_marca(db: AsyncSession): 
    result = await db.execute(select(models.Marca))
    return result.scalars().all()
async def crear_color(db: AsyncSession, color:
schemas.ColorCreateRequest):
    nuevo_color = models.Color(**color.dict())
    db.add(nuevo_color)
    await db.commit()
    await db.refresh(nuevo_color)
    return nuevo_color
async def obtener_color(db: AsyncSession): 
    result = await db.execute(select(models.Color))
    return result.scalars().all()
async def crear_modelo(db: AsyncSession, modelo:
schemas.ModeloCreateRequest):
    nuevo_modelo = models.Modelo(**modelo.dict())
    db.add(nuevo_modelo)
    await db.commit()
    await db.refresh(nuevo_modelo)
    return nuevo_modelo
async def obtener_modelo(db: AsyncSession): 
    result = await db.execute(select(models.Modelo))
    return result.scalars().all()
async def crear_estadov(db: AsyncSession, estado:
schemas.Estado_vehiculoCreateRequest):
    nuevo_estado = models.Estado_vehículo(**estado.dict())
    db.add(nuevo_estado)
    await db.commit()
    await db.refresh(nuevo_estado)
    return nuevo_estado
async def obtener_estadov(db: AsyncSession): 
    result = await db.execute(select(models.Estado_vehículo))
    return result.scalars().all()
async def crear_combustible(db: AsyncSession, combustible:
schemas.Tipo_combustibleCreateRequest):
    nuevo_combustible = models.Estado_vehículo(**combustible.dict())
    db.add(nuevo_combustible)
    await db.commit()
    await db.refresh(nuevo_combustible)
    return nuevo_combustible
async def obtener_combustibles(db: AsyncSession): 
    result = await db.execute(select(models.Tipo_combustible))
    return result.scalars().all()
async def crear_vendedor(db: AsyncSession, vendedor:
schemas.VendedorCreateRequest):
    nuevo_vendedor = models.Estado_vehículo(**vendedor.dict())
    db.add(nuevo_vendedor)
    await db.commit()
    await db.refresh(nuevo_vendedor)
    return nuevo_vendedor
async def obtener_vendedores(db: AsyncSession): 
    result = await db.execute(select(models.Vendedor))
    return result.scalars().all()
async def crear_cliente(db: AsyncSession, cliente:
schemas.VendedorCreateRequest):
    nuevo_cliente = models.Estado_vehículo(**cliente.dict())
    db.add(nuevo_cliente)
    await db.commit()
    await db.refresh(nuevo_cliente)
    return nuevo_cliente
async def obtener_clientes(db: AsyncSession): 
    result = await db.execute(select(models.Vendedor))
    return result.scalars().all()
async def crear_metodo(db: AsyncSession, metodo:
schemas.VendedorCreateRequest):
    nuevo_metodo = models.Estado_vehículo(**metodo.dict())
    db.add(nuevo_metodo)
    await db.commit()
    await db.refresh(nuevo_metodo)
    return nuevo_metodo
async def obtener_metodos(db: AsyncSession): 
    result = await db.execute(select(models.Vendedor))
    return result.scalars().all()