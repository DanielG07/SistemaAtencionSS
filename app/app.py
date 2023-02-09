import os
from datetime import datetime
from sqlalchemy import Date
from flask import Flask, redirect, render_template, request, url_for, send_file
from utils.funcion_excel import createApiResponse
from utils.mocks import preregistro_mock, registro_mock, completados_mock
from flask_sqlalchemy import SQLAlchemy
from utils.funcion_correo import enviar_correo
from werkzeug.utils import secure_filename
from lee_pdf import lectura

#server='DESKTOP-A8TJQDL\SQLEXPRESS01'  #PARA JOSHEP
server='LAPTOP-9T4B4IDA' #PARA J CRUZ
bd='Sistema_Atencion_SS'
user='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "./app/pdfs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://' + user + ':' + password + '@' + server + '/' + bd + '?driver=ODBC+Driver+17+for+SQL+Server'

# CONEXIÓN A LA BASE DE DATOS
try:
    db = SQLAlchemy(app)
    print("Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)

# MODELO PARA LA TABLA "DATA_USERS"

class UserModel(db.Model):
    __tablename__ = 'DATA_USERS'
    id = db.Column(db.Integer, primary_key=True, name='Id_data_users')
    nombre = db.Column(db.String(40), nullable=True, name='Nombre')
    a_paterno = db.Column(db.String(40), nullable=True, name='A_Paterno')
    a_materno = db.Column(db.String(40), nullable=True, name='A_Materno')
    curp = db.Column(db.String(30), nullable=True, name='CURP')
    boleta = db.Column(db.String(25), nullable=True, name='Boleta')
    id_sexo = db.Column(db.Integer, name='Id_Sexo')
    id_plantel = db.Column(db.Integer, name='Id_Plantel')
    cp = db.Column(db.String(30), nullable=True, name='CP')
    telefono = db.Column(db.String(30), nullable=True, name='Tel_particular')
    direccion =  db.Column(db.String(max), nullable=True, name='Direccion')
    alcaldia =  db.Column(db.String(75), nullable=True, name='Alcaldia')
    escolaridad = db.Column(db.String(10), nullable=True, name='Escolaridad')
    correo = db.Column(db.String(50), nullable=True, name='Correo')
    id_carrera = db.Column(db.Integer, name='Id_carrera')
    prestatario = db.Column(db.String(max), nullable=True, name='Prestatario')
    codigo_prestatario = db.Column(db.String(30), nullable=True, name='Codigo_Prestatario')
    responsable = db.Column(db.String(75), nullable=True, name='Responsable')
    programa = db.Column(db.String(max), nullable=True, name='Programa')
    clave_programa = db.Column(db.String(30), nullable=True, name='Clave_programa')
    cargo = db.Column(db.String(75), nullable=True, name='Cargo')
    tel_responsable = db.Column(db.String(40), nullable=True, name='Tel_responsable')
    fecha_registro = db.Column(db.Date, name='Fecha_registro')
    fecha_inicio = db.Column(db.Date, name='Fecha_inicio')
    fecha_termino = db.Column(db.Date, name='Fecha_termino')
    correo_prestatario = db.Column(db.String(50), nullable=True, name='Correo_prestatario')
    ubicacion_calleynum = db.Column(db.String(75), nullable=True, name='Ubicacion_calleynum')
    ubicacion_colonia = db.Column(db.String(75), nullable=True, name='Ubicacion_colonia')
    ubicacion_alcaldia = db.Column(db.String(75), nullable=True, name='Ubicacion_alcaldia')
    ubicacion_codpos = db.Column(db.String(30), nullable=True, name='Ubicacion_codpos')

# INSERCION DE DATOS DEL ALUMNO

def insertar_registro(data):
    
    print(data)
    i_platel=int(data['plantel'])
    data['plantel'] = i_platel

    aux=data['fecha_registro']
    aux2=data['fecha_inicio']
    aux3=data['fecha_termino']

    print(aux)
    print(aux2)
    print(aux3)

    f_registro = datetime.strptime(aux, "%Y-%m-%d")
    f_inicio = datetime.strptime(aux2, "%Y-%m-%d")
    f_termino = datetime.strptime(aux3, "%Y-%m-%d")

    data['fecha_registro'] = f_registro
    data['fecha_inicio'] = f_inicio
    data['fecha_termino'] = f_termino


    print(type(data['fecha_registro']))
    print(type(data['fecha_inicio']))
    print(type(data['fecha_termino']))

    try:
        new_user = UserModel(
            nombre=data['nombre'],
            a_paterno=data['paterno'],
            a_materno=data['materno'],
            curp=data['curp'],
            boleta=data['boleta'],
            id_sexo=data['id_sexo'],
            id_plantel=data['plantel'],
            cp=data['codigo_postal'],
            telefono=data['tel_particular'],
            direccion=data['direccion'],
            alcaldia=data['alcaldia'],
            escolaridad=data['escolaridad'],
            correo=data['correo'],
            id_carrera=data['id_carrera'],
            prestatario=data['prestatario'],
            codigo_prestatario=data['codigo'],
            responsable=data['responsable'],
            programa=data['programa'],
            clave_programa=data['clave_programa'],
            cargo=data['cargo'],
            tel_responsable=data['tel_responsable'],
            fecha_registro=data['fecha_registro'],
            fecha_inicio=data['fecha_inicio'],
            fecha_termino=data['fecha_termino'],
            correo_prestatario=data['correo_prestatario'],
            ubicacion_calleynum=data['ubicacion_calleynum'],
            ubicacion_colonia=data['ubicacion_colonia'],
            ubicacion_alcaldia=data['ubicacion_alcaldia'],
            ubicacion_codpos=data['ubicacion_codpos'],
        )
        db.session.add(new_user)
        db.session.commit()
        print("Registro insertado exitosamente")
    except Exception as e:
        print("Error al insertar el registro: ", e)
        db.session.rollback()



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
            'titulo1': request.form['Idp-titulo'],
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
            'correo': request.form['Idp-email'],
            'tel_particular':request.form['Idp-telefono'],
            'escolaridad':request.form['Idp-escolaridad'],
            'direccion':request.form['Idp-direccion'],
            'codigo_postal':request.form['Idp-codPostal'],
            'alcaldia':request.form['Idp-alcaldia'],
            'prestatario': request.form['Idp-prestatario'],
            'codigo': request.form['Idp-cod_prestatario'],
            'programa': request.form['Idp-programa'],
            'clave_programa':request.form['Idp-clave_programa'],
            'fecha_registro':request.form['Idp-FActual'],
            'fecha_inicio': request.form['Idp-FInicio'],
            'fecha_termino': request.form['Idp-FTermino'],
            'responsable':request.form['Idp-responsable'],
            'cargo':request.form['Idp-cargo'],
            'tel_responsable':request.form['Idp-tel-responsable'],
            'correo_prestatario':request.form['Idp-correo_prestatario'],
            'ubicacion_calleynum':request.form['Idp-Calleynum'],
            'ubicacion_colonia':request.form['Idp-Colonia'],
            'ubicacion_alcaldia':request.form['Idp-Alcaldia_prestatario'],
            'ubicacion_codpos':request.form['Idp-cpPrestatario'],
            'contrasena':request.form['Idp-contraseña'],
            'confirmarcontrasena':request.form['Idp-Confirmar-contraseña'],
            'plantel':'140',
            
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
        errorcontrasena = False
        if data['contrasena']!=data['confirmarcontrasena']:
            errorcontrasena=True

        if  errorcontrasena==False:
            insertar_registro(data)
            return "Registro Exitoso"
        else:
            errorcontrasena = "Las contraseñas deben ser iguales"
            return render_template("confirmacion.html", data=data, errorcontrasena=errorcontrasena)
    
    return render_template("confirmacion.html",data=data ,errorcontrasena=errorcontrasena)

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
        errorcarta = "Debe seleccionar una carta compromiso válida"
        print(data)
        if data['titulo1']=="INSTITUTO POLITÉCNICO NACIONAL":
            return render_template('confirmacion.html',data=data)
        else:
            print(errorcarta)
            return render_template('registro.html',data=data,errorcarta=errorcarta)
          

@app.route('/admin', methods=['GET', 'POST'])
def indexAdmin():
    data={
        'titulo':'Administrador'
    }
    return render_template('admin/main.html',data=data)

@app.route('/admin/expedientes')
def reportesAdmin():
    data={
        'titulo':'Expedientes - Administrador'
    }
    return render_template('admin/expedientes.html',data=data, registros = registro_mock)

@app.route('/admin/completados')
def completadosAdmin():
    data={
        'titulo':'Completados - Administrador'
    }
    return render_template('admin/completados.html',data=data, registros = completados_mock)


@app.route('/admin/preregistros')
def preregistrosAdmin():
    data={
        'titulo':'Preregistros - Administrador'
    }
    return render_template('admin/preregistros.html',data=data, registros = preregistro_mock)

@app.route('/admin/estadisticas')
def estadisticasAdmin():
    data={
        'titulo':'Estadisitcas Reportes'
    }
    return render_template('admin/estadisticas.html',data=data)

@app.route("/admin/generar_preregistros")
def generarExcelPreregistro():
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(preregistro_mock)
    return apiResponse

@app.route("/admin/generar_emision")
def generarExcelEmision():
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(registro_mock)
    return apiResponse

@app.route("/admin/generar_completados")
def generarExcelCompletados():
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(completados_mock)
    return apiResponse

@app.route("/admin/expediente/<boleta>")
def expedienteAlumno(boleta=0):
    data={
        'titulo':'Expediente - ' + boleta
    }
    # enviar_correo("jorgecruzmen2000@gmail.com", "Expediente aceptado.", "carta término")
    # Traer datos del usuario con la boleta asignada
    expediente = {}
    for item in registro_mock:
        if item.get("boleta") == boleta:
            expediente = item
            break

    return render_template('admin/perfilAlumno.html',data=data, expediente=expediente, registros = preregistro_mock)

@app.route("/reporte/<periodo>")
def generarReporte(periodo):
    if periodo == "semanal":
        print("Semanal")
    elif periodo == "mensual":
        print("mensual")
    elif periodo == "trimestral":
        print("trimestral")
    elif periodo == "semestral":
        print("semestral")
    return send_file() # Enviar archivo de reporte correspondiente

@app.route('/estudiante/<boleta>', methods=['GET', 'POST'])
def indexEstudiante(boleta):
    data={
        'titulo' : 'Alumno'
    }
    return render_template('estudiante/main.html', data=data)

@app.route('/estudiante/expediente/<boleta>', methods=['GET'])
def expedienteEstudiante(boleta):
    data={
        'titulo' : 'Alumno - Expediente'
    }
    # Buscar información del estudiante y mandarlo para pintar
    expediente = {}
    for item in registro_mock:
        if item.get("boleta") == boleta:
            expediente = item
            break
    return render_template('estudiante/expediente.html', data=data, expediente=expediente)

@app.route('/estudiante/perfil/<boleta>', methods=['GET'])
def perfilEstudiante(boleta):
    data={
        'titulo' : 'Alumno - Perfil'
    }
    # Buscar información del estudiante y mandarlo para pintar
    expediente = {}
    for item in registro_mock:
        if item.get("boleta") == boleta:
            expediente = item
            break
    return render_template('estudiante/perfil.html', data=data, expediente=expediente)



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



