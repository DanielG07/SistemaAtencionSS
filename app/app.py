import os
from datetime import datetime
from sqlalchemy import Date
from flask import Flask, redirect, render_template, request, url_for, send_file, session , send_file
from flask_session import Session
from utils.funcion_excel import createApiResponse
from utils.funcion_excel_2 import createApiResponse2
from utils.mocks import preregistro_mock, registro_mock, completados_mock
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, or_
from utils.funcion_correo import enviar_correo, enviar_correo_contrasena
from werkzeug.utils import secure_filename
from utils.lee_pdf import lectura
import hashlib
import secrets
import datetime as d

server='localhost'
bd='Sistema_Atencion_SS'
username='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['CARTAS_COMPROMISO'] = "./app/documentos/CartaCompromiso/"
app.config['EXPEDIENTES'] = "./app/documentos/Expedientes"
app.config['VER_EXPEDIENTES'] = "./documentos/Expedientes/"
app.config['EVALUACION_DESEMPENO'] = "./app/documentos/Evaluaciones"
app.config['VER_EVALUACION_DESEMPENO'] = "./documentos/Evaluaciones/"
app.config['CARTA_TERMINO'] = "./app/documentos/CartasTermino"
app.config['VER_CARTA_TERMINO'] = "./documentos/CartasTermino/"
app.config['CONSTANCIA_LIBERACION'] = "./app/documentos/ConstanciasLiberacion"
app.config['VER_CONSTANCIA_LIBERACION'] = "./documentos/ConstanciasLiberacion/"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password + '@' + server + '/' + bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = os.urandom(24)
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
    tipo_user = db.Column(db.Integer, nullable=False,name='Tipo_user')
    id_status_user = db.Column(db.Integer, nullable=False, name='Id_Estatus_user')
    actualizacion_estatus=db.Column(db.DateTime, nullable=False, name='Actualizacion_Estatus')  

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
    semestre = db.Column(db.Integer,nullable=True,name='Semestre')
    cp = db.Column(db.String(30), nullable=True, name='CP')
    telefono = db.Column(db.String(30), nullable=True, name='Tel_particular')
    direccion =  db.Column(db.String(500), nullable=True, name='Direccion')
    alcaldia =  db.Column(db.String(75), nullable=True, name='Alcaldia')
    escolaridad = db.Column(db.String(10), nullable=True, name='Escolaridad')
    correo = db.Column(db.String(50), nullable=True, name='Correo')
    id_carrera = db.Column(db.Integer, nullable=True,name='Id_carrera')
    clave_carrera = db.Column(db.String(50), nullable=True, name='Clave_carrera')
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
    token = db.Column(db.String(32), nullable=True,unique=True,name='Token')
    No_registro = db.Column(db.String(20), nullable=True, name='No_Registro')
    numero_registro = db.Column(db.Integer, nullable=True, name='Numero_Registro')

# MODELO PARA EL CATALOGO DE CARRERAS
class Carreras(db.Model):
    __tablename__ = 'TABLE_CARRERA'
    id = db.Column(db.Integer, primary_key=True, name='Id_Carrera')
    carrera = db.Column(db.String(200), nullable=True, name='DESCRIPCION_CARRERA')

# MODELO PARA LA TABLA "DOCUMENTOS"
class Documentos(db.Model):
    __tablename__ = 'DOCUMENTOS'
    id = db.Column(db.Integer, primary_key=True, name='Id_documento')
    id_alumno = db.Column(db.Integer, name='Id_alumno')
    id_tipo = db.Column(db.Integer, name='Id_Tipo_Documento')
    id_status = db.Column(db.Integer, name='Id_Status_Documento')
    fecha_envio = db.Column(db.Date, nullable=True, name='Fecha_Envio')
    fecha_aceptado = db.Column(db.Date, nullable=True, name='Fecha_Aceptado')
    ubicacion = db.Column(db.String(256), nullable=True, name='Ubicacion_Archivo')
    nombre_archivo = db.Column(db.String(256), nullable=True, name='Nombre_Archivo')

class StatusDocumento (db.Model):
    __tablename__ = 'STATUS_DOCUMENTO'
    id = db.Column(db.Integer, primary_key=True, name='Id_Status_Documento')
    status_documento = db.Column(db.String(20), nullable=True,  name='Status_Documento')


class TipoDocumento (db.Model):
    __tablename__ = 'TIPO_DOCUMENTO'
    id = db.Column(db.Integer, primary_key=True, name='Id_Tipo_Documento')
    tipo_documento = db.Column(db.String(40), nullable=True, name='Tipo_Documento' )

class TipoUser (db.Model):
    __tablename__ = 'TIPO_USERS_TABLE'
    id = db.Column(db.Integer, primary_key=True, name='Id_Tipo_Users')
    tipo_usuario = db.Column(db.String(20), nullable=True, name='Descripcion_user' )

