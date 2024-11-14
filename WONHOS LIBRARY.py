from flask import Flask, render_template, request

app = Flask(__name__)

def crear_vista(template_name, mensaje=None):
    def vista():
        if request.method == 'POST' and mensaje:
            return mensaje
        return render_template(template_name)
    return vista

app.route('/')(crear_vista('WL.html'))
app.route('/reserva', methods=['GET', 'POST'])(crear_vista('WL.html', "Reserva realizada."))
app.route('/buscar', methods=['GET', 'POST'])(crear_vista('WL.html', "Búsqueda realizada."))
app.route('/categorias')(crear_vista('WL.html'))
app.route('/ocupados')(crear_vista('WL.html'))
app.route('/inicio-sesion', methods=['GET', 'POST'])(crear_vista('WL.html', "Inicio de sesión realizado."))
app.route('/proximos-stock')(crear_vista('WL.html'))

if __name__ == '__main__':
    app.run(debug=True)
