from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': 'sql202.infinityfree.com',
    'user': 'if0_37717099',
    'password': 'rkive12345',
    'database': 'if0_37717099_XXX'
}

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    if request.method == 'POST':
        nombre_completo = request.form['nombre_completo']
        fecha_nacimiento = request.form['fecha_nacimiento']
        telefono = request.form['telefono']
        correo = request.form['correo']
        nombre_libro = request.form['nombre_libro']
        fecha_apartado = request.form['fecha_apartado']
        
        # Conexión a la base de datos
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        
        sql = """
        INSERT INTO wonhoslib (nombre_completo, fecha_nacimiento, telefono, correo, nombre_libro, fecha_apartado)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(sql, (nombre_completo, fecha_nacimiento, telefono, correo, nombre_libro, fecha_apartado))
        conn.commit()  # Confirmar los cambios
        
        cursor.close()
        conn.close()
        
        return "Reserva realizada con éxito."
    
    return render_template('reserva.html')  # Asegúrate de que esta plantilla esté bien configurada

if __name__ == '__main__':
    app.run(debug=True)
