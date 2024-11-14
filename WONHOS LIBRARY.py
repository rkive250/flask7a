from flask import Flask, render_template, request
from wonhos_library import PageFactory

app = Flask(__name__)

@app.route('/')
def home():
    page = PageFactory.create_page("home")
    return render_template('WL.html', title="Bienvenido a Wonhos Library")

@app.route('/reserva', methods=['GET', 'POST'])
def reserva():
    page = PageFactory.create_page("reserva")
    if request.method == 'POST':
        return "Reserva realizada."
    return render_template('WL.html', title="Reserva")

@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    page = PageFactory.create_page("buscar")
    if request.method == 'POST':
        return "Búsqueda realizada."
    return render_template('WL.html', title="Buscar")

@app.route('/categorias')
def categorias():
    page = PageFactory.create_page("categorias")
    return render_template('WL.html', title="Categorías")

@app.route('/ocupados')
def ocupados():
    page = PageFactory.create_page("ocupados")
    return render_template('WL.html', title="Ocupados")

@app.route('/inicio-sesion', methods=['GET', 'POST'])
def inicio_sesion():
    page = PageFactory.create_page("inicio-sesion")
    if request.method == 'POST':
        return "Inicio de sesión realizado."
    return render_template('WL.html', title="Inicio de Sesión")

@app.route('/proximos-stock')
def proximos_stock():
    page = PageFactory.create_page("proximos-stock")
    return render_template('WL.html', title="Próximos a Salir de Stock")

if __name__ == '__main__':
    app.run(debug=True)
