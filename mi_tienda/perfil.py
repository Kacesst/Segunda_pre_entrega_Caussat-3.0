
def ver_perfil(cliente):
    print("======= PERFIL DEL CLIENTE =======")
    print(f"Nombre: {cliente.nombre} {cliente.apellido}")
    print(f"DNI: {cliente.dni}")
    print(f"Teléfono: {cliente.telefono}")
    print(f"Correo electrónico: {cliente.email}")
    print("\nOpciones:")
    print("1. Ver carrito de compras")
    print("2. Realizar una compra")
    print("3. Volver al menú principal")
    
    opcion = input("Ingrese el número de opción que desee: ")
    
    if opcion == "1":
        mostrar_carrito(cliente)
    elif opcion == "2":
        realizar_compra(cliente)
    elif opcion == "3":
        print("Volviendo al menú principal.")
    else:
        print("Opción inválida. Por favor, ingrese un número válido del menú.\n")

def mostrar_carrito(cliente):
    print("======= CARRITO DE COMPRAS =======")
    if not cliente.carrito:
        print("El carrito está vacío.\n")
    else:
        for idx, item in enumerate(cliente.carrito, 1):
            producto = item["producto"]
            cantidad = item["cantidad"]
            print(f"{idx}. {producto.nombre} - Cantidad: {cantidad}")
        total_carrito = obtener_total_carrito(cliente)
        print(f"Total a pagar: ${total_carrito}\n")

def realizar_compra(cliente):
    print("======= REALIZAR COMPRA =======")
    mostrar_carrito(cliente)
    print("Ingrese los siguientes datos para completar la compra:")
    # Solicitar los datos necesarios para completar la compra
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    telefono = input("Teléfono: ")
    dni = input("DNI: ")
    direccion = input("Dirección: ")
    tarjeta_credito = input("Tarjeta de crédito: ")
    
    total_carrito = obtener_total_carrito(cliente)
    costo_envio = 10  # Costo fijo de envío en dólares
    porcentaje_venta = 5  # Porcentaje adicional por venta en porcentaje
    
    print(f"Total a pagar por productos: ${total_carrito}")
    
    costo_total = cliente.obtener_total_carrito() + costo_envio + (costo_envio * porcentaje_venta / 100)
    print(f"Costo total de la compra (con envío y porcentaje): ${costo_total}")
    
    confirmacion = input("¿Desea confirmar la compra? (s/n): ")
    
    if confirmacion.lower() == "s":
        
        cliente.carrito = []  
        print("¡Compra realizada con éxito! Gracias por su compra.")
    else:
        print("Compra cancelada. Gracias por visitar nuestra tienda.")      

def obtener_total_carrito(cliente):
    total = 0
    for item in cliente.carrito:
        producto = item["producto"]
        cantidad = item["cantidad"]
        total += producto.precio * cantidad
    return total
