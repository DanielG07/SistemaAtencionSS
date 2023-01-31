import os
from io import BytesIO
import xlsxwriter
from flask import Flask, redirect, render_template, request, url_for, send_file
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
        "numero": "-",
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
        "numero": "-",
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
        "numero": "-",
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
        "numero": "-",
        "registro_lista": "15",
        "f_envio": "01/01/2021",
    },
]

registro_mock = [
    {
        "boleta": "2019640295",
        "nombre": "Daniel González Jiménez",
        "carrera": "I. B.",
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
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERIA Y TECNOLOGIAS AVANZADAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/003",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640297",
        "nombre": "Joshep Irvin Camacho Dominguez",
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Femenino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "ACEPTADO",
        "numero": "21140/004",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640298",
        "nombre": "Guillermo Ian Rodriguez Mancera",
        "carrera": "I. B.",
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

completados_mock = [
    {
        "boleta": "2019640295",
        "nombre": "Daniel González Jiménez",
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCA UST",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "COMPLETADO",
        "numero": "21140/002",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640296",
        "nombre": "Jorge Angel Cruz Meneses",
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "UNIDAD PROFESIONAL INTERDISCIPLINARIA DE INGENIERIA Y TECNOLOGIAS AVANZADAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "COMPLETADO",
        "numero": "21140/003",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640297",
        "nombre": "Joshep Irvin Camacho Dominguez",
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Femenino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "COMPLETADO",
        "numero": "21140/004",
        "registro_lista": "15",
        "f_envio": "01/01/2021"
    },
    {
        "boleta": "2019640298",
        "nombre": "Guillermo Ian Rodriguez Mancera",
        "carrera": "I. B.",
        "semestre": "9",
        "genero": "Masculino",
        "prestatario": "ESCUELA SUPERIOR DE COMERCIO Y ADMINISTRACION, UNIDAD SANTO TOMAS",
        "f_inicio": "01/10/2021",
        "f_termino": "01/05/2022",
        "correo_electronico": "dgonzalezj1501@alumno.ipn.mx",
        "estatus": "COMPLETADO",
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
    if request.method == "POST":
        data = {
            'nombre': request.form['Idp-nombre'],
            'paterno': request.form['Idp-apellidoP'],
            'materno': request.form['Idp-apellidoM'],
            'boleta': request.form['Idp-Boleta'],
            'curp': request.form['Idp-CURP'],
            'carrera': request.form['Idp-carrera'],
            'clave_carrera': request.form['Idp-clave_carrera'],
            'id_carrera': '',
            'semestre': request.form['Idp-semestre'],
            'sexo': request.form['Idp-genero'],
            'id_sexo': '',
            'tel_particular':request.form['Idp-telefono'],
            'escolaridad':request.form['Idp-escolaridad'],
            'direccion':request.form['Idp-direccion'],
            'codigo_postal':request.form['Idp-codPostal'],
            'alcaldia':request.form['Idp-alcaldia'],
            'prestatario': request.form['Idp-prestatario'],
            'codigo': request.form['Idp-cod_prestatario'],
            'programa': request.form['Idp-programa'],
            'clave_programa':request.form['Idp-clave_programa'],
            'fecha_inicio': request.form['Idp-FInicio'],
            'fecha_termino': request.form['Idp-FTermino'],
            'correo': request.form['Idp-email'],
        }

        ## CARRERA
        if data['carrera']=='ESCA.UST CONTADOR PÚBLICO':
            data['id_carrera']=1
        if data['carrera']=='ESCA.UST LICENCIADO EN RELACIONES COMERCIALES':
            data['id_carrera']=2
        if data['carrera']=='ESCA.UST LICENCIADO EN NEGOCIOS INTERNACIONALES':
            data['id_carrera']=3
        if data['carrera']=='ESCA.UST LICENCIADO EN ADMINISTRACION Y DESARROLLO EMPRESARIAL':
            data['id_carrera']=4
        if data['carrera']=='ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL.':
            data['id_carrera']=5
        if data['carrera']=='ESCA.UST LICENCIADO EN COMERCIO INTERNACIONAL (SADE)':
            data['id_carrera']=6
        if data['carrera']=='ESCA.U.TEP. LICENCIADO EN NEGOCIOS INTERNACIONALES':
            data['id_carrera']=7
        ## SEXO
        if data['sexo']=='Masculino':
            data['id_sexo']=1
        if data['sexo']=='Femenino':
            data['id_sexo']=2

        print(data)
        error = False
        if data['semestre'] == '0':
            error=True
        if error== False:
            return "Registro Exitoso"
        else:
            error = "Por favor, rellene todos los campos"
            return render_template("confirmacion.html", data=data,error=error)
    
    return render_template("confirmacion.html",data=data ,error=error)

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
        #print(data)
        return render_template('confirmacion.html',data=data)  

@app.route('/admin', methods=['GET', 'POST'])
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

@app.route('/completados')
def completadosAdmin():
    data={
        'titulo':'Completados - Administrador'
    }
    return render_template('admin/completados.html',data=data, registros = completados_mock)


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

@app.route("/generar_preregistros")
def generarExcelPreregistro():
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(preregistro_mock)
    return apiResponse

@app.route("/generar_emision")
def generarExcelEmision():
    apiResponse = createApiResponse(registro_mock)
    return apiResponse

@app.route("/generar_completados")
def generarExcelCompletados():
    apiResponse = createApiResponse(completados_mock)
    return apiResponse

def createApiResponse(data):
    bufferFile = writeBufferExcelFile(data)
    mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    return send_file(bufferFile, mimetype=mimetype)

def writeBufferExcelFile(data):
    buffer = BytesIO()
    workbook = xlsxwriter.Workbook(buffer)
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', '#')
    worksheet.write('B1', 'REG NÚM')
    worksheet.write('C1', 'N DE BOLETA')
    worksheet.write('D1', 'APELLIDO PATERNO')
    worksheet.write('E1', 'APELLIDO MATERNO')
    worksheet.write('F1', 'NOMBRE (S)')
    worksheet.write('G1', 'GENERO')
    worksheet.write('H1', 'CLAVE CARRERA')
    worksheet.write('I1', 'MODALIDAD')
    index = 2
    for item in data:
        worksheet.write('A' + str(index), str(index - 2))
        worksheet.write('B' + str(index), item['numero'])
        worksheet.write('C' + str(index), item['boleta'])
        worksheet.write('D' + str(index), item['nombre'])
        worksheet.write('E' + str(index), item['nombre'])
        worksheet.write('F' + str(index), item['nombre'])
        worksheet.write('G' + str(index), item['genero'])
        worksheet.write('H' + str(index), item['carrera'])
        worksheet.write('I' + str(index), item['correo_electronico'])
        index = index + 1
    workbook.close()
    buffer.seek(0)
    return buffer

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



