
CATALOGO = [
    {"id": 1, "nombre": "Pack Carcasas Silicona", "precio": 9990},
    {"id": 2, "nombre": "Parlante RGB Bluetooth", "precio": 34990},
    {"id": 3, "nombre": "Notebook HP 15\" Win 11", "precio": 399990},
    {"id": 4, "nombre": "Audífonos Bluetooth In-Ear", "precio": 19990}
]

carrito = []


print("\n=========================================")
print("          MENÚ PRINCIPAL                   ")
print("   ¡Bienvenido a GZ-Trading-Bridge!        ")
print(" =========================================")
print("1. Ver Catálogo y Agregar Productos")
print("2. Ver mi Carrito de Compras")
print("3. Proceder al Pago (Checkout)")
print("5. Cerrar Sesión y Salir")
print("-----------------------------------------")
  
opcion = input("Seleccione una opción (1-5): ")

if opcion == "1":
    print("\n=========================================")
    print("          CATÁLOGO DE PRODUCTOS          ")
    print("=========================================")
    for prod in CATALOGO:
        print(f"[{prod['id']}] {prod['nombre']} - ${prod['precio']:,}".replace(",", "."))
        print("-----------------------------------------")

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
            print(f"\n[Éxito]: {cantidad}x '{seleccionado['nombre']}' añadido(s) al carrito.")
    else:
        print("La cantidad ingresada debe ser mayor a cero.")

else:
        print("El ID de producto seleccionado no existe.")