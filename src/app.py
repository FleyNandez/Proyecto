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
    




@app.route('/registro_exitoso')
def registro_exitoso():
    id = request.args.get('id')
    return render_template('solicitud_registrada_con_exito.html', titulo_pagina = "REGISTRO EXITOSO", id=id)




@app.route('/consultar')
def consultar():
    return render_template('consultar.html', titulo_pagina = "CONSULTAR")

@app.route('/solicitud_en_curso')
def solicitud_en_curso():
    return render_template('solicitud_en_curso.html', titulo_pagina = "SOLICITUD EN CURSO")

@app.route('/quienes_somos')
def quienes_somos ():
    return render_template('quienes_somos.html', titulo_pagina = "QUIENES SOMOS")

@app.route('/MOD')
def MOD ():
    return render_template('MOD.html', titulo_pagina = "MOD")

@app.route('/contratista')
def contratista():
    return render_template('contratista.html', titulo_pagina = "contratista")

@app.route('/moviles')
def moviles():
    return render_template('moviles.html', titulo_pagina = "moviles")

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


@app.route('/orden_trabajo')
def ordenes():      
    usuarios = Usuario.obtener_datos_usuario()     
    return render_template('orden_trabajo.html', titulo_pagina="ORDEN TRABAJO", usuarios=usuarios)


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




