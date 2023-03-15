from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import pymysql

server='localhost' 
bd='Sistema_Atencion_SS'
username ='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password + '@' + server + '/' + bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    db = SQLAlchemy(app)
    print(" * Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)
