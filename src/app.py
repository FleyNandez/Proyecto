from flask import Flask, render_template
from src.modelos import Base, engine, session
from src.modelos.usuario import Usuario
from src.modelos.contratista import Contratista
from src.modelos.orden_trabajo import orden_trabajo
from src.modelos.movil import Movil
from src.modelos.fallas import Falla
from src.modelos.mis_enums import TipoDocumentoEnum, TipoFallaEnum, LocalidadEnum
from flask import request, redirect, url_for
import datetime



app =Flask(__name__)

Base.metadata.create_all(engine)

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/')
def index():
    return render_template('index.html', titulo_pagina = "INICIO")

@app.route('/generar_reporte', methods = ['POST', 'GET'])
def generar_reporte():       
    if request.method == 'POST':
        nombre = request.form.get('nombre')
        apellido = request.form.get('apellido')
        tipo_documento = request.form.get('tipo_documento')
        numero_documento = request.form.get('numero_documento')
        direccion_falla = request.form.get('direccion_falla')
        localidad = request.form.get('localidad')
        email = request.form.get('email')
        celular = request.form.get('celular')
        tipo_falla = request.form.get('tipo_falla')       
                              
        usuario = Usuario (nombre,apellido,tipo_documento,numero_documento,direccion_falla,localidad,email,celular,tipo_falla)
        Usuario.agregar_datos_usuario(usuario)
        return redirect(url_for('registro_exitoso'))
    return render_template('generar_reportes.html', titulo_pagina = "GENERAR REPORTE")

@app.route('/registro_exitoso')
def registro_exitoso():
    id = request.args.get('id')
    return render_template('solicitud_registrada_con_exito.html', titulo_pagina = "REGISTRO EXITOSO", id=id)

@app.route('/inicio')
def inicio():
    return render_template('index.html', titulo_pagina = "INICIO")


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

@app.route('/moviles_ordenes', methods = ['POST', 'GET'])
def moviles_ordenes():
    fallas = Falla.obtener_datos_falla() 
    return render_template('moviles_ordenes.html', titulo_pagina = "Fallas", fallas=fallas)


@app.route('/orden_trabajo')
def orden():      
    usuarios = Usuario.obtener_datos_usuario()     
    return render_template('orden_trabajo.html', titulo_pagina="ORDEN TRABAJO", usuarios=usuarios)

    
