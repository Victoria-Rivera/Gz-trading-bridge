import mysql.connector

def conectar_bd():
    #Conexion a mysql
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  
        database="gz_trading"
    )

def validar_credenciales(usuario, clave):
    try:
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
            
        if len(clave) < 8:
            cursor.close()
            conexion.close()
            return "ERROR_LARGO"

        if user_data['contrasena'] == clave:
            cursor.execute("UPDATE usuarios SET intentos_fallidos = 0 WHERE correo = %s", (usuario,))
            conexion.commit()
            resultado = "OK"
        else:
            nuevos_intentos = user_data['intentos_fallidos'] + 1
            if nuevos_intentos >= 3:
                cursor.execute("UPDATE usuarios SET intentos_fallidos = %s, bloqueado = 1 WHERE correo = %s", (nuevos_intentos, usuario))
                resultado = "BLOQUEADO"
            else:
                cursor.execute("UPDATE usuarios SET intentos_fallidos = %s WHERE correo = %s", (nuevos_intentos, usuario))
                resultado = "ERROR_DATOS"
            conexion.commit()

        cursor.close()
        conexion.close()
        return resultado

    except mysql.connector.Error:
        
        #Si el servidor falla o no encuentra la base de datos se puede iniciar igualmente
        print("Servidor XAMPP no detectado. Activando entorno de simulación local (QA Offline).")
        
        # Validación de longitud 
        if len(clave) < 8:
            return "ERROR_LARGO"
            
        # Credenciales de prueba
        if usuario == "victoria@duocuc.cl" and clave == "clave1234":
            return "OK"
        else:
            return "ERROR_DATOS"