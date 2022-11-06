import os
from flask import Flask,render_template, request, url_for,redirect
from werkzeug.utils import secure_filename
from lee_pdf import lectura

app = Flask(__name__)
app.config['UPLOADER_FOLDER'] = "./app/pdfs"

@app.route("/registro",methods=['GET','POST'])
def upload_file():
    cursos = ['PHP','Python','Java']
    data={
        'nombre':'Jorge Angel',
        'a_paterno':'Cruz',
        'a_materno':'Meneses',
        'boleta':'2019640027',
        'curp':'CUMJ000723HMCRNRA8',
        'carrera':4,
        'semestre':3,
        'genero':2,
        'prestatario':'ESCA Santo Tomás',
        'correo':'jorgecruzmen2000@gmail.com',
        'fechainicio':'2022-10-03',
        'fechatermino':'2023-04-04'
    }
    return render_template('registro.html',data=data)

@app.route("/registro/confirmacion_datos",methods=['POST'])
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

if __name__ == '__main__':
    app.run(debug=True,port=5002)