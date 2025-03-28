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



class MovilController(FlaskController):
    
    
 @app.route('/login', methods=['POST'])
 def login():
    
    username = request.form.get('username')
    
    if username == "movil_1":
        return redirect(url_for('movil_liviano'))
    elif username == "movil_2":
        return redirect(url_for('movil_canasta'))
    elif username == "movil_3":
        return redirect(url_for('movil_subterraneo'))
    
    
 @app.route('/movil_liviano')
 def movil_liviano():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_1")
    print(ordenes)
    return render_template('movil_liviano.html', titulo_pagina="Movil Liviano", ordenes=ordenes)

 @app.route('/movil_canasta')
 def movil_canasta():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_2")
    return render_template('movil_canasta.html', titulo_pagina="Movil Canasta", ordenes=ordenes)

 @app.route('/movil_subterraneo')
 def movil_subterraneo():
    ordenes = Orden_Trabajo.obtener_ordenes_por_movil("movil_3")
    return render_template('movil_subterraneo.html', titulo_pagina="Movil Subterraneo", ordenes=ordenes)


@app.route('/moviles_ordenes', methods=['POST', 'GET'])
def moviles_ordenes():
    if request.method == 'POST':
        orden_trabajo_id = request.form.get('usuario_id')
        movil_id = request.form.get('movil') 
        
        
        asignado = Orden_Trabajo.asignar_movil(orden_trabajo_id, movil_id)

        if asignado:
            print(f"Orden asignada al móvil {movil_id}.")
        else:
            print(f"No se pudo asignar la orden para el usuario con ID {orden_trabajo_id}.")
    
    usuarios = Usuario.obtener_datos_usuario()
    return render_template('orden_trabajo.html', titulo_pagina="Ordenes de Trabajo", usuarios=usuarios)
