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

async def obtener_ventas(db: AsyncSession): 
    result = await db.execute(select(models.Venta))
    return result.scalars().all()

async def modificar_venta(db: AsyncSession, venta): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Venta)).where(models.Venta.id == venta)
)
    return result.scalars().all()

async def eliminar_venta(db: AsyncSession, venta): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Venta)).where(models.Venta.id == venta)
)
    return result.scalars().all()

async def crear_auto(db: AsyncSession, auto:
schemas.AutoCreateRequest):
    nuevo_auto = models.Auto(**auto.dict())
    db.add(nuevo_auto)
    await db.commit()
    await db.refresh(nuevo_auto)
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Auto)).where(models.Auto.id == nuevo_auto.id)#mirar si añadir
)
    auto_con_relacion = result.scalar_one()
    return auto_con_relacion
async def obtener_autos(db: AsyncSession):
    result = await db.execute(
select(models.Auto).options(selectinload(models.Auto)) )
    return result.scalars().all()

async def modificar_auto(db: AsyncSession, auto): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Auto)).where(models.Auto.id == auto)
)
    return result.scalars().all()

async def eliminar_auto(db: AsyncSession, auto): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Auto)).where(models.Auto.id == auto)
)
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

async def modificar_marca(db: AsyncSession, marca): 
    result = await db.execute(
    select(models.Marca).options(selectinload(models.Auto)).where(models.Auto.id == marca)
)
    return result.scalars().all()

async def eliminar_marca(db: AsyncSession, marca): 
    result = await db.execute(
    select(models.Marca).options(selectinload(models.Marca)).where(models.Marca.id == marca)
)
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

async def modificar_color(db: AsyncSession, color): 
    result = await db.execute(
    select(models.Color).options(selectinload(models.Color)).where(models.Color.id == color)
)
    return result.scalars().all()

async def eliminar_color(db: AsyncSession, color): 
    result = await db.execute(
    select(models.Color).options(selectinload(models.Color)).where(models.Color.id == color)
)
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

async def modificar_modelo(db: AsyncSession, modelo): 
    result = await db.execute(
    select(models.Modelo).options(selectinload(models.Modelo)).where(models.Modelo.id == modelo)
)
    return result.scalars().all()

async def eliminar_modelo(db: AsyncSession, modelo): 
    result = await db.execute(
    select(models.Modelo).options(selectinload(models.Modelo)).where(models.Modelo.id == modelo)
)
    return result.scalars().all()

async def crear_estadovehiculo(db: AsyncSession, estado:
schemas.Estado_vehiculoCreateRequest):
    nuevo_estado = models.Estado_vehiculo(**estado.dict())
    db.add(nuevo_estado)
    await db.commit()
    await db.refresh(nuevo_estado)
    return nuevo_estado
async def obtener_estadovehiculo(db: AsyncSession): 
    result = await db.execute(select(models.Estado_vehiculo))
    return result.scalars().all()

async def modificar_estadovehiculo(db: AsyncSession, estado): 
    result = await db.execute(
    select(models.Estado_vehiculo).options(selectinload(models.Estado_vehiculo)).where(models.Estado_vehiculo.id == estado)
)
    return result.scalars().all()

async def eliminar_estadovehiculo(db: AsyncSession, estado): 
    result = await db.execute(
    select(models.Estado_venta).options(selectinload(models.Estado_vehiculo)).where(models.Estado_vehiculo.id == estado)
)
    return result.scalars().all()

async def crear_estadoventa(db: AsyncSession, estado:
schemas.Estado_vehiculoCreateRequest):
    nuevo_estado = models.Estado_venta(**estado.dict())
    db.add(nuevo_estado)
    await db.commit()
    await db.refresh(nuevo_estado)
    return nuevo_estado
async def obtener_estadoventa(db: AsyncSession): 
    result = await db.execute(select(models.Estado_venta))
    return result.scalars().all()

async def modificar_estadoventa(db: AsyncSession, estado): 
    result = await db.execute(
    select(models.Estado_venta).options(selectinload(models.Estado_venta)).where(models.Estado_venta.id == estado)
)
    return result.scalars().all()

async def eliminar_estadoventa(db: AsyncSession, estado): 
    result = await db.execute(
    select(models.Estado_venta).options(selectinload(models.Estado_venta)).where(models.Estado_venta.id == estado)
)
    return result.scalars().all()

