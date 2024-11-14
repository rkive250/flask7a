from flask import Flask, render_template, request, jsonify
import mysql.connector
import pusher

app = Flask(__name__)

def get_db_connection():
    con = mysql.connector.connect(
        host="185.232.14.52",
        database="u760464709_tst_sep",
        user="u760464709_tst_sep_usr",
        password="dJ0CIAFF="
    )
    return con

@app.route("/")
def index():
    return render_template("WL.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    try:
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

        # Configuración de Pusher
        pusher_client = pusher.Pusher(
            app_id='1864232',
            key='ec020425c2206acb32eb',
            secret='a5091fe74dbda031cda4',
            cluster='us2',
            ssl=True
        )
        pusher_client.trigger("conexion", "evento", {"tel": telefono, "ncurso": nombre_curso})

        # Devolver JSON
        return jsonify({"message": f"Teléfono {telefono} y curso {nombre_curso} guardados correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/buscar")
def buscar():
    try:
        con = get_db_connection()
        if not con.is_connected():
            con.reconnect()

        cursor = con.cursor()
        cursor.execute("SELECT * FROM tst0_cursos")
        registros = cursor.fetchall()

        cursor.close()
        con.close()

        # Devolver registros en JSON
        return jsonify(data=registros)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/alumnos/eliminar/<int:id_curso>", methods=["DELETE"])
def eliminar(id_curso):
    try:
        con = get_db_connection()
        if not con.is_connected():
            con.reconnect()

        cursor = con.cursor()
        sql = "DELETE FROM tst0_cursos WHERE Id_Curso = %s"
        val = (id_curso,)
        cursor.execute(sql, val)
        con.commit()

        cursor.close()
        con.close()

        # Devolver mensaje en JSON
        return jsonify({"message": f"Registro con ID {id_curso} eliminado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/alumnos/editar/<int:id_curso>", methods=["GET", "POST"])
def editar(id_curso):
    con = get_db_connection()
    try:
        if request.method == "GET":
            cursor = con.cursor()
            cursor.execute("SELECT * FROM tst0_cursos WHERE Id_Curso = %s", (id_curso,))
            registro = cursor.fetchone()
            cursor.close()
            return jsonify(data=registro)

        if request.method == "POST":
            telefono = request.form["tel"]
            nombre_curso = request.form["ncurso"]

            cursor = con.cursor()
            sql = "UPDATE tst0_cursos SET Telefono = %s, Nombre_Curso = %s WHERE Id_Curso = %s"
            val = (telefono, nombre_curso, id_curso)
            cursor.execute(sql, val)
            con.commit()

            cursor.close()
            return jsonify({"message": f"Registro con ID {id_curso} actualizado correctamente"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
