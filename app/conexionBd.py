import os
import pymysql
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from dotenv import load_dotenv

load_dotenv()

server=os.getenv('SERVER')
bd=os.getenv('DATABASE')
username =os.getenv('USERNAMEBD')
password=os.getenv('PASSWORDBD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://' + username + ':' + password + '@' + server + '/' + bd
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

try:
    db = SQLAlchemy(app)
    print(" * Conexión a la base de datos exitosa")
except Exception as e:
    print("Error al conectarse a la base de datos: ", e)
