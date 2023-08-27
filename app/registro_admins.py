import os
import hashlib
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv

load_dotenv()

server=os.getenv('SERVER')
bd=os.getenv('DATABASE')
username =os.getenv('USERNAMEBD')
password=os.getenv('PASSWORDBD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password + '@' + server + '/' + bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Session(app)
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

def insertar_admin(data):
    print(data)
    password = data.get('contrasena')
    passwo = hashlib.md5(password.encode('utf-8')).hexdigest().encode('utf-8')
    print(password)
    print(passwo)
    try:
        new_user = Users(
            boleta = data.get('usuario'),
            passw = passwo,
            tipo_user = 1,
        )
        db.session.add(new_user)
        db.session.commit()
        print("Se insertó un nuevo administrador en la tabla USERS")
    except Exception as e:
        print("Error al insertar el administrador: ", e)
        db.session.rollback()

if __name__ == '__main__':
    with app.app_context():
        data = {'usuario': 'Admin', 'contrasena': '123456'}
        insertar_admin(data)
        print("La inserción se ha realizado correctamente")

