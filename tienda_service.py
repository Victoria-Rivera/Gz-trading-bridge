import pagos_service as pagos
import auth_service as auth

CATALOGO = [
    {"id": 1, "nombre": "Pack Carcasas Silicona", "precio": 9990},
    {"id": 2, "nombre": "Parlante RGB Bluetooth", "precio": 34990},
    {"id": 3, "nombre": "Notebook HP 15\" Win 11", "precio": 399990},
    {"id": 4, "nombre": "Audífonos Bluetooth In-Ear", "precio": 19990}
]

carrito = []
sesion_activa = False

print("  GZ-TRADING-BRIDGE ")
print("    ¡Bienvenido!    ")
# control de acceso
while not sesion_activa:
    print("--- INICIO DE SESIÓN ---")
    user = input("Correo: ")
    password = input("Contraseña: ")

    # Conexion a auth_service
    resultado = auth.validar_credenciales(user, password)

    if resultado == "OK":
        print("Acceso concedido. Inicializando entorno de usuario.")
        sesion_activa = True
    elif resultado == "BLOQUEADO":
        print("Cuenta bloqueada en XAMPP por exceso de intentos erróneos.")
        exit() # Corta la ejecución del programa
    elif resultado == "ERROR_LARGO":
        print("La contraseña debe tener más de 8 caracteres.")
    else:
        print("Credenciales inválidas. Intente nuevamente.")

while sesion_activa:
    print("\n=========================================")
    print("          MENÚ PRINCIPAL                   ")
    print("   ¡Bienvenido a GZ-Trading-Bridge!        ")
    print(" =========================================")
    print("1. Ver Catálogo y Agregar Productos")
    print("2. Ver mi Carrito de Compras")
    print("3. Proceder al Pago (Checkout)")
    print("4. Cerrar Sesión y Salir")
    print("-----------------------------------------")
  
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        print("\n=========================================")
        print("          CATÁLOGO DE PRODUCTOS          ")
        print("=========================================")
        for prod in CATALOGO:
            print(f"[{prod['id']}] {prod['nombre']} - ${prod['precio']:,}".replace(",", "."))
        print("-----------------------------------------")

        try:
            prod_id = int(input("Ingrese el ID del producto que desea añadir: "))
            seleccionado = next((p for p in CATALOGO if p["id"] == prod_id), None)
            
            if seleccionado:
                cantidad = int(input(f"¿Cuántas unidades de '{seleccionado['nombre']}' desea agregar? "))
                if cantidad > 0:
                    item_carrito = {
                        "nombre": seleccionado["nombre"],
                        "precio": seleccionado["precio"],
                        "cantidad": cantidad,
                        "subtotal": seleccionado["precio"] * cantidad
                    }
                    carrito.append(item_carrito)
                    print(f"{cantidad}x '{seleccionado['nombre']}' añadido(s) al carrito.")
                else:
                    print("La cantidad ingresada debe ser mayor a cero.")
            else:
                print("El ID de producto seleccionado no existe.")
                
        except ValueError:
            print("Se ingresó un carácter alfabético o no numérico inválido, intente nuevamente")


    elif opcion == "2":
        print("\n=========================================")
        print("     CARRITO DE COMPRAS (TIENDA-SERVICE) ")
        print("=========================================")
        if not carrito:
            print("Su carrito se encuentra actualmente vacío.")
        else:
            neto_total = 0
            for item in carrito:
                print(f"• {item['nombre']} x{item['cantidad']} - Subtotal: ${item['subtotal']:,}".replace(",", "."))
                neto_total += item["subtotal"]
            print("-----------------------------------------")
            print(f"Subtotal Neto Acumulado: ${neto_total:,}".replace(",", "."))

        print("-----------------------------------------")
        input("Presione ENTER para regresar al menú principal...")

    elif opcion == "3":
        if not carrito:
            print("El carrito está vacío. Ingrese artículos en el catálogo antes.")
            continue
            
        print("\n=========================================")
        print("       CHECKOUT DE PAGO (PAGOS-SERVICE)  ")
        print("=========================================")
        
        
        total_neto = sum(item["subtotal"] for item in carrito)
        
        iva, total_final = pagos.calcular_totales(total_neto)

        print(f"Subtotal Neto: ${total_neto:,}".replace(",", "."))
        print(f"IVA (19%):     ${iva:,}".replace(",", "."))
        print(f"Total Final:   ${total_final:,} (IVA Incluido)").replace(",", ".")
        print("-----------------------------------------")
        print("Métodos disponibles: [1] Tarjeta | [2] Mercado Pago | [3] Google Play")
        
        metodo_opcion = input("Seleccione una pasarela (1-3): ")
        metodo = "Tarjeta de Crédito" if metodo_opcion == "1" else "Mercado Pago" if metodo_opcion == "2" else "Google Play"

        confirmar = input("¿Confirmar pago de ${total_final:,} con {metodo}? (si/no): ".replace(",", ".")).lower()
        
        if confirmar == "si":
            pagos.procesar_transaccion(metodo, total_final)
            print("Pago procesado y validado. Ventana de despacho estimado: 24 - 30 JUN.")
            print("¡Gracias por su compra en GZ-Trading-Bridge!")
            break 
        else:
            print("Transacción cancelada por el usuario. Volviendo al menú.")

    elif opcion == "4":
        print("Cerrando sesión de forma segura... Conexiones con XAMPP terminadas. ¡Adiós!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")