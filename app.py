from flask import Flask, render_template, request
import pusher
import mysql.connector
import datetime
import pytz

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
    return render_template("app.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    telefono = request.form["tel"]
    nombre_curso = request.form["ncurso"]
    return f"telefono {telefono} curso: {nombre_curso}"

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

    return str(registros)

@app.route("/evento", methods=["GET"])
def evento():
    pusher_client = pusher.Pusher(
        app_id='1864232',
        key='ec020425c2206acb32eb',
        secret='a5091fe74dbda031cda4',
        cluster='us2',
        ssl=True
    )

    con = get_db_connection()

    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor()
    args = request.args

    sql = "INSERT INTO tst0_cursos (Telefono, Nombre_Curso) VALUES (%s, %s)"
    val = (args["tel"], args["ncurso"])
    cursor.execute(sql, val)
    con.commit()

    cursor.close()
    con.close()

    pusher_client.trigger("conexion", "evento", args)
    return args
