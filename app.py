from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='id22192670_socd1',
        password='{mO6d^l>YZ2|7rKO',
        database='id22192670_socd'
    )

@app.route("/cursos", methods=["GET"])
def obtener_cursos():
    con = get_db_connection()
    cursor = con.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tst0_cursos")
    registros = cursor.fetchall()
    cursor.close()
    con.close()
    return jsonify(data=registros)

@app.route("/agregar", methods=["POST"])
def agregar():
    datos = request.json
    nombre_curso = datos.get("ncurso")
    duracion = datos.get("duracion")

    if not nombre_curso or not duracion:
        return jsonify({"error": "Faltan datos obligatorios"}), 400

    con = get_db_connection()
    cursor = con.cursor()

    try:
        sql = "INSERT INTO tst0_cursos (Nombre_Curso, Duracion) VALUES (%s, %s)"
        cursor.execute(sql, (nombre_curso, duracion))
        con.commit()
        return jsonify({"message": "Curso agregado correctamente"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

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
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Curso no encontrado"}), 404
        
        return jsonify({"message": "Curso actualizado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

@app.route("/eliminar/<int:idcurso>", methods=["DELETE"])
def eliminar(idcurso):
    con = get_db_connection()
    cursor = con.cursor()

    try:
        sql = "DELETE FROM tst0_cursos WHERE idCurso = %s"
        cursor.execute(sql, (idcurso,))
        con.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"error": "Curso no encontrado"}), 404
        
        return jsonify({"message": "Curso eliminado correctamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        con.close()

if __name__ == "__main__":
    app.run(debug=True)
