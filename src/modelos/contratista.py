
# este seria una especie de administrador del sistema, seguir viendo grabaciones para saber como ajustarlo

from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos import Session, Base 

