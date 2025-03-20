from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum

from src.modelos.usuario import Usuario
from sqlalchemy.orm import relationship



class Orden_Trabajo(Base):
    __tablename__ = "Orden_Trabajo"
    id = Column(Integer, ForeignKey("Usuario.id"), primary_key=True)
    direccion_falla = Column(String(300), unique=False, nullable=False)
    localidad = Column(Enum(LocalidadEnum), unique=False, nullable=False)
    tipo_falla = Column(Enum(TipoFallaEnum), unique=False, nullable=False)    
    movil = Column(Enum(MovilEnum), nullable=True) 
    
    usuario = relationship("Usuario", back_populates="ordenes_trabajo")
    

    def __init__(self, id, direccion_falla, localidad, tipo_falla, movil=None):
        self.id = id
        self.direccion_falla = direccion_falla
        self.localidad = localidad
        self.tipo_falla = tipo_falla
        self.movil = movil

    @staticmethod
    def obtener_datos_orden():
        with Session() as session:
            ordenes = session.query(Orden_Trabajo).all()  # Debes obtener datos de la tabla Orden_Trabajo
        return ordenes

    @staticmethod
    def asignar_movil(orden_trabajo_id, movil):
        with Session() as session:
            orden_trabajo = session.query(Orden_Trabajo).filter_by(id=orden_trabajo_id).first()
            
            if orden_trabajo:
                orden_trabajo.movil = movil  # Asignar el móvil a la orden
                session.commit()  # Guardar cambios en la base de datos
                return True
            else:
                print(f"No se encontró la orden para el ID de usuario: {orden_trabajo_id}")
                return False

    @staticmethod
    def obtener_ordenes_por_movil(movil):
        with Session() as session:
            ordenes = session.query(Orden_Trabajo).filter_by(movil=movil).all()
        return ordenes
    

    
    
