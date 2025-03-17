from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from src.modelos import Session, Base 
from .mis_enums import TipoFallaEnum, LocalidadEnum, MovilEnum

from src.modelos.usuario import Usuario



class orden_trabajo(Base):
    __tablename__ = "Orden_Trabajo"
    id = Column(Integer, ForeignKey("Usuario.id"), primary_key=True)
    direccion_falla = Column (String(300), unique = True, nullable = False)
    localidad = Column (Enum(LocalidadEnum), unique = True, nullable = False)
    tipo_falla = Column (Enum(TipoFallaEnum), unique = True, nullable = False)    
    movil = Column (Enum(MovilEnum),nullable=True) 
    
    
    
    def __init__(self, id, direccion_falla,localidad,tipo_falla, movil_id=None):
        
        self.id = id
        self.direccion_falla = direccion_falla        
        self.localidad = localidad
        self.tipo_falla = tipo_falla
        self.movil_id = movil_id
    
    
    @staticmethod
    def obtener_datos_orden():
        with Session() as session:
            ordenes = session.query(Usuario).all()                            
        return ordenes
    
        
    @staticmethod
    def asignar_movil(orden_trabajo_id, movil):
      with Session() as session:
            orden = session.query(Usuario).all()
            if orden:
                orden_trabajo.movil = movil 
                session.commit() 
                return True
            else:
                print(f"No se encontró la orden para el ID de usuario: {orden_trabajo_id}")
                return False
      
       
    @staticmethod
    def obtener_ordenes_por_movil(movil):
     with Session() as session:
        ordenes = session.query(orden_trabajo).filter_by(movil=movil).all()
     return ordenes
    
    

    

                

                

  


   
    


    