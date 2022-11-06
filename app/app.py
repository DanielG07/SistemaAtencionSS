from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    #return "<h1>Hola Mundo!!!!!!!!</h1>"
    cursos = ['PHP','Python','Java']
    data={
        'titulo':'Este es el titulo',
        'bienvenida':'saludos',
        'cursos':cursos,
        'numero_cursos':len(cursos)
    }
    return render_template('index.html',data=data)

if __name__== '__main__':
    app.run(debug=True,port=5000)