from flask import Flask, request, jsonify
import mysql.connector
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Función para obtener la conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="tu_usuario",  # Cambia por tu usuario de MySQL
        password="tu_contraseña",  # Cambia por tu contraseña de MySQL
        database="tu_base_de_datos"  # Cambia por tu base de datos de MySQL
    )

# Ruta para buscar cursos en la base de datos
@app.route("/buscar", methods=["GET"])
def buscar():
    nombre_curso = request.args.get("ncurso", "")  # Obtiene el parámetro del curso de la solicitud
    con = get_db_connection()
    cursor = con.cursor()

    if nombre_curso:  # Si se proporciona un nombre de curso
        sql = "SELECT * FROM tst0_cursos WHERE Nombre_Curso LIKE %s"
        cursor.execute(sql, ('%' + nombre_curso + '%',))
    else:  # Si no se proporciona un nombre de curso, muestra todos los registros
        cursor.execute("SELECT * FROM tst0_cursos")

    registros = cursor.fetchall()
    cursor.close()
    con.close()

    # Verifica que haya registros para devolver
    if registros:
        return jsonify(data=registros)  # Línea corregida
    else:
        return jsonify(data=[])

# Ruta para insertar un nuevo curso en la base de datos
@app.route("/insertar", methods=["POST"])
def insertar():
    datos = request.json
    nombre_curso = datos.get("ncurso", "")
    duracion = datos.get("duracion", "")

    if not nombre_curso or not duracion:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    con = get_db_connection()
    cursor = con.cursor()

    try:
        sql = "INSERT INTO tst0_cursos (Nombre_Curso, Duracion) VALUES (%s, %s)"
        cursor.execute(sql, (nombre_curso, duracion))
        con.commit()
        return jsonify({"message": "Curso insertado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

# Ruta para actualizar un curso existente en la base de datos
@app.route("/actualizar", methods=["PUT"])
def actualizar():
    datos = request.json
    id_curso = datos.get("idcurso", "")
    nombre_curso = datos.get("ncurso", "")
    duracion = datos.get("duracion", "")

    if not id_curso or not nombre_curso or not duracion:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    con = get_db_connection()
    cursor = con.cursor()

    try:
        sql = "UPDATE tst0_cursos SET Nombre_Curso = %s, Duracion = %s WHERE idCurso = %s"
        cursor.execute(sql, (nombre_curso, duracion, id_curso))
        con.commit()
        return jsonify({"message": "Curso actualizado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

# Ruta para eliminar un curso de la base de datos
@app.route("/eliminar", methods=["DELETE"])
def eliminar():
    datos = request.json
    id_curso = datos.get("idcurso", "")

    if not id_curso:
        return jsonify({"error": "Falta el ID del curso"}), 400

    con = get_db_connection()
    cursor = con.cursor()

    try:
        sql = "DELETE FROM tst0_cursos WHERE idCurso = %s"
        cursor.execute(sql, (id_curso,))
        con.commit()
        return jsonify({"message": "Curso eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

if __name__ == "__main__":
    app.run(debug=True)


return jsonify(data=registros)

if __name__ == "__main__":
    app.run(debug=True)
