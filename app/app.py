from flask import Flask,render_template

app = Flask(__name__)

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

if __name__== '__main__':
    app.run(debug=True,port=5000)