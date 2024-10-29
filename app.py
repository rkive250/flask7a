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
    return render_template("index.html")

# Si no necesitas las rutas de alumnos, puedes eliminarlas o adaptarlas según tus necesidades.

if __name__ == "__main__":
    app.run(debug=True)
