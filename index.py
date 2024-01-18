from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/nosotros')
def nosotros():
    return render_template('nosotros.html')
    
@app.route('/admision')
def admision():
    return render_template('admision.html')

@app.route('/eduplasticas')
def eduplasticas():
    return render_template('eduplasticas.html')

@app.route('/edumusica')
def edumusica():
    return render_template('edumusica.html')

@app.route('/edudanza')
def edudanza():
    return render_template('edudanza.html')

@app.route('/formusica')
def formusica():
    return render_template('formusica.html')

@app.route('/forplasticas')
def forplasticas():
    return render_template('forplasticas.html')

@app.route('/planadocente')
def planadocente():
    return render_template('planadocente.html')

@app.route('/documentos')
def documentos():
    return render_template('documentos.html')

@app.route('/accesos')
def accesos():
    return render_template('accesos.html')

@app.route('/repositorio')
def repositorio():
    return render_template('repositorio.html')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html')


if __name__ == '__main__':
    app.run(debug=True)