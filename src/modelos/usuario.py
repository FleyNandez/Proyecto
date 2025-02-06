from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
import datetime
from sqlalchemy.ext.declarative import declarative_base
from .mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos import Session, Base 


class Usuario(Base):
    __tablename__ = "Usuario"
    id = Column (Integer, primary_key = True)
    orden_trabajo = Column (Integer, ForeignKey("Orden_Trabajo.id"), nullable = False)
    fecha_reporte = Column(DateTime, default=datetime.datetime, nullable=False)
    nombre = Column (String, nullable=False)
    apellido = Column (String, nullable=False)
    tipo_documento = Column (Enum(TipoDocumentoEnum), nullable=False)
    numero_documento = Column (String(20), nullable=False )
    direccion_falla = Column (String(100), nullable=False)
    email = Column (String)
    celular = Column (String)
    tipo_falla = Column (ForeignKey("Falla.id"), unique = True, nullable = False)
    localidad = Column (Enum(LocalidadEnum), unique = True, nullable = False)     
      
    
       
    def __init__(self, orden_trabajo, fecha_reporte, nombre, apellido, tipo_documento, numero_documento, direccion_falla,email, celular, tipo_falla, localidad):
        
        self.orden_trabajo = orden_trabajo
        self.fecha_reporte = fecha_reporte
        self.nombre = nombre
        self.apellido = apellido
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        self.direccion_falla = direccion_falla
        self.email = email
        self.celular = celular
        self.tipo_falla = tipo_falla
        self.localidad = localidad