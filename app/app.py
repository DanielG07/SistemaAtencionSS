import os
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename
from lee_pdf import lectura

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "./app/pdfs"

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

@app.route("/registro/confirmacion_datos", methods=['POST'])
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

if __name__== '__main__':
    app.run(debug=True,port=5000)