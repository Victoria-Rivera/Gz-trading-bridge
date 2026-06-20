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

    if not user_data:
        cursor.close()
        conexion.close()
        return "ERROR_DATOS"
    
    if user_data['bloqueado'] == 1:
        cursor.close()
        conexion.close()
        return "BLOQUEADO"
        
    # Validación de longitud de contraseña (Requerimiento)
    if len(clave) < 8:
        cursor.close()
        conexion.close()
        return "ERROR_LARGO"

    # Verificación de coincidencia de credenciales
    if user_data['contrasena'] == clave:
        # Inicio exitoso: se resetean los intentos fallidos en la BD
        cursor.execute("UPDATE usuarios SET intentos_fallidos = 0 WHERE correo = %s", (usuario,))
        conexion.commit()
        resultado = "OK"
    else:
        # Aumento de intentos fallidos por credenciales erróneas
        nuevos_intentos = user_data['intentos_fallidos'] + 1
        if nuevos_intentos >= 3:
            # Bloqueo físico directo en la base de datos al 3er intento
            cursor.execute("UPDATE usuarios SET intentos_fallidos = %s, bloqueado = 1 WHERE correo = %s", (nuevos_intentos, usuario))
            resultado = "BLOQUEADO"
        else:
            cursor.execute("UPDATE usuarios SET intentos_fallidos = %s WHERE correo = %s", (nuevos_intentos, usuario))
            resultado = "ERROR_DATOS"
        conexion.commit()

    cursor.close()
    conexion.close()
    return resultado

