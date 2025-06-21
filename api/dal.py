from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload
from sqlalchemy import update
from api import models, schemas
from fastapi import HTTPException
import api.auth as auth

async def crear_venta(db: AsyncSession, venta:schemas.VentaCreateRequest):
    nuevo_venta = models.Venta(**venta.dict())
    db.add(nuevo_venta)
    await db.commit()
    await db.refresh(nuevo_venta)
    return nuevo_venta

async def obtener_ventas(db: AsyncSession):
    result = await db.execute(select(models.Venta))
    return result.scalars().all()

async def modificar_venta(db: AsyncSession, venta:schemas.VentaResponse):
    ventam = models.Venta(**venta.dict())
    stmt = update(models.Venta).where(models.Venta.id == ventam.id).values(**venta.dict())#No se si funciona
    await db.execute(stmt)
    await db.commit()
    return ventam

async def eliminar_venta(db: AsyncSession, venta):
    result = await db.execute(select(models.Auto).options(selectinload(models.Venta)).where(models.Venta.id == venta))
    return result.scalars().all()

async def crear_auto(db: AsyncSession, auto:schemas.AutoCreateRequest):
    nuevo_auto = models.Auto(**auto.dict())
    db.add(nuevo_auto)
    await db.commit()
    await db.refresh(nuevo_auto)
    result = await db.execute(select(models.Auto).options(selectinload(models.Auto)).where(models.Auto.id == nuevo_auto.id))#mirar si añadir
    auto_con_relacion = result.scalar_one()
    return auto_con_relacion
async def obtener_autos(db: AsyncSession):
    result = await db.execute(select(models.Auto).options(selectinload(models.Auto)))
    return result.scalars().all()

async def modificar_auto(db: AsyncSession, auto:schemas.AutoResponse):
    autom = models.Auto(**auto.dict())
    stmt = update(models.Auto).where(models.Auto.id == autom.id).values(**auto.dict())#No se si funciona
    await db.execute(stmt)
    await db.commit()
    return autom

async def eliminar_auto(db: AsyncSession, auto:int):
    result = await db.execute(select(models.Auto).where(models.Auto.id == auto))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_marca(db: AsyncSession, marca:schemas.MarcaCreateRequest):
    nuevo_marca = models.Marca(**marca.dict())
    db.add(nuevo_marca)
    await db.commit()
    await db.refresh(nuevo_marca)
    return nuevo_marca

async def obtener_marca(db: AsyncSession):
    result = await db.execute(select(models.Marca))
    return result.scalars().all()

async def modificar_marca(db: AsyncSession, marca:schemas.MarcaResponse):
    marcam = models.Marca(**marca.dict())
    stmt = update(models.Marca).where(models.Marca.id == marcam.id).values(nombre=marcam.nombre)
    await db.execute(stmt)
    await db.commit()
    return marcam

async def eliminar_marca(db: AsyncSession, marca:int):
    result = await db.execute(select(models.Marca).where(models.Marca.id == marca))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_color(db: AsyncSession, color:schemas.ColorCreateRequest):
    nuevo_color = models.Color(**color.dict())
    db.add(nuevo_color)
    await db.commit()
    await db.refresh(nuevo_color)
    return nuevo_color
async def obtener_color(db: AsyncSession):
    result = await db.execute(select(models.Color))
    return result.scalars().all()

async def modificar_color(db: AsyncSession, color:schemas.ColorResponse):
    colorm = models.Color(**color.dict())
    stmt = update(models.Color).where(models.Color.id == colorm.id).values(nombre=colorm.nombre)
    await db.execute(stmt)
    await db.commit()
    return colorm

async def eliminar_color(db: AsyncSession, color:int):
    result = await db.execute(select(models.Color).where(models.Color.id == color))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_modelo(db: AsyncSession, modelo:schemas.ModeloCreateRequest):
    nuevo_modelo = models.Modelo(**modelo.dict())
    db.add(nuevo_modelo)
    await db.commit()
    await db.refresh(nuevo_modelo)
    return nuevo_modelo
async def obtener_modelo(db: AsyncSession):
    result = await db.execute(select(models.Modelo))
    return result.scalars().all()

async def modificar_modelo(db: AsyncSession, modelo:schemas.ModeloResponse):
    modelom = models.Modelo(**modelo.dict())
    stmt = update(models.Modelo).where(models.Modelo.id == modelom.id).values(nombre=modelom.nombre)
    await db.execute(stmt)
    await db.commit()
    return modelom

async def eliminar_modelo(db: AsyncSession, modelo:int):
    result = await db.execute(select(models.Modelo).where(models.Modelo.id == modelo))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_estadovehiculo(db: AsyncSession, estado:schemas.Estado_vehiculoCreateRequest):
    nuevo_estado = models.Estado_vehiculo(**estado.dict())
    db.add(nuevo_estado)
    await db.commit()
    await db.refresh(nuevo_estado)
    return nuevo_estado
async def obtener_estadovehiculo(db: AsyncSession):
    result = await db.execute(select(models.Estado_vehiculo))
    return result.scalars().all()

async def modificar_estadovehiculo(db: AsyncSession, estado:schemas.Estado_vehiculoResponse):
    estadom = models.Estado_vehiculo(**estado.dict())
    stmt = update(models.Estado_vehiculo).where(models.Estado_vehiculo.id == estadom.id).values(nombre=estadom.nombre)
    await db.execute(stmt)
    await db.commit()
    return estadom

async def eliminar_estadovehiculo(db: AsyncSession, estado:int):
    result = await db.execute(select(models.Estado_vehiculo).where(models.Estado_vehiculo.id == estado))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_estadoventa(db: AsyncSession, estado:schemas.Estado_vehiculoCreateRequest):
    nuevo_estado = models.Estado_venta(**estado.dict())
    db.add(nuevo_estado)
    await db.commit()
    await db.refresh(nuevo_estado)
    return nuevo_estado

