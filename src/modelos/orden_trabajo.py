from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class orden_trabajo():
    __tablename__ = "orden_trabajo"
    id = Column (Integer, primary_key = True)
    direccion_falla = Column (String(300), unique = True, nullable = False)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)
    localidad = Column (Enum(localidad), unique = True, nullable = False)
    movil = Column (Enum(movil), ForeignKey("movil.id"), nullable = False) 
    


    ForeignKey