class StatusUser (db.Model):
    __tablename__ = 'STATUS_USER'
    id = db.Column(db.Integer, primary_key=True, name='Id_Estatus_user')
    status = db.Column(db.String(10), nullable=True, name='Descripcion_Status' )

class Sexo (db.Model):
    __tablename__ = 'TABLE_SEXO'
    id = db.Column(db.Integer, primary_key=True, name='Id_Sexo')
    sexo = db.Column(db.String(15), nullable=True, name='Sexo' )    



 


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
            tipo_user = 2,
            id_status_user=1
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
                print("Se realizó la consulta exitosa:")
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
            semestre = data.get('semestre'),
            cp=data.get('codigo_postal'),
            telefono=data.get('tel_particular'),
            direccion=data.get('direccion'),
            alcaldia=data.get('alcaldia'),
            escolaridad=data.get('escolaridad'),
            correo=data.get('correo'),
            id_carrera=data.get('id_carrera'),
            clave_carrera = data.get('clave_carrera'),
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
            No_registro = "SIN ASIGNAR",
            numero_registro = -1
        )
        print(new_user)
        db.session.add(new_user)
        db.session.commit()
        print("Registro insertado exitosamente")
    except Exception as e:
        print("Error al insertar el registro: ", e)
        db.session.rollback()

# CREACION DE LOS DOCUMENTOS DEL ALUMNO (EN EL REGISTRO)
def crear_documentos(Id_alumno):
    print(Id_alumno)
    try:
        documento1 = Documentos(
            id_alumno = Id_alumno,
            id_tipo = 1,
            id_status = 1,
            fecha_envio= None,
            fecha_aceptado=None,
            ubicacion=None,
        )
        documento2 = Documentos(
            id_alumno = Id_alumno,
            id_tipo = 2,
            id_status = 1,
            fecha_envio= None,
            fecha_aceptado=None,
            ubicacion=None,
        )
        documento3 = Documentos(
            id_alumno = Id_alumno,
            id_tipo = 3,
            id_status = 1,
            fecha_envio= None,
            fecha_aceptado=None,
            ubicacion=None,
        )
        documento4 = Documentos(
            id_alumno = Id_alumno,
            id_tipo = 4,
            id_status = 1,
            fecha_envio= None,
            fecha_aceptado=None,
            ubicacion=None,
        )
        db.session.add(documento1)
        db.session.add(documento2)
        db.session.add(documento3)
        db.session.add(documento4)
        db.session.commit()
        print("Documento creado en la base de datos")
    except Exception as e:
        print("Error al crear el documento", e)
        db.session.rollback()

## RUTAS DE LA APLICACION

@app.route('/')
def index():
    data={
        'titulo':'Sistema Servicio Social'
    }
    nueva = session.get('nueva',None)
    error = session.get('error', None)
    exitoso = session.get('exitoso', None)
    instrucciones = session.get('instrucciones', None)
    session.pop('error', None)
    session.pop('exitoso', None)
    session.pop('nueva', None)
    session.pop('instrucciones', None)
    session.clear()
    return render_template('index.html', error=error,data=data,exitoso=exitoso,nueva=nueva,instrucciones=instrucciones)

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
        usuario = Users.query.filter_by(boleta=data.get('boleta')).first()
        if usuario:
            errorboleta = "Ya existe un usuario registrado con esa boleta"
            print(errorboleta)
            return render_template ("confirmacion.html",data=data,errorboleta=errorboleta)
            
        insertar_user(data)
        user = Users.query.filter_by(boleta=data.get('boleta')).first()
        if user:
            id_user = user.id
            ##INSERCION DE DATOS DEL ALUMNO
            insertar_data_user(data,id_user)
            ##CREACION DE LOS DOCUMENTOS DEL ALUMNO
            alumno = DataUsers.query.filter_by(boleta=data.get('boleta')).first()
            if alumno:
                id_alumno = alumno.id
                crear_documentos(id_alumno)
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
        f.save(os.path.join(app.config['CARTAS_COMPROMISO'],filename))
        print(filename)
        ruta = app.config['CARTAS_COMPROMISO'] + filename
        data = lectura(ruta)
        print(data)
        if data['titulo1']=="INSTITUTO POLITÉCNICO NACIONAL":
            errorboleta = session.get('errorboleta', None)
            session.pop('errorboleta', None)
            return render_template('confirmacion.html',data=data,errorboleta=errorboleta)
        else:
            errorcarta = "Debe seleccionar una carta compromiso válida"
            session['errorcarta'] = errorcarta
            print(errorcarta)
            return redirect('/registro')
          

@app.route('/admin', methods=['GET', 'POST'])
def indexAdmin():
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Administrador'
    }
    return render_template('admin/main.html',data=data)

@app.route('/admin/reportes')
def reportesAdmin():
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Reportes - Administrador'
    }
    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(StatusUser.status == "ACEPTADO")
    .all())
    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.append(userSend)
    return render_template('admin/reportes.html',data=data, registros = users_list)

