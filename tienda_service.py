import random  
import Funciones.pagos_service as pagos
import Funciones.auth_service as auth

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


while not sesion_activa:
    print("--- INICIO DE SESIÓN ---")
    user = input("Correo: ")
    password = input("Contraseña: ")


    resultado = auth.validar_credenciales(user, password)

    if resultado == "OK":
        print("Acceso concedido. Inicializando entorno de usuario.")
        sesion_activa = True
    elif resultado == "BLOQUEADO":
        print("Cuenta bloqueada en XAMPP por exceso de intentos erróneos.")
        exit() 
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
            print(f"[{prod['id']}] {prod['nombre']} - {pagos.formatear_dinero(prod['precio'])}")
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
                print(f"• {item['nombre']} x{item['cantidad']} - Subtotal: {pagos.formatear_dinero(item['subtotal'])}")
                neto_total += item["subtotal"]
            print("-----------------------------------------")
            print(f"Subtotal Neto Acumulado: {pagos.formatear_dinero(neto_total)}")

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
        
        #Descuento random
        descuentos_posibles = [0, 10, 15, 25, 50]
        porcentaje_desc = random.choice(descuentos_posibles)
        
        monto_descuento = total_neto * (porcentaje_desc / 100)
        neto_con_descuento = total_neto - monto_descuento
        
        iva, total_final = pagos.calcular_totales(neto_con_descuento)

        print(f"Subtotal Neto Inicial: {pagos.formatear_dinero(total_neto)}")
        
        if porcentaje_desc > 0:
            print(f"¡Cupón Sorpresa Aplicado!: {porcentaje_desc}% de descuento")
            print(f"Monto Descontado:      -{pagos.formatear_dinero(monto_descuento)}")
            print(f"Nuevo Neto:            {pagos.formatear_dinero(neto_con_descuento)}")
        else:
            print("Cupón Sorpresa: Hoy no hubo suerte (0% de descuento)")
            
        print(f"IVA (19%):             {pagos.formatear_dinero(iva)}")
        print(f"Total Final a Pagar:   {pagos.formatear_dinero(total_final)} (IVA Incluido)")
        print("-----------------------------------------")
        print("Métodos disponibles: [1] Tarjeta | [2] Mercado Pago | [3] Google Play")
        
        metodo_opcion = input("Seleccione una pasarela (1-3): ")
        metodo = "Tarjeta de Crédito" if metodo_opcion == "1" else "Mercado Pago" if metodo_opcion == "2" else "Google Play"

        confirmar = input(f"¿Confirmar pago de {pagos.formatear_dinero(total_final)} con {metodo}? (si/no): ").lower()
        
        if confirmar == "si":
            pagos.procesar_transaccion(metodo, total_final)
            print("Pago procesado y validado. Ventana de despacho estimado: 24 - 30 JUN.")
            print("¡Gracias por su compra en GZ-Trading-Bridge!")
            break 
        else:
            print("Transacción cancelada por el usuario. Volviendo al menú.")

    elif opcion == "4":
        print("Cerrando sesión de forma segura... ¡Adiós :)!")
        break
    else:
        print("Opción no válida. Por favor, ingrese un número del 1 al 4.")