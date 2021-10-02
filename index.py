from logging import debug
from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template ('index.html')
    
@app.route('/contacto')
def contacto():
    return render_template ('contacto.html')

@app.route('/lenguajes')
def mostrarLenguajes():
    listlenguajes=("PHP", "Python","Java","Perl","JavaScriipt","Rubby","Rust")

    return render_template ('lenguajes.html', lenguajes=listlenguajes)

if __name__ == '__main__':
    app.run(debug=True, port=5017)

