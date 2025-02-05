from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from enums import MovilEnum

class Movil():
    __tablename__ = "Movil"
    id = Column (Integer, primary_key = True)
    clase_movil = Column (Enum(MovilEnum), unique = True, nullable = False)
    orden_trabajo = Column (Integer, ForeignKey("orden_trabajo.id"), nullable = False) 