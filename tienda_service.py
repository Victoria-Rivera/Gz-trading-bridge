
CATALOGO = [
    {"id": 1, "nombre": "Pack Carcasas Silicona", "precio": 9990},
    {"id": 2, "nombre": "Parlante RGB Bluetooth", "precio": 34990},
    {"id": 3, "nombre": "Notebook HP 15\" Win 11", "precio": 399990},
    {"id": 4, "nombre": "Audífonos Bluetooth In-Ear", "precio": 19990}
]


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