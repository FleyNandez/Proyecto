from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 

class Falla(Base):
    __tablename__ = "Falla"
    id = Column (Integer, primary_key = True)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)
    orden_trabajo = Column (Integer, ForeignKey("orden_trabajo.id"), nullable = False) 
    
Base = declarative_base()

class TipoFallaEnum(str, Enum):
    opcion_1 = "luminaria hurtada"
    opcion_2 = "sector sin alumbrado"
    opcion_3 = "cables sueltos"
    opcion_4 = "poste en mal estado"
    opcion_5 = "Solicitud luminaria nueva"
  
  