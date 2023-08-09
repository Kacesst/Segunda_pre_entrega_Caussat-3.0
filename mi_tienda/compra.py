import json

def procesar_pago(total):
    print(f"Procesando el pago de ${total}...")
    tarjeta_numero = input("Ingrese el número de la tarjeta de crédito: ")
    tarjeta_expiracion = input("Ingrese la fecha de expiración (MM/AA): ")
    tarjeta_cvv = input("Ingrese el código de seguridad (CVV): ")

    if (tarjeta_numero, tarjeta_expiracion, tarjeta_cvv):
        print("Tarjeta válida. Procesando transacción...")
        print("Transacción exitosa. El pago ha sido procesado.")
    else:
        print("Tarjeta inválida. El pago no pudo ser procesado.")


def cargar_inventario():
    with open("productos.json", "r") as file:
        productos = json.load(file)
    inventario = {producto["nombre"]: producto["stock"] for producto in productos}
    return inventario

def restar_inventario(productos_en_carrito):
    print("Actualizando el inventario...")
    inventario = cargar_inventario()

    for producto, cantidad in productos_en_carrito.items():
        if producto in inventario:
            for talla, stock in inventario[producto].items():
                if talla in cantidad and inventario[producto][talla] >= cantidad[talla]:
                    inventario[producto][talla] -= cantidad[talla]
                    print(f"Stock de {producto} (Talla {talla}) actualizado.")
                else:
                    print(f"No hay suficiente stock de {producto} (Talla {talla}). Actualización de inventario cancelada.")
        else:
            print(f"Producto {producto} no encontrado en el inventario.")

    with open("productos.json", "w") as file:
        json.dump(producto, file, indent=4)
        productos_en_carrito = {
    "Jordan 1 Retro High OG Spider-Man Across the Spider-Verse": {
        "US 9": 1,
        "US 9.5": 1
    },
    "SB Dunk Low Travis Scott": {
        "US 10": 2
    }
}

    restar_inventario(productos_en_carrito)

def generar_factura(cliente, total):
    factura = {
        "cliente": f"{cliente.nombre} {cliente.apellido}",
        "total": total
    }
    with open("factura.json", "w") as archivo:
        json.dump(factura, archivo)
    print("Factura generada y guardada.")

def realizar_compra(cliente):
    total = cliente.obtener_total_carrito()
    print(f"El total de la compra es: ${total}")
    confirmacion = input("¿Desea confirmar la compra? (s/n): ")

    if confirmacion.lower() == "s":
        procesar_pago(total)
        restar_inventario(cliente.carrito)
        generar_factura(cliente, total)
        
        cliente.carrito = []  # Vaciar el carrito después de la compra
        cliente.guardar_en_json()  # Guardar la información actualizada del cliente
        print("¡Compra realizada con éxito! Gracias por su compra.")
    else:
        print("Compra cancelada. Gracias por visitar nuestra tienda.")
