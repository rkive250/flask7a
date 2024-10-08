from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# Configuración para conectar con la base de datos
def get_db_connection():
    con = mysql.connector.connect(
        host="185.232.14.52",
        database="u760464709_tst_sep",
        user="u760464709_tst_sep_usr",
        password="dJ0CIAFF="
    )
    return con

# Ruta principal que muestra el archivo HTML
@app.route("/")
def index():
    return render_template("app.html")

# Ruta para guardar los datos de un nuevo alumno en la base de datos
@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    telefono = request.form["tel"]
    nombre_curso = request.form["ncurso"]

    con = get_db_connection()
    cursor = con.cursor()

    sql = "INSERT INTO tst0_cursos (Telefono, Nombre_Curso) VALUES (%s, %s)"
    val = (telefono, nombre_curso)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    return "Registro guardado correctamente"

# Ruta para actualizar un registro existente
@app.route("/alumnos/actualizar", methods=["POST"])
def alumnosActualizar():
    id_curso = request.form["id"]
    telefono = request.form["tel"]
    nombre_curso = request.form["ncurso"]

    con = get_db_connection()
    cursor = con.cursor()

    sql = "UPDATE tst0_cursos SET Telefono = %s, Nombre_Curso = %s WHERE id = %s"
    val = (telefono, nombre_curso, id_curso)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    return "Registro actualizado correctamente"

# Ruta para eliminar un registro
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

# Ruta para buscar y devolver los registros de la tabla en formato JSON
@app.route("/buscar", methods=["GET"])
def buscar():
    nombre_curso = request.args.get("ncurso", "")  # Obtiene el parámetro de búsqueda (opcional)
    con = get_db_connection()
    cursor = con.cursor()

    if nombre_curso:  # Si se proporciona un nombre de curso para buscar
        sql = "SELECT * FROM tst0_cursos WHERE Nombre_Curso LIKE %s"
        cursor.execute(sql, ('%' + nombre_curso + '%',))
    else:  # Si no se proporciona un nombre, muestra todos los registros
        cursor.execute("SELECT * FROM tst0_cursos")

    registros = cursor.fetchall()
    cursor.close()
    con.close()

    return jsonify(data=registros)

if __name__ == "__main__":
    app.run(debug=True)  
