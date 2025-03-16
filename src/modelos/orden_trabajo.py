from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum
from sqlalchemy.orm import relationship


class orden_trabajo(Base):
    __tablename__ = "Orden_Trabajo"
    id = Column(Integer, ForeignKey("Usuario.id"), primary_key=True)
    direccion_falla = Column (String(300), unique = True, nullable = False)
    localidad = Column (Enum(LocalidadEnum), unique = True, nullable = False)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)    
    movil = Column (Enum(MovilEnum),nullable=True) 
    
    usuario = relationship("Usuario", back_populates="orden_trabajo")
    
    
    
    def __init__(self, direccion_falla,localidad,tipo_falla, movil):
        
        self.direccion_falla = direccion_falla        
        self.localidad = localidad
        self.tipo_falla = tipo_falla
        self.movil = movil
    
    
    @staticmethod
    def asignar_movil(usuario_id, movil):
        with Session() as session:
            # Buscar la orden vinculada al usuario
            orden = session.query(orden_trabajo).filter_by(id=usuario_id).first()
            if orden:
                orden.movil = movil  # Asignar el móvil
                session.commit()  # Guardar los cambios
                return True
            else:
                print(f"No se encontró la orden para el ID de usuario: {usuario_id}")
                return False
        

                

                

  


   
    


    