@app.route('/admin/completados')
def completadosAdmin():
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Completados - Administrador'
    }
    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(StatusUser.status == "COMPLETADO")
    .all())
    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.append(userSend)
    return render_template('admin/completados.html',data=data, registros = users_list)


@app.route('/admin/expedientes', methods=['GET', 'POST'])
def preregistrosAdmin():
    if 'username' not in session:
        return redirect('/')

    print(session)
    data={
        'titulo':'Expedientes - Administrador'
    }
    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(or_(StatusUser.status.like("ESPERA"), StatusUser.status.like("RECHAZADO")))
    .all())
    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.append(userSend)

    return render_template('admin/expedientes.html',data=data, registros = users_list)

@app.route('/admin/finalizado')
def finalizadosAdmin():
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Finalizados - Administrador'
    }
    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(StatusUser.status == "CONCLUIDO")
    .all())
    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.insert(0,userSend)
    return render_template('admin/finalizado.html',data=data, registros = users_list)

@app.route('/admin/estadisticas')
def estadisticasAdmin():
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Estadisitcas Reportes'
    }
    return render_template('admin/estadisticas.html',data=data)

@app.route("/admin/generar_preregistros")
def generarExcelPreregistro():
    if 'username' not in session:
        return redirect('/')
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(preregistro_mock)
    return apiResponse

@app.route("/admin/generar_completados")
def generarExcelEmision():
    if 'username' not in session:
        return redirect('/')
    
    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(StatusUser.status == "COMPLETADO")
    .all())

    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.append(userSend)
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse2(users_list)
    return apiResponse

@app.route("/admin/generar_finalizado")
def generarExcelCompletados():
    if 'username' not in session:
        return redirect('/')

    users = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(StatusUser.status == "CONCLUIDO")
    .all())

    users_list = []
    for user in users:
        userSend = {
            "boleta": user[0],
            "nombre": user[1] + " " + user[2] + " " +user[3],
            "carrera": user[4],
            "semestre": user[5],
            "genero": user[6],
            "prestatario": user[7],
            "f_inicio": user[8],
            "f_termino": user[9],
            "correo_electronico": user[10],
            "estatus": user[11],
            "numero": user[12],
            "f_envio": user[13],
        }
        users_list.append(userSend)
    # Traer datos de acuerdo a la pagina
    apiResponse = createApiResponse(users_list)
    return apiResponse

@app.route("/admin/expediente/<boleta>")
def expedienteAlumno(boleta=0):
    if 'username' not in session:
        return redirect('/')
    data={
        'titulo':'Expediente - ' + boleta
    }

    total = (db.session.query(
        DataUsers.numero_registro)
        .order_by(DataUsers.numero_registro.desc())
        .first())

    today = d.date.today()
    date = today.strftime("%Y")
    date = date.split("20")[1]

    if total[0] == -1:
        total = 0
    else:
        total = total[0]

    expediente = (db.session.query(
        Users.boleta, 
        DataUsers.nombre, 
        DataUsers.a_paterno, 
        DataUsers.a_materno, 
        Carreras.carrera, 
        DataUsers.semestre, 
        Sexo.sexo, 
        DataUsers.prestatario, 
        DataUsers.fecha_inicio, 
        DataUsers.fecha_termino, 
        DataUsers.correo, 
        StatusUser.status, 
        DataUsers.No_registro,
        DataUsers.fecha_registro)
    .join(StatusUser, Users.id_status_user == StatusUser.id)
    .join(DataUsers, Users.id == DataUsers.user_id)
    .join(Carreras, Carreras.id == DataUsers.id_carrera)
    .join(Sexo, Sexo.id == DataUsers.id_sexo)
    .filter(Users.boleta == boleta)
    .first())

    documentos = (db.session.query(
        Users.boleta,
        Documentos.fecha_envio,
        Documentos.fecha_aceptado,
        StatusDocumento.status_documento,
        TipoDocumento.tipo_documento,
        Documentos.ubicacion,
        Documentos.nombre_archivo,
        Documentos.id,
        Documentos.id_status)
        .join(DataUsers, Users.id == DataUsers.user_id)
        .join(Documentos, DataUsers.id == Documentos.id_alumno)
        .join(TipoDocumento, TipoDocumento.id == Documentos.id_tipo)
        .join(StatusDocumento, StatusDocumento.id == Documentos.id_status)
        .filter(Users.boleta == boleta)
        .all())

    expedientePage = {
        "boleta": expediente[0],
        "nombre": expediente[1] + " " + expediente[2] + " " + expediente[3],
        "carrera": expediente[4],
        "semestre": expediente[5],
        "genero": expediente[6],
        "prestatario": expediente[7],
        "f_inicio": expediente[8],
        "f_termino": expediente[9],
        "correo_electronico": expediente[10],
        "estatus": expediente[11],
        "numero": expediente[12],
        "registro_lista": expediente[12],
        "f_envio": expediente[13],
    }
    print(expedientePage)

    documentosPage = []
    for documento in documentos:
        print(documento)
        documentoPage = {
            "boleta": documento[0],
            "f_envio": documento[1],
            "f_aceptado": documento[2],
            "status": documento[3],
            "t_documento": documento[4],
            "u_documento": documento[5],
            "n_documento": documento[6],
            "id_documento": documento[7],
            "id_status": documento[8]
        }
        documentosPage.append(documentoPage)

    print(documentosPage)
    return render_template('admin/perfilAlumno.html',data=data, expediente=expedientePage, documentos=documentosPage, total=total, today=date)

