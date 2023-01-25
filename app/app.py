import os
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from lee_pdf import lectura

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "./app/pdfs"

preregistro_mock = [
    {
        "boleta": "2019640295",
        "nombre": "Daniel González Jiménez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCA UST",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/002",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640296",
        "nombre": "Jorge Angel Cruz Meneses",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERIA Y TECNOLOGIAS AVANZADAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/030",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640297",
        "nombre": "Joshep Irvin Camacho Dominguez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Femenino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "RECHAZADO",
        "numero": "21140/008",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640298",
        "nombre": "Guillermo Ian Rodriguez Mancera",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ESPERA",
        "numero": "21140/005",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
]

registro_mock = [
    {
        "boleta": "2019640295",
        "nombre": "Daniel González Jiménez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCA UST",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/002",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640296",
        "nombre": "Jorge Angel Cruz Meneses",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERIA Y TECNOLOGIAS AVANZADAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/030",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640297",
        "nombre": "Joshep Irvin Camacho Dominguez",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Femenino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/008",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640298",
        "nombre": "Guillermo Ian Rodriguez Mancera",
        "carrera": "I. T.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/005",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
]

@app.route('/')
def index():
    data={
        'titulo':'Sistema Servicio Social'
    }
    return render_template('index.html',data=data)

@app.route('/registro')
def registroUsuario():
    data={
        'titulo':'Registro'
    }
    return render_template('registro.html',data=data)

@app.route('/registro', methods=['POST'])
def registro():
    data = {
        'nombre': request.form['Idp-nombre'],
        'apellidoM': request.form['Idp-apellidoP'],
        'apellidoP': request.form['Idp-apellidoM'],
        'boleta': request.form['Idp-Boleta'],
        'curp': request.form['Idp-CURP'],
        'clave_carrera': request.form['Idp-c_carrera'],
        'carrera': request.form['Idp-carrera'],
        'semestre': request.form['Idp-semestre'],
        'genero': request.form['Idp-genero'],
        'prestatario': request.form['Idp-prestatario'],
        'programa': request.form['Idp-programa'],
        'fecha_inicio': request.form['Idp-FInicio'],
        'fecha_fin': request.form['Idp-FTermino'],
        'correo': request.form['Idp-email'],
    }
    print(data)

    return redirect(url_for("index"))

@app.route("/confirmacion_datos", methods=['POST'])
def uploader():
    if request.method == "POST":
        f = request.files['archivo']
        filename= secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOADER_FOLDER'],filename))
        print(filename)
        ruta = './app/pdfs/'+ filename
        print(ruta)
        registro = lectura(ruta)
        data=registro
        print(data)
        return render_template('confirmacion.html',data=data)  

@app.route('/admin')
def indexAdmin():
    data={
        'titulo':'Administrador'
    }
    return render_template('admin/main.html',data=data)

@app.route('/expedientes')
def reportesAdmin():
    data={
        'titulo':'Expedientes - Administrador'
    }
    return render_template('admin/expedientes.html',data=data, registros = registro_mock)


@app.route('/preregistros')
def preregistrosAdmin():
    data={
        'titulo':'Preregistros - Administrador'
    }
    return render_template('admin/preregistros.html',data=data, registros = preregistro_mock)

@app.route('/estadisticas')
def estadisticasAdmin():
    data={
        'titulo':'Estadisitcas Reportes'
    }
    return render_template('admin/estadisticas.html',data=data)


#PRUEBAS PARA INICIO DE SESION SIN BASE DE DATOS#
@app.route('/inicio', methods=['POST'])
def inicio():
    data = {
        'boleta': request.form['boleta'],
        'contrasena': request.form['contrasena']
    }
    print(data)

    return render_template('inicio.html',data=data)

if __name__== '__main__':
    app.run(debug=True,port=5000)