async def crear_combustible(db: AsyncSession, combustible:
schemas.Tipo_combustibleCreateRequest):
    nuevo_combustible = models.Tipo_combustible(**combustible.dict())
    db.add(nuevo_combustible)
    await db.commit()
    await db.refresh(nuevo_combustible)
    return nuevo_combustible
async def obtener_combustibles(db: AsyncSession): 
    result = await db.execute(select(models.Tipo_combustible))
    return result.scalars().all()

async def modificar_combustible(db: AsyncSession, combustible): 
    result = await db.execute(
    select(models.Tipo_combustible).options(selectinload(models.Estado_venta)).where(models.Estado_venta.id == combustible)
)
    return result.scalars().all()

async def eliminar_combustible(db: AsyncSession, combustible): 
    result = await db.execute(
    select(models.Tipo_combustible).options(selectinload(models.Tipo_combustible)).where(models.Tipo_combustible.id == combustible)
)
    return result.scalars().all()

async def crear_vendedor(db: AsyncSession, vendedor:
schemas.VendedorCreateRequest):
    nuevo_vendedor = models.Vendedor(**vendedor.dict())
    db.add(nuevo_vendedor)
    await db.commit()
    await db.refresh(nuevo_vendedor)
    return nuevo_vendedor
async def obtener_vendedores(db: AsyncSession): 
    result = await db.execute(select(models.Vendedor))
    return result.scalars().all()

async def modificar_vendedor(db: AsyncSession, vendedor): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Auto)).where(models.Auto.id == vendedor)
)
    return result.scalars().all()

async def eliminar_vendedor(db: AsyncSession, vendedor): 
    result = await db.execute(
    select(models.Auto).options(selectinload(models.Vendedor)).where(models.Vendedor.id == vendedor)
)
    return result.scalars().all()

async def crear_cliente(db: AsyncSession, cliente:
schemas.ClienteCreateRequest):
    nuevo_cliente = models.Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    await db.commit()
    await db.refresh(nuevo_cliente)
    return nuevo_cliente

async def obtener_clientes(db: AsyncSession): 
    result = await db.execute(select(models.Cliente))
    return result.scalars().all()

async def modificar_cliente(db: AsyncSession, cliente): 
    result = await db.execute(
    select(models.Cliente).options(selectinload(models.Cliente)).where(models.Cliente.id == cliente)
)
    return result.scalars().all()

async def eliminar_cliente(db: AsyncSession, cliente): 
    result = await db.execute(
    select(models.Cliente).options(selectinload(models.Cliente)).where(models.Cliente.id == cliente)
)
    return result.scalars().all()

async def crear_metodo(db: AsyncSession, metodo:
schemas.Metodo_pagoCreateRequest):
    nuevo_metodo = models.Metodo_pago(**metodo.dict())
    db.add(nuevo_metodo)
    await db.commit()
    await db.refresh(nuevo_metodo)
    return nuevo_metodo

async def obtener_metodos(db: AsyncSession): 
    result = await db.execute(select(models.Metodo_pago))
    return result.scalars().all()

async def modificar_metodo(db: AsyncSession, metodo): 
    result = await db.execute(
    select(models.Metodo_pago).options(selectinload(models.Metodo_pago)).where(models.Metodo_pago.id == metodo)
)
    return result.scalars().all()

async def eliminar_metodo(db: AsyncSession, metodo): 
    result = await db.execute(
    select(models.Metodo_pago).options(selectinload(models.Metodo_pago)).where(models.Metodo_pago.id == metodo)
)
    return result.scalars().all()

async def crear_usuario(db: AsyncSession, usuario:
schemas.UsuarioCreateRequest):
    nuevo_usuario = models.Usuario(**usuario.dict())
    db.add(nuevo_usuario)
    await db.commit()
    await db.refresh(nuevo_usuario)
    return nuevo_usuario

async def obtener_usuarios(db: AsyncSession): 
    result = await db.execute(select(models.Usuario))
    return result.scalars().all()

async def modificar_usuario(db: AsyncSession, usuario): 
    result = await db.execute(
    select(models.Usuario).options(selectinload(models.Usuario)).where(models.Usuario.id == usuario)
)
    return result.scalars().all()

async def eliminar_usuario(db: AsyncSession, usuario): 
    result = await db.execute(
    select(models.Usuario).options(selectinload(models.Usuario)).where(models.Usuario.id == usuario)
)
    return result.scalars().all()