@app.route("/admin/aceptarDocumento", methods=['POST'])
def aceptarDocumento():
    data = request.json
    if 'registro' in data:
        user = DataUsers.query.filter_by(boleta = data['boleta']).first()
        user.No_registro = data['registro']
        user.numero_registro = data['noRegistro']
        db.session.commit()

    id_user =  (db.session.query(
        DataUsers.id 
       )
    .filter(DataUsers.boleta == data['boleta'])
    .first())
    
    documento = Documentos.query.filter_by(id_alumno=id_user[0], id_status=3).first()
    documento.id_status = 2
    documento.fecha_aceptado = d.date.today().strftime("%Y-%m-%d")
    db.session.commit()

    if documento.id_tipo == 1:
        user = Users.query.filter_by(boleta=data['boleta']).first()
        user.id_status_user = 3
        db.session.commit()

    if documento.id_tipo == 3:
        user = Users.query.filter_by(boleta=data['boleta']).first()
        user.id_status_user = 4
        db.session.commit()

    if documento.id_tipo == 4:
        user = Users.query.filter_by(boleta=data['boleta']).first()
        user.id_status_user = 5
        db.session.commit()

    enviar_correo(data['email'], "Sistema Servicio Social - Documento Aceptado", "documento fue aceptado")

    return {
        "ok": False
    }
    

@app.route("/admin/rechazarDocumento", methods=['POST'])
def rechazarDocumento():
    data = request.json
    print(data)
    id_user =  (db.session.query(
        DataUsers.id 
       )
    .filter(DataUsers.boleta == data['boleta'])
    .first())

    documento = Documentos.query.filter_by(id_alumno=id_user[0], id_status=3).first()
    documento.id_status = 4
    db.session.commit()

    enviar_correo(data['email'], "Sistema Servicio Social - Documento Aceptado", "documento fue rechazado")

    return {
        "ok": False
    }

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
    if 'boleta' not in session or session['boleta'] != boleta:
        return redirect('/')
    data = {
        'titulo': 'Alumno'
    }
    return render_template('estudiante/main.html', data=data)

@app.route('/estudiante/expediente/<boleta>', methods=['GET'])
def expedienteEstudiante(boleta):
    if 'boleta' not in session or session['boleta'] != boleta:
        return redirect('/')
    data={
        'titulo' : 'Alumno - Expediente'
    }
    user = DataUsers.query.filter_by(boleta=boleta).first()
    if user:
        id = user.id
        id_carrera = user.id_carrera
        carreras = Carreras.query.filter_by(id=id_carrera).first()
        documentos = db.session.query(Documentos).join(DataUsers, DataUsers.id==Documentos.id_alumno).\
            filter(DataUsers.id==id).all()
        print(documentos)
        print(len(documentos))
        en_espera = False
        documentos_list = []
        for documento in documentos:
            id_alumno = documento.id_alumno
            id_tipo = documento.id_tipo
            id_status = documento.id_status
            id_doc = documento.id
            tipo_doc= TipoDocumento.query.filter_by(id=id_tipo).first()
            status_doc = StatusDocumento.query.filter_by(id=id_status).first()
            if id_status == 3:
                en_espera = True
            documento_dict = {
            'id_doc': id_doc,   
            'id_alumno': id_alumno,
            'id_tipo': id_tipo,
            'id_status': id_status,
            'fecha_envio': documento.fecha_envio,
            'fecha_aceptado': documento.fecha_aceptado,
            'ubicacion': documento.ubicacion,
            'nombre_archivo': documento.nombre_archivo,
            'tipo_documento': tipo_doc.tipo_documento,
            'status_documento': status_doc.status_documento,
            }
            documentos_list.append(documento_dict)
        ## SE IMPRIME CADA ELEMENTO DE LA LISTA
        for documento in documentos_list:
            print(documento['id_doc'])
            print(documento['id_alumno'])
            print(documento['id_tipo'])
            print(documento['id_status'])
            print(documento['fecha_envio'])
            print(documento['fecha_aceptado'])
            print(documento['ubicacion'])
            print(documento['tipo_documento'])
            print(documento['status_documento'])  

        expediente = {
            'nombre': user.nombre,
            'paterno': user.a_paterno,
            'materno': user.a_materno,
            'curp': user.curp,
            'boleta': user.boleta,
            'id_sexo': user.id_sexo,
            'plantel':user.id_plantel,
            'clave_carrera': user.clave_carrera,
            'id_carrera': user.id_carrera,
            'carrera':carreras.carrera,
            'semestre': user.semestre,
            'correo': user.correo,
            'tel_particular':user.telefono,
            'escolaridad':user.escolaridad,
            'direccion':user.direccion,
            'codigo_postal':user.cp,
            'alcaldia':user.alcaldia,
            'prestatario': user.prestatario,
            'codigo': user.codigo_prestatario,
            'programa': user.programa,
            'clave_programa':user.clave_programa,
            'fecha_registro': user.fecha_registro,
            'fecha_inicio': user.fecha_inicio,
            'fecha_termino': user.fecha_termino,
            'responsable':user.responsable,
            'cargo':user.cargo,
            'tel_responsable':user.tel_responsable,
            'correo_prestatario':user.correo_prestatario,
            'ubicacion_calleynum':user.ubicacion_calleynum,
            'ubicacion_colonia':user.ubicacion_colonia,
            'ubicacion_alcaldia':user.ubicacion_alcaldia,
            'ubicacion_codpos':user.ubicacion_codpos,
            'numero':user.No_registro,
            'espera':en_espera,
        }
        print(expediente)
        
    # Buscar información del estudiante y mandarlo para pintar
        
    #for item in registro_mock:
        #if item.get("boleta") == boleta:
            #expediente = item
            #break
    return render_template('estudiante/expediente.html', data=data, expediente=expediente,documentos=documentos_list)