async def obtener_estadoventa(db: AsyncSession):
    result = await db.execute(select(models.Estado_venta))
    return result.scalars().all()

async def modificar_estadoventa(db: AsyncSession, estado:schemas.Estado_ventaResponse):
    estadom = models.Estado_venta(**estado.dict())
    stmt = update(models.Estado_venta).where(models.Estado_venta.id == estadom.id).values(nombre=estadom.nombre)
    await db.execute(stmt)
    await db.commit()
    return estadom

async def eliminar_estadoventa(db: AsyncSession, estado:int):
    result = await db.execute(select(models.Estado_venta).where(models.Estado_venta.id == estado))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_combustible(db: AsyncSession, combustible:schemas.Tipo_combustibleCreateRequest):
    nuevo_combustible = models.Tipo_combustible(**combustible.dict())
    db.add(nuevo_combustible)
    await db.commit()
    await db.refresh(nuevo_combustible)
    return nuevo_combustible

async def obtener_combustibles(db: AsyncSession):
    result = await db.execute(select(models.Tipo_combustible))
    return result.scalars().all()

async def modificar_combustible(db: AsyncSession, combustible:schemas.Tipo_combustibleResponse):
    combustiblem = models.Tipo_combustible(**combustible.dict())
    stmt = update(models.Tipo_combustible).where(models.Tipo_combustible.id == combustiblem.id).values(nombre=combustiblem.nombre)
    await db.execute(stmt)
    await db.commit()
    return combustiblem

async def eliminar_combustible(db: AsyncSession, combustible:int):
    result = await db.execute(select(models.Tipo_combustible).where(models.Tipo_combustible.id == combustible))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_vendedor(db: AsyncSession, vendedor:schemas.VendedorCreateRequest):
    nuevo_vendedor = models.Vendedor(**vendedor.dict())
    db.add(nuevo_vendedor)
    await db.commit()
    await db.refresh(nuevo_vendedor)
    return nuevo_vendedor
async def obtener_vendedores(db: AsyncSession):
    result = await db.execute(select(models.Vendedor))
    return result.scalars().all()

async def modificar_vendedor(db: AsyncSession, vendedor:schemas.VendedorResponse):
    vendedorm = models.Vendedor(**vendedor.dict())
    stmt = update(models.Vendedor).where(models.Vendedor.id == vendedorm.id).values(nombre=vendedorm.nombre)
    await db.execute(stmt)
    await db.commit()
    return vendedorm

async def eliminar_vendedor(db: AsyncSession, vendedor:int):
    result = await db.execute(select(models.Auto).where(models.Vendedor.id == vendedor))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."
async def crear_cliente(db: AsyncSession, cliente:schemas.ClienteCreateRequest):
    nuevo_cliente = models.Cliente(**cliente.dict())
    db.add(nuevo_cliente)
    await db.commit()
    await db.refresh(nuevo_cliente)
    return nuevo_cliente

async def obtener_clientes(db: AsyncSession):
    result = await db.execute(select(models.Cliente))
    return result.scalars().all()

async def modificar_cliente(db: AsyncSession, cliente:schemas.ClienteResponse):
    clientem = models.Cliente(**cliente.dict())
    stmt = update(models.Cliente).where(models.Cliente.id == clientem.id).values(nombre=clientem.nombre)
    await db.execute(stmt)
    await db.commit()
    return clientem

async def eliminar_cliente(db: AsyncSession, cliente:int):
    result = await db.execute(select(models.Auto).where(models.Cliente.id == cliente))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def crear_metodo(db: AsyncSession, metodo:schemas.Metodo_pagoCreateRequest):
    nuevo_metodo = models.Metodo_pago(**metodo.dict())
    db.add(nuevo_metodo)
    await db.commit()
    await db.refresh(nuevo_metodo)
    return nuevo_metodo

async def obtener_metodos(db: AsyncSession):
    result = await db.execute(select(models.Metodo_pago))
    return result.scalars().all()

async def modificar_metodo(db: AsyncSession, metodo:schemas.Metodo_pagoResponse):
    metodom = models.Metodo_pago(**metodo.dict())
    stmt = update(models.Metodo_pago).where(models.Metodo_pago.id == metodom.id).values(nombre=metodom.nombre)
    await db.execute(stmt)
    await db.commit()
    return metodom

async def eliminar_metodo(db: AsyncSession, metodo:int):
    result = await db.execute(select(models.Auto).where(models.Metodo_pago.id == metodo))
    result=result.scalars().first()
    await db.delete(result)
    await db.commit()
    return "Borrado con éxito."

async def inicio_usuario(db: AsyncSession, usuario: schemas.UsuarioCreateRequest):
    db_user = db.query(models.Usuario).filter_by(nombre=usuario.apodo).first()
    if not db_user or not auth.verify_password(usuario.contrasena, db_user.hash):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    access_token = auth.create_access_token(data={"sub": usuario.apodo})
    return {"access_token": access_token, "token_type": "bearer"}

async def crear_usuario(db: AsyncSession, usuario: schemas.UsuarioCreateRequest):
    if db.query(models.Usuario).filter_by(nombre=usuario.apodo).first():
        raise HTTPException(status_code=400, detail="Usuario ya registrado")
    hashed_pw = auth.get_password_hash(usuario.contrasena)
    nuevo_usuario = models.Usuario(**usuario.dict())
    nuevo_usuario.hash=hashed_pw
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

async def obtener_usuarios(db: AsyncSession):
    result = await db.execute(select(models.Usuario))
    return result.scalars().all()
