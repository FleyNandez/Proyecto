from flask import Flask, render_template
app =Flask(__name__)

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
