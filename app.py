from flask import Flask, request, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='id22192670_socd1',
        password='{mO6d^l>YZ2|7rKO',
        database='id22192670_socd'
    )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=["GET"])
def alumnosBuscar():
    con = get_db_connection()
    cursor = con.cursor()

    cursor.execute("SELECT * FROM tst0_cursos")
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    return jsonify(data=registros)

@app.route("/alumnos/insertar", methods=["POST"])
def alumnosInsertar():
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    grado = request.form["grado"]

    con = get_db_connection()
    cursor = con.cursor()

    sql = "INSERT INTO tst0_cursos (nombre, edad, grado) VALUES (%s, %s, %s)"
    val = (nombre, edad, grado)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    return "Registro insertado correctamente"

@app.route("/alumnos/editar", methods=["POST"])
def alumnosEditar():
    id_curso = request.form["id"]
    nombre = request.form["nombre"]
    edad = request.form["edad"]
    grado = request.form["grado"]

    con = get_db_connection()
    cursor = con.cursor()

    sql = "UPDATE tst0_cursos SET nombre = %s, edad = %s, grado = %s WHERE id = %s"
    val = (nombre, edad, grado, id_curso)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    return "Registro actualizado correctamente"

@app.route("/alumnos/eliminar", methods=["POST"])
def alumnosEliminar():
    id_curso = request.form["id"]

    con = get_db_connection()
    cursor = con.cursor()

    sql = "DELETE FROM tst0_cursos WHERE id = %s"
    val = (id_curso,)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    return "Registro eliminado correctamente"

if __name__ == "__main__":
    app.run(debug=True)