@app.route('/estudiante/perfil/<boleta>', methods=['GET'])
def perfilEstudiante(boleta):
    if 'boleta' not in session or session['boleta'] != boleta:
        return redirect('/')
    data={
        'titulo' : 'Alumno - Perfil'
    }
    user = DataUsers.query.filter_by(boleta=boleta).first()
    if user:
        id_carrera = user.id_carrera
        id_sexo = user.id_sexo
        carreras = Carreras.query.filter_by(id=id_carrera).first()
        sexos = Sexo.query.filter_by(id=id_sexo).first()
        expediente = {
            'nombre': user.nombre,
            'paterno': user.a_paterno,
            'materno': user.a_materno,
            'curp': user.curp,
            'boleta': user.boleta,
            'id_sexo': user.id_sexo,
            'sexo':sexos.sexo,
            'plantel':user.id_plantel,
            'clave_carrera': user.clave_carrera,
            'id_carrera': user.id_carrera,
            'carrera':carreras.carrera,
            'semestre': user.semestre,
            'correo': user.correo,
            'tel_particular':user.telefono,
            'escolaridad':user.escolaridad,
            'direccion':user.direccion,
            'codigo_postal':user.cp,
            'alcaldia':user.alcaldia,
            'prestatario': user.prestatario,
            'codigo': user.codigo_prestatario,
            'programa': user.programa,
            'clave_programa':user.clave_programa,
            'fecha_registro': user.fecha_registro,
            'fecha_inicio': user.fecha_inicio,
            'fecha_termino': user.fecha_termino,
            'responsable':user.responsable,
            'cargo':user.cargo,
            'tel_responsable':user.tel_responsable,
            'correo_prestatario':user.correo_prestatario,
            'ubicacion_calleynum':user.ubicacion_calleynum,
            'ubicacion_colonia':user.ubicacion_colonia,
            'ubicacion_alcaldia':user.ubicacion_alcaldia,
            'ubicacion_codpos':user.ubicacion_codpos,
            'numero':user.No_registro,
        }
    # Buscar información del estudiante y mandarlo para pintar
    return render_template('estudiante/perfil.html', data=data, expediente=expediente)


## RESTABLECIMIENTO DE CONTRASEÑA DEL ALUMNO

@app.route('/restablecer_contrasena')
def restablecer_contrasena():
    data={
        'titulo':'Cambiar contraseña'
    }
    errortoken = session.get('errortoken',None)
    errorboleta = session.get('errorboleta',None)
    errorcorreo = session.get('errorcorreo',None)
    session.pop('errorboleta', None)
    session.pop('errorcorreo', None)
    session.pop('errortoken', None)
    session.clear()
    return render_template('restablecer_contrasena.html',data=data,errorboleta=errorboleta,errorcorreo=errorcorreo,errortoken=errortoken)

