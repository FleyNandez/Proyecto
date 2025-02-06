from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as PyEnum 

Base = declarative_base()

class TipoDocumentoEnum(PyEnum):
    opcion_1 = "cedula ciudadania"
    opcion_2 = "cedula extranjera"

class LocalidadEnum(PyEnum):
    opcion_1 = "Usaquén"
    opcion_2 = "Chapinero"
    opcion_3 = "Santa Fe"
    opcion_4 = "San Cristóbal"
    opcion_5 = "Usme"
    opcion_6 = "Tunjuelito"
    opcion_7 = "Bosa"
    opcion_8 = "Kennedy"
    opcion_9 = "Fontibón"
    opcion_10 = "Engativá"
    opcion_11 = "Suba"
    opcion_12 = "Barrios Unidos"
    opcion_13 = "Teusaquillo"
    opcion_14 = "Mártires"
    opcion_15 = "Antonio Nariño"
    opcion_16 = "Puente Aranda"
    opcion_17 = "Candelaria"
    opcion_18 = "Rafael Uribe Uribe"
    opcion_19 = "Ciudad Bolívar"
    opcion_20 = "Sumapaz"

class TipoFallaEnum(PyEnum):
    opcion_1 = "luminaria hurtada"
    opcion_2 = "sector sin alumbrado"
    opcion_3 = "cables sueltos"
    opcion_4 = "poste en mal estado"
    opcion_5 = "Solicitud luminaria nueva"
    
class MovilEnum(PyEnum):
    opcion_1 = "liviano"
    opcion_2 = "canasta"
    opcion_3 = "subterraneo"
    
class MovilEnum(PyEnum):
    opcion_1 = "Liviano-Fleyder Hernandez"
    opcion_2 = "Canasta-Jimmy Otalora"
    opcion_3 = "Subterraneo-Fabian Lopez"