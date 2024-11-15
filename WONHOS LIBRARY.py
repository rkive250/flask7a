from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('WL.html')

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']
        nombre_libro = request.form['nombre_libro']
        fecha_apartado = request.form['fecha_apartado']
        
        # Aquí puedes procesar los datos (por ejemplo, guardarlos en una base de datos)
        print(f"Reserva realizada: {nombre_completo}, {fecha_nacimiento}, {telefono}, {correo}, {nombre_libro}, {fecha_apartado}")
        
        # Pasamos un mensaje de éxito al renderizar la plantilla
        return render_template('reserva.html', mensaje="Reserva realizada con éxito.")
    
    # Si es un GET, mostramos el formulario vacío
    return render_template('reserva.html', mensaje="Por favor, complete el formulario.")

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    if request.method == 'POST':
        return "Búsqueda realizada."
    return render_template('buscar.html')

@app.route('/categorias')
def categorias():
    return render_template('categorias.html')

@app.route('/ocupados')
def ocupados():
    return render_template('ocupados.html')

@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    if request.method == 'POST':
        return "Inicio de sesión realizado."
    return render_template('inicio_sesion.html')

@app.route('/proximos-stock')
def proximos_stock():
    return render_template('proximos_stock.html')

if __name__ == '__main__':
    app.run(debug=True)