@app.route('/restablecer_contrasena',methods=['POST'])
def restablecer_contrasena_usuario():
    if request.method == 'POST':
        boleta = request.form['Idp-Boleta']
        correo = request.form['Idp-email']
        # Verificar si el correo está registrado en la base de datos
        usuario = DataUsers.query.filter_by(boleta=boleta).first()
        if usuario:
            correobase = usuario.correo
            if correobase == correo:
                # Generar un token único para el usuario
                token = secrets.token_urlsafe(16)
                # Guardar el token en la base de datos
                usuario.token = token
                db.session.commit()
                # Crear el enlace de restablecimiento de contraseña
                enlace = url_for('restablecer_contrasena_confirmacion', token=token, _external=True)
                # Crear el mensaje de correo electrónico
                asunto = 'Restablecimiento de contraseña'
                print(asunto)
                mensaje = render_template('email/restablecer_contrasena.html', enlace=enlace)
                print(mensaje)
                enviar_correo_contrasena(correo, asunto, mensaje)
                print("Se envio")
                # Redirigir al usuario a la página de inicio con un mensaje de confirmación
                instrucciones = "Se ha enviado un correo electrónico con instrucciones para restablecer tu contraseña."
                print(instrucciones)
                session['instrucciones'] = instrucciones
                return redirect(url_for('index'))
            else:
                errorcorreo = "El correo ingresado no está registrado en el sistema"
                session['errorcorreo'] = errorcorreo
                return redirect(url_for('restablecer_contrasena'))
        else:
            errorboleta = "No existe un usuario con esa boleta, registrese o ingrese una boleta correcta"
            session['errorboleta'] = errorboleta
            print(errorboleta)
            return redirect(url_for('restablecer_contrasena'))


@app.route('/restablecer-contrasena-confirmacion/<token>', methods=['GET', 'POST'])
def restablecer_contrasena_confirmacion(token):
    usuario = DataUsers.query.filter_by(token=token).first()
    if not usuario:
        errortoken="El enlace de restablecimiento de contraseña no es válido o ha expirado."
        session['errortoken'] = errortoken
        print(errortoken)
        return redirect(url_for('restablecer_contrasena'))
    if request.method == 'POST':
        if usuario:
            print("Existe el usuario, el enlace está activo")
            id = usuario.user_id
            user = Users.query.filter_by(id=id).first()
            if user:
                print("Encontré el id")
            # Verificar que la contraseña sea segura
            contrasena = request.form['Idp-contraseña']
            # Actualizar la contraseña del usuario
            passwo = hashlib.md5(contrasena.encode('utf-8')).hexdigest().encode('utf-8')
            user.passw = passwo
            usuario.token = None
            db.session.commit()
            print('Tu contraseña ha sido actualizada.')
            nueva="Se ha actualizado tu contraseña"
            session['nueva'] = nueva
            return redirect(url_for('index'))
    return render_template('restablecer_contrasena_confirmacion.html')


#PRUEBAS PARA INICIO DE SESION
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
        user = Users.query.filter_by(boleta=data.get('boleta')).first()
        if user.tipo_user == 2:
            print("Estudiante")
            session['boleta'] = user.boleta
            return redirect(f'/estudiante/{user.boleta}')
        if user.tipo_user == 1:
            print("Administrador")
            session['username'] = user.boleta
            return redirect('/admin')
    else:
        error = "Boleta o contraseña inválidos"
        session['error'] = error
        return redirect('/')

@app.route('/cerrar_sesion', methods=['GET'])
def cerrar_sesion():
    session.pop('boleta', None)
    session.clear()
    return redirect('/')

#SUBIR DOCUMENTACIÓN DEL ALUMNO
@app.route("/subir_expediente", methods=['POST'])
def subirExpediente():
    if request.method == "POST":
        if 'boleta' not in session:
            return redirect('/')
        boleta = session.get('boleta', None)
        alumno = DataUsers.query.filter_by(boleta=boleta).first()
        f = request.files['expediente']
        filename = secure_filename(f.filename)
        new_filename = "Expediente" + boleta + os.path.splitext(filename)[1]
        f.save(os.path.join(app.config['EXPEDIENTES'], new_filename))
        print(new_filename)
        ruta = './app/documentos/Expedientes/' + new_filename
        print("Se ha guardado correctamente en la ruta " + ruta)
        #RECUPERAMOS LOS DATOS PARA MODIFICAR EN BD
        id_documento = int(request.form['id_doc'])
        id_alumno = alumno.id 
        id_status = int(request.form.get('id_status'))
        fecha_actual_str = request.form.get('Idp-Factual')
        fecha_actual = datetime.strptime(fecha_actual_str, '%Y-%m-%d').date()
        ubicacion = ruta
        print(fecha_actual)
        print(type(fecha_actual))
        data = {
            'titulo': 'Alumno',
        }
        ## CASO EN QUE SEA "NO ARCHIVO" O "RECHAZADO"
        if id_status == 1 or id_status == 4:
            print("El status es SIN ARCHIVO")
            documento = Documentos.query.filter_by(id=id_documento, id_alumno=id_alumno).first()
            documento.id_status = 3 #CAMBIAMOS EL STATUS A ESPERA
            documento.fecha_envio = fecha_actual
            documento.ubicacion = ubicacion
            documento.nombre_archivo = new_filename
            db.session.commit()
            exito = "Se ha subido correctamente su documento, espere validación"
        return render_template('estudiante/main.html', data=data,exito=exito)

