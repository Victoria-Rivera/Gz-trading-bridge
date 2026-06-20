import mysql.connector

def conectar_bd():
    # Conexión a la base de datos mediante XAMPP
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="gz_trading"
    )

