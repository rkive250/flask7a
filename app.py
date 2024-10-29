from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('app.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        return "Reserva realizada."
    return render_template('app.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        return "Búsqueda realizada."
    return render_template('app.html')

@app.route('/categorias')
def categorias():
    return render_template('app.html')

@app.route('/ocupados')
def ocupados():
    return render_template('app.html')

@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        return "Inicio de sesión realizado."
    return render_template('app.html')

@app.route('/proximos-stock')
def proximos_stock():
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)
