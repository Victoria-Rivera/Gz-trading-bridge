import mysql.connector

def conectar_bd():
    # Conexión a la base de datos mediante XAMPP
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="gz_trading"
    )

def validar_credenciales(usuario, clave):
    conexion = conectar_bd()
    cursor = conexion.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM usuarios WHERE correo = %s", (usuario,))
    user_data = cursor.fetchone()

