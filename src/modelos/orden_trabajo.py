from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum


class orden_trabajo(Base):
    __tablename__ = "Orden_Trabajo"
    id = Column (Integer, primary_key = True)
    direccion_falla = Column (String(300), unique = True, nullable = False)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)
    localidad = Column (Enum(LocalidadEnum), unique = True, nullable = False)
    movil = Column (Enum(MovilEnum),ForeignKey("Movil.movil"), nullable = False) 
    
    
    
    def __init__(self, direccion_falla,tipo_falla, localidad, movil):
        
        self.direccion_falla = direccion_falla
        self.tipo_falla = tipo_falla
        self.localidad = localidad
        self.movil = movil
    


   
    


    