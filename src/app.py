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

@app.route('/generar_reporte')
def generar_reporte():       
    return render_template('generar_reportes.html', titulo_pagina = "GENERAR REPORTE")

@app.route('/registro_exitoso')
def registro_exitoso():
    return render_template('solicitud_registrada_con_exito.html', titulo_pagina = "REGISTRO EXITOSO")

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


@app.route('/contratista_ordenes')
def contratista_ordenes():      
    usuarios = Usuario.obtener_datos_usuario()  
    return render_template('contratista_ordenes.html', titulo_pagina="CONTRATISTA ORDENES", usuarios=usuarios)


@app.route('/moviles_ordenes')
def moviles_ordenes():
    return render_template('moviles_ordenes.html', titulo_pagina = "MOVILES ORDENES")




@app.route('/registrar_falla', methods=['POST'])
def registrar_falla():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tipo_documento = request.form['tipo_documento']
    numero_documento = request.form['numero_documento']
    direccion_falla = request.form['direccion_falla']
    localidad = request.form['localidad']
    email = request.form.get('email')
    celular = request.form.get('celular')
    tipo_falla = request.form['tipo_falla']
    
    
    
    print(f"Datos recibidos: nombre={nombre}, apellido={apellido}, tipo_documento={tipo_documento}")    
       
    ultimo_orden_trabajo = session.query(Usuario).order_by(Usuario.orden_trabajo.desc()).first()
    nuevo_orden_trabajo = ultimo_orden_trabajo.orden_trabajo + 1 if ultimo_orden_trabajo else 1
    


    nuevo_usuario = Usuario(
        orden_trabajo=nuevo_orden_trabajo,
        fecha_reporte=datetime.datetime.now(),
        nombre=nombre,
        apellido=apellido,
        tipo_documento=tipo_documento,
        numero_documento=numero_documento,
        direccion_falla=direccion_falla,
        localidad=localidad,
        email=email,
        celular=celular,
        tipo_falla=tipo_falla        
    )
    
    print(f"Nuevo usuario creado: {nuevo_usuario.nombre}, Orden de trabajo: {nuevo_usuario.orden_trabajo}")

    with session.begin():
        session.add(nuevo_usuario)
        print("Nuevo usuario agregado a la base de datos")

    return redirect(url_for('registro_exitoso'))

if __name__ == '__main__':
    app.run(debug=True)
    
