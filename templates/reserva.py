from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']
        nombre_libro = request.form['nombre_libro']
        fecha_apartado = request.form['fecha_apartado']
        
        print(f"Reserva realizada: {nombre_completo}, {fecha_nacimiento}, {telefono}, {correo}, {nombre_libro}, {fecha_apartado}")
        
        return render_template('reserva.html', mensaje="Reserva realizada con éxito.")
    
    return render_template('reserva.html', mensaje="Por favor, complete el formulario.")

if __name__ == '__main__':
    app.run(debug=True)

    
    return render_template('reserva.html')  

if __name__ == '__main__':
    app.run(debug=True)
