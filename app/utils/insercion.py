import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Date
from flask import Flask
#server='DESKTOP-A8TJQDL\SQLEXPRESS01'  #PARA JOSHEP
server='LAPTOP-9T4B4IDA' #PARA J CRUZ
bd='Sistema_Atencion_SS'
user='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://' + user + ':' + password + '@' + server + '/' + bd + '?driver=ODBC+Driver+17+for+SQL+Server'

db = SQLAlchemy()
db.init_app(app)

try:
    db = SQLAlchemy(app)
    db.init_app(app)
    print("Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)

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
    fecha_registro = db.Column(Date, default=datetime.date.today, name='Fecha_registro')
    fecha_inicio = db.Column(Date, name='Fecha_inicio')
    fecha_termino = db.Column(Date, name='Fecha_termino')
    correo_prestatario = db.Column(db.String(50), nullable=True, name='Correo_prestatario')
    ubicacion_calleynum = db.Column(db.String(75), nullable=True, name='Ubicacion_calleynum')
    ubicacion_colonia = db.Column(db.String(75), nullable=True, name='Ubicacion_colonia')
    ubicacion_alcaldia = db.Column(db.String(75), nullable=True, name='Ubicacion_alcaldia')
    ubicacion_codpos = db.Column(db.String(30), nullable=True, name='Ubicacion_codpos')

    
def insertar_registro(data):
    print(data)
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
            fecha_registro=datetime.date.today,
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