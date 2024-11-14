from flask import Flask, request, jsonify
from flask_mysql_connector import MySQL
import pusher

app = Flask(__name__)

class MySQLConnectionFactory:
    @staticmethod
    def create_connection(app):
        app.config['MYSQL_HOST'] = '185.232.14.52'
        app.config['MYSQL_DATABASE'] = 'u760464709_tst_sep'
        app.config['MYSQL_USER'] = 'u760464709_tst_sep_usr'
        app.config['MYSQL_PASSWORD'] = 'dJ0CIAFF='
        return MySQL(app)

mysql = MySQLConnectionFactory.create_connection(app)

pusher_client = pusher.Pusher(
    app_id='1864232',
    key='ec020425c2206acb32eb',
    secret='a5091fe74dbda031cda4',
    cluster='us2',
    ssl=True


)

class CursoCRUD:
    @staticmethod
    def obtener_todos():
        try:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("SELECT Id_Curso, Nombre_Curso, Telefono FROM tst0_cursos")
            return cursor.fetchall()
        except Exception as e:
            return str(e)
    
    @staticmethod
    def guardar(nombre_curso, telefono):
        try:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("INSERT INTO tst0_cursos (Nombre_Curso, Telefono) VALUES (%s, %s)", (nombre_curso, telefono))
            conn.commit()
            
            pusher_client.trigger('conexion', 'evento', {'tel': telefono, 'ncurso': nombre_curso})
            
            return "Registro guardado exitosamente."
        except Exception as e:
            return str(e)
    
    @staticmethod
    def eliminar(id_curso):
        try:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tst0_cursos WHERE Id_Curso = %s", (id_curso,))
            conn.commit()
            return "Registro eliminado exitosamente."
        except Exception as e:
            return str(e)

    @staticmethod
    def obtener_por_id(id_curso):
        try:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("SELECT Id_Curso, Nombre_Curso, Telefono FROM tst0_cursos WHERE Id_Curso = %s", (id_curso,))
            return cursor.fetchone()
        except Exception as e:
            return str(e)
    
    @staticmethod
    def actualizar(id_curso, nombre_curso, telefono):
        try:
            conn = mysql.connection
            cursor = conn.cursor()
            cursor.execute("UPDATE tst0_cursos SET Nombre_Curso = %s, Telefono = %s WHERE Id_Curso = %s", (nombre_curso, telefono, id_curso))
            conn.commit()
            return "Registro actualizado exitosamente."
        except Exception as e:
            return str(e)

@app.route('/buscar', methods=['GET'])
def buscar():
    data = CursoCRUD.obtener_todos()
    if isinstance(data, str):
        return jsonify({'error': data})
    return jsonify({'data': data})

@app.route('/alumnos/guardar', methods=['POST'])
def guardar():
    nombre_curso = request.form['ncurso']
    telefono = request.form['tel']
    mensaje = CursoCRUD.guardar(nombre_curso, telefono)
    if "error" in mensaje.lower():
        return jsonify({'error': mensaje})
    return jsonify({'message': mensaje})

@app.route('/alumnos/eliminar/<int:id_curso>', methods=['DELETE'])
def eliminar(id_curso):
    mensaje = CursoCRUD.eliminar(id_curso)
    if "error" in mensaje.lower():
        return jsonify({'error': mensaje})
    return jsonify({'message': mensaje})

@app.route('/alumnos/editar/<int:id_curso>', methods=['GET'])
def obtener_datos(id_curso):
    data = CursoCRUD.obtener_por_id(id_curso)
    if isinstance(data, str):
        return jsonify({'error': data})
    return jsonify({'data': data})

@app.route('/alumnos/editar/<int:id_curso>', methods=['POST'])
def editar(id_curso):
    nombre_curso = request.form['ncurso']
    telefono = request.form['tel']
    mensaje = CursoCRUD.actualizar(id_curso, nombre_curso, telefono)
    if "error" in mensaje.lower():
        return jsonify({'error': mensaje})
    return jsonify({'message': mensaje})

if __name__ == '__main__':
    app.run(debug=True)
