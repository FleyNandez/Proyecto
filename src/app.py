
from flask import Flask, render_template
from src.modelos import Base, engine 
from src.modelos.usuario import Usuario
from src.modelos.orden_trabajo import orden_trabajo
from src.modelos.movil import Movil
from src.modelos.fallas import Falla


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

@app.route('/generar_reporte')
def nuevo_registro():
    return render_template('generar_reportes.html', titulo_pagina = "GENERAR REPORTE")

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
    return render_template('contratista_ordenes.html', titulo_pagina = "contratista_ordenes")

@app.route('/moviles_ordenes')
def moviles_ordenes():
    return render_template('moviles_ordenes.html', titulo_pagina = "moviles_ordenes")

