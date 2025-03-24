from flask import Flask, render_template
from flask_controller import FlaskControllerRegister
from src.modelos import Base, engine, session
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import Orden_Trabajo
from src.modelos.movil import Movil
from src.modelos.fallas import Falla
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from flask import request, redirect, url_for
import datetime



app =Flask(__name__)

Base.metadata.create_all(engine)

register = FlaskControllerRegister(app)
register.register_package('src.controllers')

if __name__ == '__main__':
    app.run(debug=True)
    

