from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('WL.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        return "Reserva realizada."
    return render_template('reserva.html')  # Asegúrate de que 'reserva.html' esté bien configurado

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        return "Búsqueda realizada."
    return render_template('buscar.html')  # Crear una plantilla de búsqueda

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')  # Crear plantilla para categorías

@app.route('/ocupados')
def ocupados():
    return render_template('ocupados.html')  # Plantilla para libros ocupados

@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        return "Inicio de sesión realizado."
    return render_template('inicio_sesion.html')  # Crear plantilla para inicio de sesión

@app.route('/proximos-stock')
def proximos_stock():
    return render_template('proximos_stock.html')  # Plantilla para próximos libros a salir de stock

if __name__ == '__main__':
    app.run(debug=True)
