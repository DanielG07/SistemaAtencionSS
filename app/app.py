import os
from datetime import datetime
from sqlalchemy import Date
from flask import Flask, redirect, render_template, request, url_for, send_file, session
from flask_session import Session
from utils.funcion_excel import createApiResponse
from utils.mocks import preregistro_mock, registro_mock, completados_mock
from flask_sqlalchemy import SQLAlchemy
from utils.funcion_correo import enviar_correo
from werkzeug.utils import secure_filename
from lee_pdf import lectura
import hashlib

#server='DESKTOP-A8TJQDL\SQLEXPRESS01'  #PARA JOSHEP
server='LAPTOP-9T4B4IDA' #PARA J CRUZ
bd='Sistema_Atencion_SS'
user='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "./app/pdfs"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://' + user + ':' + password + '@' + server + '/' + bd + '?driver=ODBC+Driver+17+for+SQL+Server'
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = 'mysecretkey'
Session(app)

# CONEXIÓN A LA BASE DE DATOS
try:
    db = SQLAlchemy(app)
    print(" * Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)

class Users(db.Model):
    __tablename__ = 'USERS'
    id = db.Column(db.Integer, primary_key=True, name='Id_user')
    boleta = db.Column(db.String(25), nullable=True, name='boleta')
    passw = db.Column(db.LargeBinary(), nullable=False,name = 'passw')
    Tipo_user = db.Column(db.Integer, nullable=False,name='Tipo_user')
    Id_Estatus_user = db.Column(db.Integer, nullable=False, name='Id_Estatus_user')  

# MODELO PARA LA TABLA "DATA_USERS"
class DataUsers(db.Model):
    __tablename__ = 'DATA_USERS'
    id = db.Column(db.Integer, primary_key=True, name='Id_data_users')
    user_id = db.Column(db.Integer, name='user_id')
    nombre = db.Column(db.String(40), nullable=True, name='Nombre')
    a_paterno = db.Column(db.String(40), nullable=True, name='A_Paterno')
    a_materno = db.Column(db.String(40), nullable=True, name='A_Materno')
    curp = db.Column(db.String(30), nullable=True, name='CURP')
    boleta = db.Column(db.String(25), nullable=True, name='Boleta')
    id_sexo = db.Column(db.Integer,nullable=True,name='Id_Sexo')
    id_plantel = db.Column(db.Integer,nullable=True,name='Id_Plantel')
    cp = db.Column(db.String(30), nullable=True, name='CP')
    telefono = db.Column(db.String(30), nullable=True, name='Tel_particular')
    direccion =  db.Column(db.String(500), nullable=True, name='Direccion')
    alcaldia =  db.Column(db.String(75), nullable=True, name='Alcaldia')
    escolaridad = db.Column(db.String(10), nullable=True, name='Escolaridad')
    correo = db.Column(db.String(50), nullable=True, name='Correo')
    id_carrera = db.Column(db.Integer, nullable=True,name='Id_carrera')
    prestatario = db.Column(db.String(500), nullable=True, name='Prestatario')
    codigo_prestatario = db.Column(db.String(30), nullable=True, name='Codigo_Prestatario')
    responsable = db.Column(db.String(75), nullable=True, name='Responsable')
    programa = db.Column(db.String(500), nullable=True, name='Programa')
    clave_programa = db.Column(db.String(30), nullable=True, name='Clave_programa')
    cargo = db.Column(db.String(75), nullable=True, name='Cargo')
    tel_responsable = db.Column(db.String(40), nullable=True, name='Tel_responsable')
    fecha_registro = db.Column(db.Date, nullable=True, name='Fecha_registro')
    fecha_inicio = db.Column(db.Date, nullable=True, name='Fecha_inicio')
    fecha_termino = db.Column(db.Date, nullable=True, name='Fecha_termino')
    correo_prestatario = db.Column(db.String(50), nullable=True, name='Correo_prestatario')
    ubicacion_calleynum = db.Column(db.String(75), nullable=True, name='Ubicacion_calleynum')
    ubicacion_colonia = db.Column(db.String(75), nullable=True, name='Ubicacion_colonia')
    ubicacion_alcaldia = db.Column(db.String(75), nullable=True, name='Ubicacion_alcaldia')
    ubicacion_codpos = db.Column(db.String(30), nullable=True, name='Ubicacion_codpos')

def insertar_user(data):
    print(data)
    password = data.get('contrasena')
    passwo = hashlib.md5(password.encode('utf-8')).hexdigest().encode('utf-8')
    print(password)
    print(passwo)
    try:
        new_user = Users(
            boleta = data.get('boleta'),
            passw = passwo,
            Tipo_user = 1,
            Id_Estatus_user=1
        )
        db.session.add(new_user)
        db.session.commit()
        print("Se insertó el registro en la tabla USERS")
    except Exception as e:
        print("Error al insertar el registro: ", e)
        db.session.rollback()

def inicio_session(data):
    exito = True
    user = Users.query.filter_by(boleta=data.get('boleta')).first()
    if user:
            contra=user.passw
            password = data.get('contrasena')
            passwo = hashlib.md5(password.encode('utf-8')).hexdigest().encode('utf-8')    
            if contra==passwo:
                print("Se realizo la consulta exitosa:")
            else:
                print("Contraseña incorrecta")
                exito=False
    else:
            id_user = None
            print("No existe el usuario")
            exito=False
            db.session.rollback()
    return exito
# INSERCION DE DATOS DEL ALUMNO
def insertar_data_user(data,id_user):
    
    print(data)
    i_platel=int(data['plantel'])
    data['plantel'] = i_platel
    aux=data['fecha_registro']
    aux2=data['fecha_inicio']
    aux3=data['fecha_termino']

    f_registro = datetime.strptime(aux, "%Y-%m-%d")
    f_inicio = datetime.strptime(aux2, "%Y-%m-%d")
    f_termino = datetime.strptime(aux3, "%Y-%m-%d")

    data['fecha_registro'] = f_registro
    data['fecha_inicio'] = f_inicio
    data['fecha_termino'] = f_termino

    try:
        new_user = DataUsers(
            user_id = id_user,
            nombre=data.get('nombre'),
            a_paterno=data.get('paterno'),
            a_materno=data.get('materno'),
            curp=data.get('curp'),
            boleta=data.get('boleta'),
            id_sexo=data.get('id_sexo'),
            id_plantel=data.get('plantel'),
            cp=data.get('codigo_postal'),
            telefono=data.get('tel_particular'),
            direccion=data.get('direccion'),
            alcaldia=data.get('alcaldia'),
            escolaridad=data.get('escolaridad'),
            correo=data.get('correo'),
            id_carrera=data.get('id_carrera'),
            prestatario=data.get('prestatario'),
            codigo_prestatario=data.get('codigo'),
            responsable=data.get('responsable'),
            programa=data.get('programa'),
            clave_programa=data.get('clave_programa'),
            cargo=data.get('cargo'),
            tel_responsable=data.get('tel_responsable'),
            fecha_registro=data.get('fecha_registro'),
            fecha_inicio=data.get('fecha_inicio'),
            fecha_termino=data.get('fecha_termino'),
            correo_prestatario=data.get('correo_prestatario'),
            ubicacion_calleynum=data.get('ubicacion_calleynum'),
            ubicacion_colonia=data.get('ubicacion_colonia'),
            ubicacion_alcaldia=data.get('ubicacion_alcaldia'),
            ubicacion_codpos=data.get('ubicacion_codpos'),
        )
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        print("Registro insertado exitosamente")
    except Exception as e:
        print("Error al insertar el registro: ", e)
        db.session.rollback()


## RUTAS DE LA APLICACION

@app.route('/')
def index():
    data={
        'titulo':'Sistema Servicio Social'
    }
    error = session.get('error', None)
    exitoso = session.get('exitoso', None)
    session.pop('error', None)
    session.pop('exitoso', None)
    session.clear()
    return render_template('index.html', error=error,data=data,exitoso=exitoso)

@app.route('/registro')
def registroUsuario():
    data={
        'titulo':'Registro'
    }
    errorcarta = session.get('errorcarta', None)
    session.pop('errorcarta', None)
    #session.clear()
    return render_template('registro.html',data=data,errorcarta=errorcarta)

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
        insertar_user(data)
        user = Users.query.filter_by(boleta=data.get('boleta')).first()
        if user:
            id_user = user.id
            print("La consulta dio resultado, el ID del alumno en la tabla USERS es:")
            print(id_user)
            print(type(id_user))
            insertar_data_user(data,id_user)
            exitoso="Tu registro fue exitoso"
            session['exitoso'] = exitoso
            return redirect('/')
        else:
            id_user = None
            print("No existe el usuario")        
    return render_template("confirmacion.html")
        

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
        if data['titulo1']=="INSTITUTO POLITÉCNICO NACIONAL":
            return render_template('confirmacion.html',data=data)
        else:
            errorcarta = "Debe seleccionar una carta compromiso válida"
            session['errorcarta'] = errorcarta
            print(errorcarta)
            return redirect('/registro')
          

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
        'titulo':"INSTITUTO POLITÉCNICO NACIONAL",
        'boleta': request.form['boleta'],
        'contrasena': request.form['contrasena']
    }
    print(data)
    resultado = inicio_session(data)
    if resultado == True:
        return render_template('inicio.html',data=data)
    else:
        error = "Boleta o contraseña inválidos"
        session['error'] = error
        return redirect('/')

if __name__== '__main__':
    app.run(debug=True,port=5000)