@app.route("/subir_evaluacion", methods=['POST'])
def subirEvaluacion():
    if request.method == "POST":
        if 'boleta' not in session:
            return redirect('/')
        boleta = session.get('boleta', None)
        alumno = DataUsers.query.filter_by(boleta=boleta).first()
        f = request.files['evaluacion']
        filename = secure_filename(f.filename)
        new_filename = "Evaluacion" + boleta + os.path.splitext(filename)[1]
        f.save(os.path.join(app.config['EVALUACION_DESEMPENO'], new_filename))
        print(new_filename)
        ruta = './app/documentos/Evaluaciones/' + new_filename
        print("Se ha guardado correctamente en la ruta " + ruta)
        #RECUPERAMOS LOS DATOS PARA MODIFICAR EN BD
        id_documento = int(request.form['id_doc'])
        id_alumno = alumno.id 
        id_status = int(request.form.get('id_status'))
        fecha_actual_str = request.form.get('Idp-Factual')
        fecha_actual = datetime.strptime(fecha_actual_str, '%Y-%m-%d').date()
        ubicacion = ruta
        print(fecha_actual)
        print(type(fecha_actual))
        data = {
            'titulo': 'Alumno',
        }
        ## CASO EN QUE SEA "NO ARCHIVO" O "RECHAZADO"
        if id_status == 1 or id_status == 4:
            documento = Documentos.query.filter_by(id=id_documento, id_alumno=id_alumno).first()
            documento.id_status = 3 #CAMBIAMOS EL STATUS A ESPERA
            documento.fecha_envio = fecha_actual
            documento.ubicacion = ubicacion
            documento.nombre_archivo = new_filename
            db.session.commit()
            exito = "Se ha subido correctamente su documento, espere validación"
        return render_template('estudiante/main.html', data=data,exito=exito)

@app.route("/subir_carta", methods=['POST'])
def subirCarta():
    if request.method == "POST":
        if 'boleta' not in session:
            return redirect('/')
        boleta = session.get('boleta', None)
        alumno = DataUsers.query.filter_by(boleta=boleta).first()
        f = request.files['carta']
        filename = secure_filename(f.filename)
        new_filename = "CartaTermino" + boleta + os.path.splitext(filename)[1]
        f.save(os.path.join(app.config['CARTA_TERMINO'], new_filename))
        print(new_filename)
        ruta = './app/documentos/ConstanciasLiberacion/' + new_filename
        print("Se ha guardado correctamente en la ruta " + ruta)
        #RECUPERAMOS LOS DATOS PARA MODIFICAR EN BD
        id_documento = int(request.form['id_doc'])
        id_alumno = alumno.id 
        id_status = int(request.form.get('id_status'))
        fecha_actual_str = request.form.get('Idp-Factual')
        fecha_actual = datetime.strptime(fecha_actual_str, '%Y-%m-%d').date()
        ubicacion = ruta
        print(fecha_actual)
        print(type(fecha_actual))
        data = {
            'titulo': 'Alumno',
        }
        ## CASO EN QUE SEA "NO ARCHIVO" O "RECHAZADO"
        if id_status == 1 or id_status == 4:
            documento = Documentos.query.filter_by(id=id_documento, id_alumno=id_alumno).first()
            documento.id_status = 3 #CAMBIAMOS EL STATUS A ESPERA
            documento.fecha_envio = fecha_actual
            documento.ubicacion = ubicacion
            documento.nombre_archivo = new_filename
            db.session.commit()
            exito = "Se ha subido correctamente su documento, espere validación"
        return render_template('estudiante/main.html', data=data,exito=exito)

@app.route("/subir_constancia", methods=['POST'])
def subirConstacia():
    
    if request.method == "POST":
        print(session)
        if 'boleta' not in session and 'username' not in session:
            return redirect('/')
        
        print(request.form)
        boleta = request.form.get('boleta')
        alumno = DataUsers.query.filter_by(boleta=boleta).first()
        f = request.files['constancia']
        filename = secure_filename(f.filename)
        new_filename = "Constancia" + boleta + os.path.splitext(filename)[1]
        f.save(os.path.join(app.config['CONSTANCIA_LIBERACION'], new_filename))
        print(new_filename)
        ruta = './app/documentos/ConstanciasLiberacion/' + new_filename
        print("Se ha guardado correctamente en la ruta " + ruta)
        #RECUPERAMOS LOS DATOS PARA MODIFICAR EN BD
        id_documento = int(request.form['id_doc'])
        id_alumno = alumno.id 
        id_status = int(request.form.get('id_status'))
        fecha_actual = d.date.today().strftime("%Y-%m-%d")
        ubicacion = ruta
        print(fecha_actual)
        print(type(fecha_actual))
        data = {
            'titulo': 'Alumno',
        }
        ## CASO EN QUE SEA "NO ARCHIVO" O "RECHAZADO"
        if id_status == 1 or id_status == 4:
            documento = Documentos.query.filter_by(id=id_documento, id_alumno=id_alumno).first()
            documento.id_status = 3 #CAMBIAMOS EL STATUS A ESPERA
            documento.fecha_envio = fecha_actual
            documento.ubicacion = ubicacion
            documento.nombre_archivo = new_filename
            db.session.commit()
            exito = "Se ha subido correctamente su documento, espere validación"
        return redirect(f'/admin/expediente/{boleta}')

