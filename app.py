from flask import Flask

from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("app.html")

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/alumnos/guardar", methods=["POST"])
def alumnosGuardar():
    matricula = request.form["txtMatriculaFA"]
    nombreapellido = request.form["txtNombreApellidoFA"]
    return f"Matrícula: {matricula} Nombre y Apellido: {nombreapellido}"
@app.route("/evento")
def evento ()
import pusher

pusher_client = pusher.Pusher(
  app_id='1864232',
  key='ec020425c2206acb32eb',
  secret='a5091fe74dbda031cda4',
  cluster='us2',
  ssl=True
)

pusher_client.trigger('conexion', 'evento', {'message': 'hello world'})
