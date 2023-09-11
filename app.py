from app import app
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Configuración de la base de datos (reemplaza con tus propias credenciales)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DB'] = 'bases de datos'

# Función para establecer la conexión a la base de datos
def conectar_bd():
    return mysql.connector.connect(
        host=app.config['MYSQL_HOST'],
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        database=app.config['MYSQL_DB']
    )

@app.route('/usuarios')
def listar_usuarios():
    # Conectar a la base de datos
    conn = conectar_bd()
    cursor = conn.cursor()

    # Ejecutar una consulta SQL para obtener todos los usuarios
    cursor.execute("SELECT * FROM users")
    usuarios = cursor.fetchall()

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

    # Renderizar una plantilla HTML para mostrar los usuarios
    return render_template('lista_usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True, port=4000)
