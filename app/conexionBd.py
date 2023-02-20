from flask_sqlalchemy import SQLAlchemy
from flask import Flask
#server='DESKTOP-A8TJQDL\SQLEXPRESS01'  #PARA JOSHEP
#server='LAPTOP-9T4B4IDA' #PARA J CRUZ
server='DANIEL\SQLEXPRESS' #PARA DANIEL
bd='Sistema_Atencion_SS'
user='SS_SISTEMAATENCION'
password='Irvin19+'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://' + user + ':' + password + '@' + server + '/' + bd + '?driver=ODBC+Driver+17+for+SQL+Server'
try:
    db = SQLAlchemy(app)
    print("Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)