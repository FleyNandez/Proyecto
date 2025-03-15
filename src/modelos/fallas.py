from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum

class Falla(Base):
    __tablename__ = "Fallas"
    id = Column (Integer, primary_key = True)
    direccion_falla = Column (String(300), unique = True, nullable = False)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)
    localidad = Column (Enum(LocalidadEnum), unique = True, nullable = False)
    
    
    
    
    def __init__(self, direccion_falla,tipo_falla, localidad):
        
        self.direccion_falla = direccion_falla
        self.tipo_falla = tipo_falla
        self.localidad = localidad
        
  
    @staticmethod
    def obtener_datos_falla():
        with Session() as session:
            fallas = session.query(Falla).all()               
        return fallas
    
  
    

  
  