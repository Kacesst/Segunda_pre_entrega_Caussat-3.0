class ProductoEnCarrito:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad

def ver_carrito(cliente):
    print("===== CARRITO DE COMPRAS =====")
    
    if not cliente.carrito:
        print("El carrito está vacío.")
        return
    
    total_precio = 0
    for producto_en_carrito in cliente.carrito:
        producto = producto_en_carrito.producto
        cantidad = producto_en_carrito.cantidad
        precio_total_producto = producto.precio * cantidad
        total_precio += precio_total_producto
        
        print(f"Producto: {producto.nombre}")
        print(f"Cantidad: {cantidad}")
        print(f"Precio unitario: {producto.precio}")
        print(f"Precio total: {precio_total_producto}")
        print("------------------------")
    
    print(f"Total a pagar: {total_precio}")

def agregar_al_carrito(cliente, producto, cantidad):
    producto_en_carrito = ProductoEnCarrito(producto, cantidad)
    cliente.carrito.append(producto_en_carrito)
    print(f"{cantidad} {producto.nombre} agregado(s) al carrito.")

def vaciar_carrito(cliente):
    cliente.carrito = []
    print("El carrito ha sido vaciado.")
