from src.app import app 
from flask import render_template, request, redirect, url_for
from flask_controller import FlaskController
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import Orden_Trabajo
from src.modelos.movil import Movil
from src.modelos.ordenes_cerradas import Ordenes_Cerradas
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from src.modelos import Base, engine, session


class Orden_TrabajoController(FlaskController):
    

 @app.route('/orden_trabajo')
 def ordenes():      
    usuarios = Usuario.obtener_datos_usuario()     
    return render_template('orden_trabajo.html', titulo_pagina="ORDEN TRABAJO", usuarios=usuarios)

