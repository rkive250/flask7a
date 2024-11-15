from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('WL.html', title="Bienvenido a Wonhos Library")

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        nombre = request.form['nombre']
        libro = request.form['libro']
        return f"Reserva realizada para {nombre} con el libro {libro}."
    return render_template('reserva.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        busqueda = request.form['busqueda']
        return f"Resultado de búsqueda para: {busqueda}"
    return render_template('buscar.html')

@app.route('/categorias')
def categorias():
    return render_template('WL.html', title="Categorías")

@app.route('/ocupados')
def ocupados():
    return render_template('WL.html', title="Ocupados")

@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        return f"Inicio de sesión realizado para el usuario: {email}"
    return render_template('inicio_sesion.html')

@app.route('/proximos-stock')
def proximos_stock():
    return render_template('WL.html', title="Próximos a Salir de Stock")

if __name__ == '__main__':
    app.run(debug=True)
