from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Auto(Base):
    __tablename__ = "auto"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    marca_id = Column(Integer, ForeignKey("marca.id"))
    color_id = Column(Integer, ForeignKey("color.id"))
    modelo_id = Column(Integer, ForeignKey("modelo.id"))
    combustible_id = Column(Integer, ForeignKey("combustible.id"))
    estado_id = Column(Integer, ForeignKey("estado.id"))
class Marca(Base):
    __tablename__ = "marca"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    modelo = relationship("Modelo", back_populates="marca")
class Color(Base):
    __tablename__ = "color"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Tipo_combustible(Base):
    __tablename__ = "combustible"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Estado_vehiculo(Base):
    __tablename__ = "estado"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Modelo(Base):
    __tablename__ = "modelo"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    marca_id = Column(Integer, ForeignKey("marca.id"))
    marca = relationship("Marca", back_populates="modelo", uselist=False)

class Venta(Base):
    __tablename__ = "venta"
    id = Column(Integer, primary_key=True, index=True)
    carrera = Column(String, nullable=True)
    vendedor_id = Column(Integer, ForeignKey("vendedor.id"))
    cliente_id = Column(Integer, ForeignKey("cliente.id"))
    metodo_id = Column(Integer, ForeignKey("metodo.id"))
    estado_id = Column(Integer, ForeignKey("estado.id"))
    auto_id = Column(Integer, ForeignKey("auto.id"))

class Vendedor(Base):
    __tablename__ = "vendedor"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Cliente(Base):
    __tablename__ = "cliente"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Metodo_pago(Base):
    __tablename__ = "metodo"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)

class Estado_venta(Base):
    __tablename__ = "estadov"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
class Usuario(Base):
    __tablename__= "usuario"
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    mail = Column(String, nullable=False)
    contrasena = Column(String, nullable=False)