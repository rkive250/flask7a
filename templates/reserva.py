from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        # Aquí puedes imprimir los datos de la reserva para ver cómo se reciben
        nombre_completo = request.form['nombre_completo']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']
        nombre_libro = request.form['nombre_libro']
        fecha_apartado = request.form['fecha_apartado']
        
        # Temporalmente, solo mostramos los datos en la consola o los retornamos como mensaje
        print(f"Reserva realizada: {nombre_completo}, {fecha_nacimiento}, {telefono}, {correo}, {nombre_libro}, {fecha_apartado}")
        
        # En lugar de conectarse a la base de datos, solo retornamos un mensaje
        return render_template('reserva.html', mensaje="Reserva realizada con éxito.")
    
    return render_template('reserva.html', mensaje="Por favor, complete el formulario.")

if __name__ == '__main__':
    app.run(debug=True)

    
    return render_template('reserva.html')  # Asegúrate de que esta plantilla esté bien configurada

if __name__ == '__main__':
    app.run(debug=True)
