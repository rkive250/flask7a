from flask import Flask, render_template, request, jsonify
import mysql.connector
import pusher

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

    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()

    sql = "INSERT INTO tst0_cursos (Telefono, Nombre_Curso) VALUES (%s, %s)"
    val = (telefono, nombre_curso)
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    # Emitir evento de Pusher
    pusher_client = pusher.Pusher(
        app_id='1864232',
        key='ec020425c2206acb32eb',
        secret='a5091fe74dbda031cda4',
        cluster='us2',
        ssl=True
    )
    pusher_client.trigger("conexion", "evento", {"tel": telefono, "ncurso": nombre_curso})

    return f"Teléfono {telefono} y curso {nombre_curso} guardados correctamente"

# Ruta para buscar y devolver los registros de la tabla en formato JSON
@app.route("/buscar")
def buscar():
    con = get_db_connection()
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()
    cursor.execute("SELECT * FROM tst0_cursos")
    registros = cursor.fetchall()

    cursor.close()
    con.close()

    # Devolver los registros en formato JSON
    return jsonify(data=registros)

# Ruta para eliminar un registro en la base de datos
@app.route("/alumnos/eliminar/<int:id_curso>", methods=["DELETE"])
def alumnosEliminar(id_curso):
    con = get_db_connection()
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()
    
    try:
        sql = "DELETE FROM tst0_cursos WHERE Id_Curso = %s"
        cursor.execute(sql, (id_curso,))
        con.commit()

        affected_rows = cursor.rowcount  # Verifica cuántas filas se han afectado

        if affected_rows > 0:
            return f"Registro con ID {id_curso} eliminado correctamente", 200
        else:
            return f"Error: No se pudo eliminar el registro con ID {id_curso} o no existe", 404

    except Exception as e:
        return f"Error al eliminar el registro: {str(e)}", 500
    finally:
        cursor.close()
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
