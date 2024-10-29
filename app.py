from flask import Flask, render_template, request

app = Flask(__name__)

# Ruta principal
@app.route('/')
def home():
    return render_template('app.html')

# Rutas para las diferentes funcionalidades
@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        # Aquí puedes manejar la lógica para reservar un libro
        return "Reserva realizada."
    return render_template('app.html')

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        # Aquí puedes manejar la lógica para buscar un libro
        return "Búsqueda realizada."
    return render_template('app.html')

@app.route('/categorias')
def categorias():
    # Aquí puedes manejar la lógica para mostrar categorías
    return render_template('app.html')

@app.route('/ocupados')
def ocupados():
    # Aquí puedes manejar la lógica para mostrar libros ocupados
    return render_template('app.html')

if __name__ == '__main__':
    app.run(debug=True)

