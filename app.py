from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Main page of Wonhos Library
    return render_template("index.html")

@app.route("/reserva")
def reserva():
    # Page for making reservations
    return render_template("reserva.html")

@app.route("/inicio_sesion")
def inicio_sesion():
    # Page for user login
    return render_template("inicio_sesion.html")

@app.route("/buscar")
def buscar():
    # Page for searching books
    return render_template("buscar.html")

@app.route("/categorias")
def categorias():
    # Page for browsing categories
    return render_template("categorias.html")

@app.route("/ocupados")
def ocupados():
    # Page to view occupied books or reserved ones
    return render_template("ocupados.html")

if __name__ == "__main__":
    app.run(debug=True)
