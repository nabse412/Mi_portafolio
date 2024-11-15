from flask import Flask, render_template

app = Flask(__name__)

# Ruta para la página principal (portafolio)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la página de proyectos
@app.route('/proyectos')
def proyectos():
    return render_template('proyectos.html')

if __name__ == '__main__':
    app.run(debug=True)
