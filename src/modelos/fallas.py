from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum

class Falla(Base):
    __tablename__ = "Falla"
    id = Column (Integer, primary_key = True)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)
    orden_trabajo = Column (Integer, ForeignKey("Orden_Trabajo.id"), nullable = False) 
    
        
    
    def __init__(self, tipo_falla, orden_trabajo):
        
        self.tipo_falla = tipo_falla
        self.orden_trabajo = orden_trabajo
  
  
    

  
  