#VISUALIZACION DE DOCUMENTOS
@app.route('/app/documentos/Expedientes/<path:filename>')
def verExpedientepdf(filename):
    if 'boleta' not in session and 'username' not in session:
        return redirect('/')
    if not filename:
        return "Error: no se ha especificado el nombre del archivo PDF"
    boleta = ""
    if 'boleta' in session:
        boleta = session.get('boleta')
    else:
        boleta = session.get('username')

    alumno = Users.query.filter_by(boleta=boleta).first()
    if alumno.tipo_user == 1:
        documento = Documentos.query.filter_by(nombre_archivo=filename).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_EXPEDIENTES'] + filename
            return send_file(ruta, mimetype='application/pdf')


    alumno = DataUsers.query.filter_by(boleta=boleta).first()
    print(alumno)
    if alumno:
        documento = Documentos.query.filter_by(id_alumno=alumno.id, id_tipo=1).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_EXPEDIENTES'] + filename
            return send_file(ruta, mimetype='application/pdf')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/app/documentos/Evaluacion/<path:filename>')
def verEvaluacionpdf(filename):
    if 'boleta' not in session and 'username' not in session:
        return redirect('/')
    if not filename:
        return "Error: no se ha especificado el nombre del archivo PDF"
    boleta = ""
    if 'boleta' in session:
        boleta = session.get('boleta')
    else:
        boleta = session.get('username')

    alumno = Users.query.filter_by(boleta=boleta).first()
    if alumno.tipo_user == 1:
        documento = Documentos.query.filter_by(nombre_archivo=filename).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_EVALUACION_DESEMPENO'] + filename
            return send_file(ruta, mimetype='application/pdf')


    alumno = DataUsers.query.filter_by(boleta=boleta).first()
    print(alumno)
    if alumno:
        documento = Documentos.query.filter_by(id_alumno=alumno.id, id_tipo=2).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_EVALUACION_DESEMPENO'] + filename
            return send_file(ruta, mimetype='application/pdf')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/app/documentos/CartaTermino/<path:filename>')
def verCartaTerminopdf(filename):
    if 'boleta' not in session and 'username' not in session:
        return redirect('/')
    if not filename:
        return "Error: no se ha especificado el nombre del archivo PDF"
    boleta = ""
    if 'boleta' in session:
        boleta = session.get('boleta')
    else:
        boleta = session.get('username')

    alumno = Users.query.filter_by(boleta=boleta).first()
    if alumno.tipo_user == 1:
        documento = Documentos.query.filter_by(nombre_archivo=filename).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_CARTA_TERMINO'] + filename
            return send_file(ruta, mimetype='application/pdf')


    alumno = DataUsers.query.filter_by(boleta=boleta).first()
    print(alumno)
    if alumno:
        documento = Documentos.query.filter_by(id_alumno=alumno.id, id_tipo=3).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_CARTA_TERMINO'] + filename
            return send_file(ruta, mimetype='application/pdf')
        else:
            return redirect('/')
    else:
        return redirect('/')

@app.route('/app/documentos/ConstanciaLiberacion/<path:filename>')
def verConstanciaLiberacionpdf(filename):
    if 'boleta' not in session and 'username' not in session:
        return redirect('/')
    if not filename:
        return "Error: no se ha especificado el nombre del archivo PDF"
    boleta = ""
    if 'boleta' in session:
        boleta = session.get('boleta')
    else:
        boleta = session.get('username')

    alumno = Users.query.filter_by(boleta=boleta).first()
    if alumno.tipo_user == 1:
        documento = Documentos.query.filter_by(nombre_archivo=filename).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_CONSTANCIA_LIBERACION'] + filename
            return send_file(ruta, mimetype='application/pdf')


    alumno = DataUsers.query.filter_by(boleta=boleta).first()
    print(alumno)
    if alumno:
        documento = Documentos.query.filter_by(id_alumno=alumno.id, id_tipo=4).first()
        if filename == documento.nombre_archivo:
            ruta = app.config['VER_CONSTANCIA_LIBERACION'] + filename
            return send_file(ruta, mimetype='application/pdf')
        else:
            return redirect('/')
    else:
        return redirect('/')

if __name__== '__main__':
    app.run(debug=True,port=5000)
